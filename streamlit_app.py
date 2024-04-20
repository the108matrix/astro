import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

"""
# Here are possible allergies right now:
"""
# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'What would you like to do?',
    ('Show pollen distribution', 'Enter symptoms', 'Get alerts')
)
