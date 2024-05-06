import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load fake middle school data
middle_school_data = {
    'Student_ID': np.arange(1, 101),
    'Grade_Level': np.random.choice(['6th', '7th', '8th'], size=100),
    'Math_Score': np.random.randint(60, 100, size=100),
    'Science_Score': np.random.randint(60, 100, size=100),
    'English_Score': np.random.randint(60, 100, size=100)
}

# Load fake IB school data
ib_school_data = {
    'Student_ID': np.arange(1, 101),
    'Grade_Level': np.random.choice(['9th', '10th', '11th', '12th'], size=100),
    'Math_Score': np.random.randint(70, 100, size=100),
    'Science_Score': np.random.randint(70, 100, size=100),
    'English_Score': np.random.randint(70, 100, size=100)
}

# Create DataFrames
middle_school_df = pd.DataFrame(middle_school_data)
ib_school_df = pd.DataFrame(ib_school_data)

# Streamlit App
st.title('Student Performance Dashboard')

# Sidebar to select school type
school_type = st.sidebar.selectbox('Select School Type', ['Middle School', 'IB School'])

# Data selection based on school type
if school_type == 'Middle School':
    selected_df = middle_school_df
else:
    selected_df = ib_school_df

# Display raw data
st.subheader('Raw Data')
st.write(selected_df)

# Data visualization
st.subheader('Average Scores by Grade Level')

# Calculate average scores by grade level
avg_scores = selected_df.groupby('Grade_Level').mean()

# Plotting
fig, ax = plt.subplots()
avg_scores.plot(kind='bar', ax=ax)
ax.set_ylabel('Average Score')
ax.set_xlabel('Grade Level')
ax.set_title('Average Scores by Grade Level')
st.pyplot(fig)
