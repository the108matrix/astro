import streamlit as st
import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
import altair as alt
import datetime
import time

#########################################################################################
# Load data


DATA_PATH = ('last_aftershocks.csv')

def load_data():
    data = pd.read_csv(DATA_PATH,sep=';')
    #data['Date'] = pd.to_datetime(data['Date'],format='%Y-%m-%d T%h%m%s' ).dt.strftime('%Y-%m-%d')
    return data

st.title('Earthquakes')

# Load rows of data into the dataframe.
if st.checkbox('Show dataframe'):
    df = load_data()

st.write(df)

df['Date'] = pd.to_datetime(df['Date']).dt.date

# find number of Earthquake 
earthquake_count = df.groupby('Date').size()

# create a nw data frame 
deprem_df = pd.DataFrame({'Date': earthquake_count.index, 'count_eq': earthquake_count.values})
print(deprem_df)

#Streamlit application
st.title('Number of Earthquake Per Day')
st.write(deprem_df)

# plotting
st.line_chart(deprem_df.set_index('Date'))

#bar chart
#fig, ax = plt.subplots()
#ax.bar(deprem_df['Date'], deprem_df['count_eq'])
#plt.xticks(rotation=45, ha='right')
#plt.xlabel('Date')
#plt.ylabel('Count')
#plt.title('Number of Earthquake')
#st.pyplot(fig)

# explanation fo plotting
#st.write("""
#plot, Number of earthquake per day.
#""")

st.title('Earthquake Map')

# Map
st.map(df,size=20, color='#bb55ff')
