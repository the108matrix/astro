import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import smtplib


st.title('SHS Computer Science Site')
st.header('This brand new site, coded in Python with hosting/library provided by _Streamlit.io_, is for all things Computer Science within Sahuarita High School, this website will provide resources for things such as the CS TSA Test.')

st.divider()

suggestions = st.text_input('Have any suggestions? Feedback such as bugs or even suggestions can help make the site better!')

