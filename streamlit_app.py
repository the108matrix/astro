import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

# Dummy student database (replace with your database integration)
students = {
    'Alice': {'marks': 85},
    'Bob': {'marks': 70},
    'Charlie': {'marks': 60}
}

# Function to check admission criteria
def check_admission(student_name):
    if student_name in students:
        marks = students[student_name]['marks']
        if marks >= 75:
            return f"{student_name} is admitted!"
        else:
            return f"{student_name} does not meet admission criteria."
    else:
        return f"{student_name} is not found in the database."

# Function to handle chatbot responses
def get_chatbot_response(user_input, students):
    if user_input.strip() == 'view students':
        return '\n'.join([f'{student}: {details["marks"]}' for student, details in students.items()])
    else:
        return str(chatbot.get_response(user_input))

# Streamlit UI
st.title('Education System')

# Add new student form
st.subheader('Add New Student')
new_student_name = st.text_input('Enter student name:')
new_student_marks = st.number_input('Enter student marks:', min_value=0, max_value=100)

if st.button('Add Student'):
    students[new_student_name] = {'marks': new_student_marks}
    st.success(f'{new_student_name} added successfully!')

# View existing students and marks
st.subheader('Existing Students and Marks')
for student, details in students.items():
    st.write(f'{student}: {details["marks"]}')

# Chatbot interface
st.subheader('Chat with EducationBot')
user_input = st.text_input('You:')

if st.button('Send'):
    response = get_chatbot_response(user_input, students)
    st.write('EducationBot:', response)

# Admission checker
st.subheader('Admission Checker')
admission_student = st.text_input('Enter student name to check admission:')
if st.button('Check Admission'):
    admission_result = check_admission(admission_student)
    st.write(admission_result)
