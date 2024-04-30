import streamlit as st
import pandas as pd
import mysql.connector

# Function to connect to MySQL database
def connect_to_mysql():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="recovery",
        database="test"
    )

# Function to load student data from MySQL database
def load_student_data():
    conn = connect_to_mysql()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    columns = [desc[0] for desc in cursor.description]
    student_data = cursor.fetchall()
    cursor.close()
    conn.close()
    return pd.DataFrame(student_data, columns=columns)

# Function to add a new student to the MySQL database
def add_student(name, marks):
    conn = connect_to_mysql()
    cursor = conn.cursor()
    if marks >= 75:
        cursor.execute("INSERT INTO students (Name, Marks) VALUES (%s, %s)", (name, marks))
        conn.commit()
        cursor.close()
        conn.close()
        return True
    else:
        cursor.close()
        conn.close()
        return False

# Function to check admission criteria
def check_admission(student_name):
    conn = connect_to_mysql()
    cursor = conn.cursor()
    cursor.execute("SELECT Marks FROM students WHERE Name = %s", (student_name,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    if result:
        marks = result[0]
        if marks >= 75:
            return f"{student_name} is admitted!"
        else:
            return f"{student_name} does not meet admission criteria (marks < 75)."
    else:
        return f"{student_name} is not found in the database."

# Function to filter students by course eligibility
def filter_students_by_course(course):
    conn = connect_to_mysql()
    cursor = conn.cursor()
    if course == "Science":
        cursor.execute("SELECT * FROM students WHERE Marks >= 80")
    elif course == "Economics":
        cursor.execute("SELECT * FROM students WHERE Marks >= 75")
    elif course == "Humanities":
        cursor.execute("SELECT * FROM students WHERE Marks >= 70")
    else:
        cursor.close()
        conn.close()
        return pd.DataFrame(columns=["Name", "Marks"])  # Return empty DataFrame if course is not recognized

    columns = [desc[0] for desc in cursor.description]
    eligible_students = cursor.fetchall()
    cursor.close()
    conn.close()
    return pd.DataFrame(eligible_students, columns=columns)

# Streamlit UI
st.title('Education System')

# Sidebar navigation
page = st.sidebar.radio("Navigation", ('Home', 'Add Student', 'Admission Checker', 'Course Eligibility'))

if page == 'Home':
    st.subheader('Welcome to the Education System!')
    st.write("This platform allows you to manage student data and check admission eligibility.")
    st.write("To get started, you can:")
    st.write("- Click on 'Manage Students' to view student data.")
    st.write("- Click on 'Add Student' to add new students.")
    st.write("- Click on 'Admission Checker' to check admission eligibility.")
    st.write("- Click on 'Course Eligibility' to see which students are eligible for specific courses.")

    # Image or additional information can be added here for a more visually appealing layout

    # Button to manage students
    if st.button("Manage Students"):
        student_df = load_student_data()
        st.write(student_df)  # Display student data

elif page == 'Add Student':
    st.subheader('Add New Student')
    name = st.text_input("Enter student name:")
    marks_str = st.text_input("Enter student marks:")

    try:
        marks = int
