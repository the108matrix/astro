import streamlit as st
import pandas as pd

# Load data
DATA_PATH = 'turkey_earthquakes.csv'

def load_data():
    data = pd.read_csv(DATA_PATH, sep=',')
    return data

df = load_data()

# UI

# Split the screen into two columns
col1, col15,col2 = st.columns([5,1, 25])

# Parameters in the left column
with col1:
    st.subheader('Filter Parameters')
    
    # Date range selection
    df['DateOnly'] = df['Date'].str.split(' ').str[0]
    df['DateOnly'] = df['DateOnly'].str.replace('/','-')
    df['DateOnly'] = pd.to_datetime(df['DateOnly'], format='%d-%m-%Y')
    min_date = df['DateOnly'].min()
    max_date = df['DateOnly'].max()
    start_date = st.date_input('Start date', min_date, min_value=min_date, max_value=max_date)
    end_date = st.date_input('End date', max_date, min_value=min_date, max_value=max_date)
    start_date = pd.to_datetime(start_date)
    
    end_date = pd.to_datetime(end_date)

    
    # Magnitude range selection
    min_mag = st.number_input('Minimum Magnitude', min_value=0.0, max_value=10.0)
    max_mag = st.number_input('Maximum Magnitude', min_value=0.0, max_value=10.0)

# Filter data based on selected date range and magnitude range
filtered_df = df[(df['DateOnly'] >= start_date) & (df['DateOnly'] <= end_date)]
if min_mag != 0.0 or max_mag != 10.0:
    filtered_df = filtered_df[(filtered_df['Magnitude'] >= min_mag) & (filtered_df['Magnitude'] <= max_mag)]

# Number of earthquakes per day
earthquake_count = filtered_df.groupby('DateOnly').size()
deprem_df = pd.DataFrame({'DateOnly': earthquake_count.index, 'count_eq': earthquake_count.values})

# Show table in the right column
with col15:
    st.empty()
with col2:
    st.title('Turkey Earthquakes')
    # Show data checkbox
    if st.checkbox('Show data'):
        st.write(df)

    # Show table checkbox
    
    
    # Show selected data checkbox
    tab1, tab2,tab3= st.tabs(["🗃 Num.of EQs","🗃 Filtered Data","📈 Chart"])
    tab1.subheader("Number of Earthquake")
    tab1.write(deprem_df)

    
    tab2.subheader("Filtered Data")
    tab2.write(filtered_df)

    # Plotting
    tab3.subheader("Chart")
    tab3.line_chart(deprem_df.set_index('DateOnly'))

    # Earthquake Map
    st.title('Earthquake Map')
    st.map(filtered_df, size=20, color='#bb55ff')
