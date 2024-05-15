import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import requests,json,hashlib,uuid
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
this is pretty new, but it's not all me - I'm messing with the `streamlit` library because I want to work their new `st.experimental_data_editor` feature into some private code.
"""

sessionid = ''

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
    db.addcontact(email=nemail,phone=nphone,fn=nfn,ln=nln,salt=nsalt,hash=nhash)
    pop.__exit__()

pop2 = st.popover('existing acct')
email = pop2.text_input(label='email',value='',max_chars=50,type='default')
pw = pop2.text_input(label='pw',value='',max_chars=50,type='password')

c = db.getcbyemail(email=email)
#st.caption(c)


if c and 'salt' in c.keys() and pw: hash = hashlib.sha512(f"{c['salt']}{pw}".encode(encoding="utf-8"))
else: hash = None
if hash: pop2.caption(str(hash.hexdigest()))

def savepw():
    pop2.caption(str(db.updatehash(cid=c['id'],hash=hash.hexdigest())))
def checkhash():
    if hash.hexdigest() == c['hash']: 
        pop2.caption('correct pw')
        return True
    else: 
        pop2.caption('incorrect pw')
        return False
if sessionid and pop2.button(label='save pw'):
    if hash: savepw()
#if pop2.button(label='check pw'):
#    if hash: checkhash()

if pop2.button('login'): 
    if hash and checkhash():
        ex = db.getsesh(c['id'])
        if not ex: ex = pop2.caption(str(db.addsesh(c['id'])))
        #for k in ex.keys():
        #        pop2.caption(f"{k}: {ex[k]}",help=str(ex[k]))
        pop2.caption(str(ex))
        sessionid = ex['id']
seshdata = db.seshdata(sessionid)
#st.caption(f"sesh: {str(seshdata)}")
worked = None
#q = st.caption(f"worked: {str(worked)}")

if sessionid: 
    chpw = st.popover('change pw')
    npw = chpw.text_input('new pw',type='password')
    if npw and chpw.button('update'):
        pass
    st.link_button('DL my resume',url='https://hartzell.io/resume')
    if sessionid and st.button('delete acct'):
        worked = db.delcontact(seshdata['cid'])
        st.caption(str(worked))
        if worked: 
            st.toast('account deleted')
            st.caption('deleted')
            sessionid = ''
        else: 
            st.toast('failed to delete acct')
            st.caption('not deleted')

#accttonuke = st.text_input('cid to nuke')
#if st.button('nuke acct'):
#    worked = db.delcontact(accttonuke)
#    if worked: accttonuke = ''

#clist = db.contactrept()
#df = pd.DataFrame(clist)
#stuff = st.popover('data editor')
#edited = stuff.data_editor(df)
#st.caption(edited)

defautgraph = st.popover('default graph',help='comes with project template')
defautgraph.caption('I could not bring myself to delete this from the template. Also 669 points & 114 turns looks pretty cool btw')
num_points = defautgraph.slider("Number of points in spiral", 1, 10000, 1100)
num_turns = defautgraph.slider("Number of turns in spiral", 1, 300, 31)

indices = np.linspace(0, 1, num_points)
theta = 2 * np.pi * num_turns * indices
radius = indices

x = radius * np.cos(theta)
y = radius * np.sin(theta)

df = pd.DataFrame({
    "x": x,
    "y": y,
    "idx": indices,
    "rand": np.random.randn(num_points),
})

defautgraph.altair_chart(alt.Chart(df, height=700, width=700)
    .mark_point(filled=True)
    .encode(
        x=alt.X("x", axis=None),
        y=alt.Y("y", axis=None),
        color=alt.Color("idx", legend=None, scale=alt.Scale()),
        size=alt.Size("rand", legend=None, scale=alt.Scale(range=[1, 150])),
    ))

"""
`///streamlit testing zone///`   `///streamlit testing zone///`   `///streamlit testing zone///`
"""