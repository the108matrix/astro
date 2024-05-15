import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import requests,json,hashlib
from sdb import dbc
db = dbc(un=st.secrets['db_username'],pw=st.secrets['db_token'],host=st.secrets['db_addr'],port=st.secrets['db_port'],db=st.secrets['db_db'])
st.caption(db.motd())

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
this is pretty sweet isn't it, but it's not all me.
I'm messing with the `streamlit` library because I want to work their new `st.experimental_data_editor` feature into some private code.
"""

cresp = requests.get(url='https://hartzell.io/stats/getcontacts')
st.caption(body=f"{cresp.status_code} - {cresp.content.decode()}",unsafe_allow_html=True)
df = pd.DataFrame(json.loads(cresp.content.decode()))

edited = st.data_editor(df)
st.caption(edited)

email = st.text_input(label='email',value='',max_chars=50,type='default')
pw = st.text_input(label='pw',value='',max_chars=50,type='password')

st.caption(body=f"{email} {pw}")

c = requests.post(url='https://hartzell.io/sec/getc',json={'sesh':'','email':email,'hash':'','exp':''})
st.caption(f"{c.status_code} {c.content.decode()}")

if c.status_code == 200: cdata = json.loads(c.content.decode())
else: cdata = None
if cdata and 'salt' in cdata.keys(): hash = hashlib.sha512(f"{cdata['salt']}{pw}")
else: hash = None
if hash: st.caption(hash)


"""
669 points & 114 turns looks pretty cool btw
"""

num_points = st.slider("Number of points in spiral", 1, 10000, 1100)
num_turns = st.slider("Number of turns in spiral", 1, 300, 31)

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

st.altair_chart(alt.Chart(df, height=700, width=700)
    .mark_point(filled=True)
    .encode(
        x=alt.X("x", axis=None),
        y=alt.Y("y", axis=None),
        color=alt.Color("idx", legend=None, scale=alt.Scale()),
        size=alt.Size("rand", legend=None, scale=alt.Scale(range=[1, 150])),
    ))
