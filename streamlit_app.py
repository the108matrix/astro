import streamlit as st
import pandas as pd
import numpy as np

# Load data
DATA_PATH = 'last_aftershocks.csv'

def load_data():
    data = pd.read_csv(DATA_PATH, sep=';')
    return data

df = load_data()

# UI
st.title('Earthquakes')

# Show data checkbox
if st.checkbox('Show data'):
    st.write(df)
    

#df['Date'] = pd.to_datetime(df['Date']).dt.date
df['DateOnly'] = df['Date'].str.split('T').str[0]

# Yeni oluşturulan tarih sütununu datetime formatına çevir
df['DateOnly'] = pd.to_datetime(df['DateOnly'], format='%Y-%m-%d')


#df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%dT%H:%M:%S')
# Date range selection
min_date = df['DateOnly'].min()
max_date = df['DateOnly'].max()




start_date = st.date_input('Start date', min_date, min_value=min_date, max_value=max_date)
end_date = st.date_input('End date', max_date, min_value=min_date, max_value=max_date)
start_date = pd.to_datetime(start_date)
end_date = pd.to_datetime(end_date)

print(start_date,end_date)

# Filter data based on selected date range
#df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%dT%H:%M:%S').dt.date
filtered_df = df[(df['DateOnly'] >= start_date) & (df['DateOnly'] <= end_date)]

# Number of earthquakes per day
earthquake_count = filtered_df.groupby('DateOnly').size()
deprem_df = pd.DataFrame({'DateOnly': earthquake_count.index, 'count_eq': earthquake_count.values})

# Show table checkbox
if st.checkbox('Show table'):
    st.write(deprem_df)
    
# Show table checkbox
if st.checkbox('Show selected data'):
    st.write(filtered_df)


# Plotting
st.line_chart(deprem_df.set_index('DateOnly'))

# Earthquake Map
st.title('Earthquake Map')
st.map(filtered_df, size=20, color='#bb55ff')
