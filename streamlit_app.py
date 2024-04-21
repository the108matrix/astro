import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

st.title('PollenPal')

st.write("Welcome to PollenPal! This app will help you track pollen levels in your area and provide you with alerts when pollen levels are high.")

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
        df = pd.DataFrame(
            np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
            columns=['lat', 'lon'])

        st.map(df)


# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'What would you like to do?',
    ('Show pollen distribution', 'Enter symptoms', 'Get alerts')
)
