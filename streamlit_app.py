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
        
# Chatbot interface
st.subheader('Chat with EducationBot')
user_input = st.text_input('You:')

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

# Add new student form
st.subheader('Add New Student')
new_student_name = st.text_input('Enter student name:')
new_student_marks = st.text_input('Enter student marks:')

# Use session state to generate unique keys
if "add_student_key_count" not in st.session_state:
    st.session_state["add_student_key_count"] = 0

add_student_button_key = f"add_student_button_{st.session_state['add_student_key_count']}"

if st.button('Add Student', key=add_student_button_key):
    try:
        marks = int(new_student_marks)
        if marks >= 75:
            student_df = add_student(student_df, new_student_name, marks)
            st.success(f'{new_student_name} added successfully!')
        else:
            st.error("Marks should be 75 or greater for admission.")
    except ValueError:
        st.error("Please enter a valid integer for marks.")
    st.session_state["add_student_key_count"] += 1

# View existing students and marks
st.subheader('Existing Students and Marks')
st.write(student_df)


# Use session state to generate unique keys
if "send_button_key_count" not in st.session_state:
    st.session_state["send_button_key_count"] = 0

send_button_key = f"send_button_{st.session_state['send_button_key_count']}"

if st.button('Send', key=send_button_key):
    response = chatbot(student_df, user_input)
    st.markdown(response)
    st.session_state["send_button_key_count"] += 1

# Admission checker
st.subheader('Admission Checker')
admission_student = st.text_input('Enter student name to check admission:')

# Use session state to generate unique keys
if "check_admission_key_count" not in st.session_state:
    st.session_state["check_admission_key_count"] = 0

check_admission_button_key = f"check_admission_button_{st.session_state['check_admission_key_count']}"

if st.button('Check Admission', key=check_admission_button_key):
    admission_result = check_admission(student_df, admission_student)
    st.write(admission_result)
    st.session_state["check_admission_key_count"] += 1

# Chat input functionality
prompt = st.text_input("Say something")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")
