import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import requests,json,hashlib,uuid,datetime,pytz
from sdb import dbc
db = dbc(un=st.secrets['db_username'],pw=st.secrets['db_token'],host=st.secrets['db_addr'],port=st.secrets['db_port'],db=st.secrets['db_db'])
#st.caption(db.motd())

#"""
# Welcome to Streamlit!
#
#Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:.
#If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
#forums](https://discuss.streamlit.io).
#
#In the meantime, below is an example of what you can do with just a few lines of code:
#"""

#thing = st.html('<h1>James was here</h1>')
#https://docs.streamlit.io/develop/concepts/design/dataframes?ref=blog.streamlit.io

"""
`///streamlit testing zone///`   `///streamlit testing zone///`   `///streamlit testing zone///`
"""
"""
this is pretty neat, but it's not all me - I'm messing with the `streamlit` library because I want to test out their new `st.data_editor` feature in some private code.
yeet
"""

#if 'count' not in st.session_state:
#    st.session_state.count = 0
#def increment_counter(increment_value=0):
#    st.session_state.count += increment_value
#def decrement_counter(decrement_value=0):
#    st.session_state.count -= decrement_value
#st.button('Increment', on_click=increment_counter,
#	kwargs=dict(increment_value=5))
#st.button('Decrement', on_click=decrement_counter,
#	kwargs=dict(decrement_value=1))
#st.write('Count = ', st.session_state.count)

if 'sessionid' not in st.session_state: 
    st.session_state.sessionid = ''
    seshdata = None
    c = None
st.caption(f"sid {st.session_state.sessionid}")
if st.session_state.sessionid != '':
    seshdata = db.seshdata(st.session_state.sessionid)
    #st.caption(seshdata)
    c = db.getcontact(seshdata['cid'])
    if datetime.datetime.now() > datetime.datetime.strptime(seshdata['exp'],'%Y-%m-%dT%H:%M:%S+00:00'):
        st.session_state.sessionid = ''
        seshdata = None

if st.session_state.sessionid == '':
    c = None
    pop = st.popover('new acct')
    nsalt = str(uuid.uuid4())
    nfn = pop.text_input('fn')
    nln = pop.text_input('ln')
    nphone = pop.text_input('phone')
    nemail = pop.text_input('email*')
    npw = pop.text_input('pw*',type='password')
    if npw and npw != '': nhash = hashlib.sha512(f"{nsalt}{npw}".encode(encoding="utf-8"),usedforsecurity=True).hexdigest()
    else: nhash = None
    if nhash and pop.button('register'):
        st.session_state['sessionid'] = db.addcontact(email=nemail,phone=nphone,fn=nfn,ln=nln,salt=nsalt,hash=nhash)['id']

if st.session_state.sessionid == '':
    c = None
    pop2 = st.popover('existing acct')
    email = pop2.text_input(label='email',value='',max_chars=50,type='default')
    pw = pop2.text_input(label='pw',value='',max_chars=50,type='password')
    if email != '': c = db.getcbyemail(email)
    pop2.caption(c)

    if c and 'salt' in c.keys() and pw: hash = hashlib.sha512(f"{c['salt']}{pw}".encode(encoding="utf-8"),usedforsecurity=True)
    else: hash = None
    if hash: pop2.caption(str(hash.hexdigest()))

    def savepw():
        pop2.caption(str(db.updatehash(cid=c['cid'],hash=hash.hexdigest())))
    def checkhash():
        if hash.hexdigest() == c['hash']: 
            pop2.caption('correct pw')
            return True
        else: 
            pop2.caption('incorrect pw')
            return False
    if st.session_state.sessionid and pop2.button(label='save pw'):
        if hash: savepw()
    if pop2.button(label='check pw'):
        if hash: checkhash()

    if pop2.button('login'): 
        if hash and checkhash():
            ex = db.getsesh(c['id'])
            if not ex: 
                ex = db.addsesh(c['id'])
                st.session_state['sessionid'] = ex['id']
                st.session_state.sessionid = ex['id']
            #for k in ex.keys():
            #        pop2.caption(f"{k}: {ex[k]}",help=str(ex[k]))
            pop2.caption(str(ex))
            st.session_state.sessionid = ex['id']
    seshdata = db.seshdata(st.session_state.sessionid)
    #st.caption(f"sesh: {str(seshdata)}")
    worked = None
    #q = st.caption(f"worked: {str(worked)}")

if st.session_state.sessionid != '':
    if st.button('logout'):
        db.delsesh(st.session_state.sessionid)
        st.session_state.sessionid = ''
    chpw = st.popover('change pw')
    npw = chpw.text_input('new pw',type='password')
    if npw and 'salt' in c.keys() and chpw.button('update'):
        chash = hashlib.sha256(f"{c['salt']}{npw}".encode(encoding='utf-8'),usedforsecurity=True).hexdigest()
        db.updatehash(cid=c['cid'],hash=chash)
        st.toast('pw updated')
    st.link_button('DL my resume',url='https://hartzell.io/resume')
    if st.session_state.sessionid and st.button('delete acct'):
        worked = db.delcontact(seshdata['cid'])
        st.caption(str(worked))
        if worked: 
            st.toast('account deleted')
            st.caption('deleted')
            st.session_state.sessionid = ''
        else: 
            st.toast('failed to delete acct')
            st.caption('not deleted')
    
    fwd = db.fwrept()
    #st.caption(fwd)
    fwf = pd.DataFrame(fwd)
    #st.caption(fwf)
    edits = st.data_editor(fwf.copy(),use_container_width=True,num_rows='dynamic',column_config={'id':None})
    rows = fwf.to_dict('records')
    st.caption(f'rows {rows}')
    rows2 = edits.to_dict('records')
    st.caption(f'rows2 {rows2}')
    ops = []
    if st.button('save fw'):
        for row in rows:
            if row not in rows2: 
                db.fwdel(row['id'])
                #ops.append('fwdel')
            else:
                for row2 in rows2:
                    if row['id'] == row2['id'] and row['asdf'] != row2['asdf']:
                        db.fwup(row2['id'],row2['asdf'])
                        #ops.append('fwup')
        for row2 in rows2:
            if row2 not in rows: db.fwadd(row2['asdf'])
    #st.caption(f'ops {ops}')


#accttonuke = st.text_input('cid to nuke')
#if st.button('nuke acct'):
#    worked = db.delcontact(accttonuke)
#    if worked: accttonuke = ''

#clist = db.contactrept()
#df = pd.DataFrame(clist)
#stuff = st.popover('data editor')
#edited = stuff.data_editor(df)
#st.caption(edited)

#defautgraph = st.popover('default graph',help='comes with project template')
#defautgraph.caption('I could not bring myself to delete this from the template. Also 669 points & 114 turns looks pretty cool btw')
#num_points = defautgraph.slider("Number of points in spiral", 1, 10000, 1100)
#num_turns = defautgraph.slider("Number of turns in spiral", 1, 300, 31)
#
#indices = np.linspace(0, 1, num_points)
#theta = 2 * np.pi * num_turns * indices
#radius = indices
#
#x = radius * np.cos(theta)
#y = radius * np.sin(theta)
#
#df = pd.DataFrame({
#    "x": x,
#    "y": y,
#    "idx": indices,
#    "rand": np.random.randn(num_points),
#})
#
#defautgraph.altair_chart(alt.Chart(df, height=700, width=700)
#    .mark_point(filled=True)
#    .encode(
#        x=alt.X("x", axis=None),
#        y=alt.Y("y", axis=None),
#        color=alt.Color("idx", legend=None, scale=alt.Scale()),
#        size=alt.Size("rand", legend=None, scale=alt.Scale(range=[1, 150])),
#    ))

"""
`///streamlit testing zone///`   `///streamlit testing zone///`   `///streamlit testing zone///`
"""