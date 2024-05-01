import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Function to load student data from Excel sheet
def load_student_data():
    # Read student data from Excel sheet
    student_data = pd.read_excel("student_data.xlsx")
    return student_data

# Function to filter students by course eligibility
def filter_students_by_course(course):
    student_df = load_student_data()
    if course == "Science":
        eligible_students = student_df[student_df["Marks"] >= 80]
    elif course == "Economics":
        eligible_students = student_df[student_df["Marks"] >= 75]
    elif course == "Humanities":
        eligible_students = student_df[student_df["Marks"] >= 70]
    else:
        eligible_students = pd.DataFrame(columns=["Name", "Marks"])  # Return empty DataFrame if course is not recognized
    return eligible_students

# Streamlit UI
st.title('Education System')

# Sidebar navigation
page = st.sidebar.radio("Navigation", ('Home', 'Add Student', 'Admission Checker', 'Course Eligibility', 'Data Visualization'))

if page == 'Home':
    st.subheader('Welcome to the Education System!')
    st.write("This platform allows you to manage student data and check admission eligibility.")
    st.write("To get started, you can:")
    st.write("- Click on 'Manage Students' to view student data.")

    if st.button("Manage Students"):
        student_df = load_student_data()
        st.write(student_df)  # Display student data

elif page == 'Add Student':
    st.subheader('Add New Student')
    name = st.text_input("Enter student name:")
    marks_str = st.text_input("Enter student marks:")

    try:
        marks = int(marks_str)
        if st.button('Add Student'):  # Button click to add student
            student_df = add_student(name, marks)  # Update the DataFrame after adding student
            st.write(student_df)  # Display updated student data
    except ValueError:
        st.error("Please enter a valid integer for marks.")

elif page == 'Admission Checker':
    st.subheader('Admission Checker')
    name = st.text_input("Enter student name to check admission:")

    if st.button('Check Admission'):  # Button click to check admission
        student_df = load_student_data()
        if name in student_df["Name"].values:
            st.write("Student found.")
        else:
            st.write("Student not found.")

elif page == 'Course Eligibility':
    st.subheader('Course Eligibility')
    course = st.selectbox("Select a course:", ["Science", "Economics", "Humanities"])

    st.write(f"Students eligible for {course} course:")
    eligible_students = filter_students_by_course(course)
    st.write(eligible_students)

elif page == 'Data Visualization':
    st.subheader('Data Visualization')

    # Load student data
    student_df = load_student_data()

    # Check if the "Marks" column exists
    if "Marks" not in student_df.columns:
        st.error("The 'Marks' column is missing in the student data.")
    else:
        # Histogram of student marks distribution
        st.write("Histogram of Student Marks Distribution")
        plt.hist(student_df["Marks"], bins=10, color='skyblue', edgecolor='black')
        plt.xlabel('Marks')
        plt.ylabel('Frequency')
        plt.title('Distribution of Student Marks')
        st.pyplot()
