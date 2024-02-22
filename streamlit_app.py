import streamlit as st
import pandas as pd
import plotly.express as px


# Load data
DATA_PATH = 'turkey_earthquakes.csv'

def load_data():
    data = pd.read_csv(DATA_PATH, sep=',')
    return data

df = load_data()

# UI

# Split the screen into two columns
#col1, col15,col2 = st.columns([0.15,0.5, 0.6])
col1, col15,col2 = st.columns([1,0.5,2])

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
    min_mag = st.number_input('Minimum Magnitude', min_value=0.0, max_value=10.0,value=5.0,step=0.1)
    max_mag = st.number_input('Maximum Magnitude', min_value=0.0, max_value=10.0, value=9.0,step=0.1)

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
        st.dataframe(df)

    # Show table checkbox
    
    
    # Show selected data checkbox
    tab1,tab2,tab3,tab4= st.tabs(["Map","🗃 Num.of EQs","🗃 Filtered Data","📈 Chart"])
    #tab1,tab2,tab3,tab4,tab5= st.tabs(["Map","🗃 Num.of EQs","🗃 Filtered Data","📈 Chart","Mag. Distribution"])
    # Earthquake Map

    
    # Draw the map with color-coded circles based on Magnitude
    tab1.subheader("Earthquake Map")

    # Draw the map with color-coded circles based on Magnitude
    if not filtered_df.empty:
    # Calculate the center of the map based on filtered data
        center_lat = filtered_df['latitude'].mean()
        center_lon = filtered_df['longitude'].mean()
        
        # Define magnitude ranges
        magnitude_ranges = [(0, 3), (3.1, 4), (4.1, 5), (5.1, 6), (6.1, 7), (7.1, 8), (8.1, 9),(9.1,float('inf'))]
        
        # Set colors for each magnitude range
        colors = ["yellow", "lightgreen", "blue", "orange", "red", "purple", "brown", "black"]
        mag_labels =["0.0-3.0", "3.1-4.0", "4.1-5.0", "5.1-6.0", "6.1-7.0", "7.1-8.0", "8.1-9.0","9.1<"]
        
        # Create a column to store color information based on Magnitude ranges
        filtered_df['Color'] = pd.cut(filtered_df['Magnitude'], bins=[range[0] for range in magnitude_ranges] + [float('inf')], labels=mag_labels, right=False)
        # Define a color palette for each magnitude range
        #color_palette = dict(zip(mag_labels, colors))
        color_palette = {
            "0.0-3.0": "yellow",
            "3.1-4.0": "lightgreen",
            "4.1-5.0": "blue",
            "5.1-6.0": "orange",
            "6.1-7.0": "red",
            "7.1-8.0": "purple",
            "8.1-9.0": "brown",
            "9.1<": "black"
        }
        # Create scatter mapbox plot
        fig = px.scatter_mapbox(filtered_df, lat="latitude", lon="longitude", color="Color", color_discrete_map=color_palette,
                                size="Magnitude", zoom=5, height=600, width=800,hover_name="Date",hover_data=["Magnitude"],
                                category_orders={"Color": ["0.0-3.0", "3.1-4.0", "4.1-5.0", "5.1-6.0", "6.1-7.0", "7.1-8.0", "8.1-9.0", "9.1<"]})
        
        
        fig.update_layout(mapbox_style="open-street-map")
        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
        fig.update_traces(marker=dict(size=7)) # Set marker size
        fig.update_layout(mapbox_center=dict(lat=center_lat, lon=center_lon))  # Center the map
        
        # Define magnitude ranges
        magnitude_ranges = [(0, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9),(9,float('inf'))]
        
        # Count earthquakes in each magnitude range
        magnitude_counts = [filtered_df[(filtered_df['Magnitude'] >= min_mag) & (filtered_df['Magnitude'] < max_mag)].shape[0] for min_mag, max_mag in magnitude_ranges]
        
        # Create a DataFrame for plotting
        magnitude_df = pd.DataFrame({'Magnitude Range': ['{}-{}'.format(min_mag, max_mag) for min_mag, max_mag in magnitude_ranges], 'Count': magnitude_counts})
        
        # Plot the bar chart with plotly
        fig_bar = px.bar(magnitude_df, x='Magnitude Range', y='Count', text='Count', color='Count')
        fig_bar.update_traces(texttemplate='%{text}', textposition='outside')
        fig_bar.update_layout(xaxis_tickangle=-45)
        fig_bar.update_yaxes(type="log")
        
        # Display the plots
        tab1.plotly_chart(fig)
        tab1.plotly_chart(fig_bar)

    else:
        tab1.write("No earthquakes found in the selected range.")
            
    tab2.subheader("Number of Earthquake")
    tab2.write(deprem_df)

    
    tab3.subheader("Filtered Data")
    tab3.write(filtered_df)

    # Plotting
    tab4.subheader("Chart")
    tab4.bar_chart(deprem_df.set_index('DateOnly'))
