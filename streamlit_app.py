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

# Chatbot function
def chatbot(student_df, query):
    if "view students" in query.lower():
        return student_df.to_markdown()
    elif "add student" in query.lower():
        st.subheader("Add New Student")
        name = st.text_input("Enter student name:")
        marks_str = st.text_input("Enter student marks:")
        try:
            marks = int(marks_str)
            if marks >= 75:
                student_df = add_student(student_df, name, marks)
                return f"{name} added successfully!"
            else:
                return "Marks should be 75 or greater for admission."
        except ValueError:
            return "Please enter a valid integer for marks."
    elif "check admission" in query.lower():
        st.subheader("Admission Checker")
        name = st.text_input("Enter student name to check admission:")
        return check_admission(student_df, name)
    else:
        return "I'm sorry, I didn't understand that query."

# Streamlit UI
st.title('Education System')

# Load student data
student_df = load_student_data()

# Chatbot interface
st.subheader('Chat with EducationBot')
user_input = st.text_input('You:')

if st.button('Send'):
    response = chatbot(student_df, user_input)
    st.markdown(response)

# View existing students and marks
st.subheader('Existing Students and Marks')
st.write(student_df)
