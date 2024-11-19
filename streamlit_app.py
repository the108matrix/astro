import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
from jyotishyamitra import *
import plotly.express as px

# Function to display planet details for a given date and chart type
def get_planet_details(date, name, gender, lat, long, tz, chart_type="D1"):
    inputdata = jsm.input_birthdata(name=name, gender=gender, year=date.year, month=date.month,
                                    day=date.day, place="", longitude=long, lattitude=lat, timezone=tz,
                                    hour=12, min=0, sec=0)

    jsm.validate_birthdata()

    if jsm.IsBirthdataValid():
        birthdata = jsm.get_birthdata()
        astrodata = jsm.generate_astrologicalData(birthdata, returnval="ASTRODATA_DICTIONARY")

        if astrodata and chart_type in astrodata:
            planets_details = astrodata[chart_type].get('planets', {})
            df_planets = pd.DataFrame(planets_details).T
            df_planets['Aspects_Houses'] = df_planets['Aspects'].apply(lambda x: x.get('houses', []))
            df_planets['Aspects_Planets'] = df_planets['Aspects'].apply(lambda x: x.get('planets', []))
            df_planets['Aspects_Signs'] = df_planets['Aspects'].apply(lambda x: x.get('signs', []))
            df_planets.drop(['Aspects', 'pos', 'rashi', 'house-nature', 'gender', 'house-num',
                             'friends', 'enemies', 'nuetral', 'varna', 'guna', 'status', df_planets.columns[0]],
                            axis=1, inplace=True)
            df_planets['Date'] = date
            return df_planets

    return pd.DataFrame()

# Streamlit App
st.title("Astrological Chart Visualization")

# Sidebar for user input
st.sidebar.header("Input Parameters")
name = st.sidebar.text_input("Name", "Aaina")
gender = st.sidebar.selectbox("Gender", ["Female", "Male"])
lat = st.sidebar.number_input("Latitude", value=28.0724)
long = st.sidebar.number_input("Longitude", value=75.8229)
tz = st.sidebar.number_input("Time Zone", value=5.5)

start_date = st.sidebar.date_input("Start Date", datetime(1990, 6, 19))
end_date = st.sidebar.date_input("End Date", datetime(1990, 11, 19))

chart_type = st.sidebar.selectbox("Chart Type", ["D1", "D2", "D3", "D9", "D10"])
selected_symbols = st.sidebar.multiselect(
    "Select Symbols",
    options=["Sun", "Moon", "Mars", "Mercury", "Jupiter", "Venus", "Saturn", "Rahu", "Ketu"],
    default=["Sun", "Moon", "Mars", "Mercury"]
)

# Main section
if st.sidebar.button("Generate Chart"):
    st.write(f"Generating astrological data from **{start_date}** to **{end_date}** for chart type **{chart_type}**.")

    # Initialize list to collect DataFrames
    all_planet_details = []

    # Iterate through the date range
    current_date = datetime.combine(start_date, datetime.min.time())
    end_datetime = datetime.combine(end_date, datetime.min.time())

    while current_date <= end_datetime:
        df = get_planet_details(current_date, name, gender, lat, long, tz, chart_type)
        if not df.empty:
            all_planet_details.append(df)
        current_date += timedelta(days=1)

    # Combine all DataFrames
    if all_planet_details:
        result_df = pd.concat(all_planet_details, ignore_index=True)

        # Filter by selected symbols
        filtered_df = result_df[result_df['symbol'].isin(selected_symbols)]

        # Visualization
        st.subheader("Nakshatra by Date")
        fig_nakshatra = px.scatter(
            filtered_df,
            x="Date",
            y="nakshatra",
            color="symbol",
            text="symbol",
            title=f"{chart_type} Chart: Planetary Transits by Nakshatra",
            labels={"nakshatra": "Nakshatra"}
        )
        fig_nakshatra.update_traces(textposition="top center", marker=dict(size=10))
        st.plotly_chart(fig_nakshatra)

        # Display the DataFrame
        st.subheader("Astrological Data")
        st.write(filtered_df)
    else:
        st.warning("No astrological data generated. Please check your inputs.")
