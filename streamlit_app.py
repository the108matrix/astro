import streamlit as st
import pandas as pd

# Function to load student data from Excel file
def load_student_data():
    try:
        return pd.read_excel("student_data.xlsx")
    except FileNotFoundError:
        return pd.DataFrame(columns=["Name", "Marks"])

# Function to add a new student to the DataFrame and Excel file
def add_student(student_df, name, marks):
    if marks >= 75:  # Check marks before adding
        new_student = pd.DataFrame([[name, marks]], columns=["Name", "Marks"])
        student_df = pd.concat([student_df, new_student], ignore_index=True)
        student_df.to_excel("student_data.xlsx", index=False)
        return student_df
    else:
        return student_df  # Don't add if marks < 75

# Function to check admission criteria
def check_admission(student_df, student_name):
    student_row = student_df.loc[student_df["Name"] == student_name]
    if not student_row.empty:
        marks = student_row.iloc[0]["Marks"]
        if marks >= 75:
            return f"{student_name} is admitted!"
        else:
            return f"{student_name} does not meet admission criteria (marks < 75)."
    else:
        return f"{student_name} is not found in the database."

# Streamlit UI
st.title('Education System')

# Load student data (hidden)
student_df = load_student_data()

# Add Student Section
st.sidebar.title('Navigation')
page = st.sidebar.radio("Go to", ('Home', 'Admission Checker'))

if page == 'Home':
    st.subheader('Home Page')
    st.write("Welcome to the Education System! This platform allows you to manage student data and check admission eligibility.")
    
    # Button to manage students
    if st.button("Manage Students"):
        st.write(student_df)  # Display student data
elif page == 'Admission Checker':
    st.subheader('Admission Checker')
    name = st.text_input("Enter student name to check admission:")

    if st.button('Check Admission'):  # Button click to check admission
        admission_status = check_admission(student_df, name)
        st.write(admission_status)
