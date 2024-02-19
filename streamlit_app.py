import streamlit as st
import pandas as pd

df =  pd.read_csv("last_aftershocks.csv",sep=";") 

    
st.write("Here's our first map:")
st.map(df,size=20, color='#bb55ff')


st.write("Here's data table:")
if st.checkbox('Show table'):
    df



