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
    new_student = pd.DataFrame([[name, marks]], columns=["Name", "Marks"])
    student_df = pd.concat([student_df, new_student], ignore_index=True)
    student_df.to_excel("student_data.xlsx", index=False)
    return student_df

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

# Load student data
student_df = load_student_data()

# Add new student form
st.subheader('Add New Student')
new_student_name = st.text_input('Enter student name:', key="new_student_name")
new_student_marks = st.number_input('Enter student marks:', min_value=0, max_value=100, key="new_student_marks")

# Unique key for each student
add_student_button_key = "add_student_button_" + new_student_name

if st.button('Add Student', key=add_student_button_key) and new_student_marks >= 75:
    student_df = add_student(student_df, new_student_name, new_student_marks)
    st.success(f'{new_student_name} added successfully!')
elif st.button('Add Student', key=add_student_button_key) and new_student_marks < 75:
    st.error("Marks should be 75 or greater for admission.")

# View existing students and marks
st.subheader('Existing Students and Marks')
st.write(student_df)

# Chatbot interface
st.subheader('Chat with EducationBot')
user_input = st.text_input('You:', key="user_input")
send_button_key = "send_button_" + user_input  # Unique key for each user input

if st.button('Send', key=send_button_key):
    response = "I'm sorry, I didn't understand that."
    st.write('EducationBot:', response)

# Admission checker
st.subheader('Admission Checker')
admission_student = st.text_input('Enter student name to check admission:', key="admission_student")
check_admission_button_key = "check_admission_button_" + admission_student  # Unique key for each admission check

if st.button('Check Admission', key=check_admission_button_key):
    admission_result = check_admission(student_df, admission_student)
    st.write(admission_result)

# Chat input functionality
prompt = st.text_input("Say something", key="chat_prompt")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")
