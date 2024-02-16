import streamlit as st
import numpy as np
import pandas as pd

#names= ['Date_Time','latitude','longitude','Depth(Km)','Type','Magnitude','Location','EventID']
df =  pd.read_csv("/home/murat/MEGA/streamlit/last_aftershocks.csv",sep=";") 

    
st.write("Here's our first map:")
st.map(df,size=20, color='#bb55ff')


st.write("Here's data table:")
if st.checkbox('Show table'):
    df



