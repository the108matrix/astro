import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

st.title('PollenPal')

st.write("Welcome to PollenPal! This app will help you track pollen levels in your area and provide you with alerts when pollen levels are high.")

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'What would you like to do?',
    ('Show pollen distribution', 'Enter symptoms', 'Get alerts')
)

if add_selectbox == 'Show pollen distribution':
    left_column, right_column = st.columns(2)
    # You can use a column just like st.sidebar:
    #left_column.button('Press me!')

    # Or even better, call Streamlit functions inside a "with" block:
    with right_column:
        st.write("Here are possible allergies right now:")
        chosen = st.radio(
            'Pollens',
            ("Hazel", "Alder", "Birch", "Grasses", "Ragweed"))
        st.write(f"This is the map of {chosen} pollen distribution")
        with left_column:
            if chosen == "Hazel":
                df1 = pd.DataFrame(
                    np.random.randn(1000, 2) / [50, 50] + [46.30, 6.37],
                    columns=['lat', 'lon'])

                st.map(df1, zoom=6)
            if chosen == "Alder":
                df = pd.DataFrame(
                    np.random.randn(1000, 2) / [50, 50] + [46.30, 6.37],
                    columns=['lat', 'lon'])

                st.map(df,zoom=6)

if add_selectbox == 'Enter symptoms':
    st.write("Enter your symptoms here:")
    symptoms = st.text_area("Symptoms")
    if st.button("Submit"):
        st.write("Symptoms submitted")

if add_selectbox == 'Get alerts':
    #st.write("To be alerted on your pollen alergies, please enter your email address below:")
    #alerts = st.text_area("Alerts")
    mail = st.text_input(
        "To be alerted on your pollen alergies, please enter your email address below:")
    add_selectbox = st.selectbox(
        'What would you like to be alerted on?',
        ("Hazel", "Alder", "Birch", "Grasses", "Ragweed", "Other"))
    if add_selectbox == "Other":
        other = st.text_area("Pollen type:")
    if st.button("Submit"):
        # code to integrate 'other pollen type'
        # code to send email alerts
        st.write("Alerts activated")