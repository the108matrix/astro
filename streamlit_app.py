import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import smtplib


st.title('SHS Computer Science Site')
st.write('This brand new site, coded in Python with hosting/library provided by _Streamlit.io_, is for all things Computer Science within Sahuarita High School, this website will provide resources for things such as the CS TSA Test.')
#st.image('shslogo.png', caption='Sahuarita High School Mustang', width=600)

st.divider()

st.header("Here is all of the available practice tests located below.")

with st.expander("Full TSA Practice Test", expanded=False):
  st.write("Place Holder")
                 

            
st.header("And here, is all of the available resources located below.")

st.divider()

st.write("This site is currently under construction, so please be patient with the site. Due to the limitations of the platform of the previous site, I have decided that it would be best to start fresh. I will be adding more features to the site as time goes on. Thank you.")
