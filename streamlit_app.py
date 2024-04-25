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

# Function to filter students by course eligibility
def filter_students_by_course(student_df, course):
    if course == "Science":
        return student_df[student_df["Marks"] >= 80]
    elif course == "Economics":
        return student_df[student_df["Marks"] >= 75]
    elif course == "Humanities":
        return student_df[student_df["Marks"] >= 70]
    else:
        return pd.DataFrame(columns=["Name", "Marks"])  # Return empty DataFrame if course is not recognized

# Streamlit UI
st.title('Education System')

# Load student data (hidden)
student_df = load_student_data()

# Sidebar navigation
page = st.sidebar.radio("Navigation", ('Home', 'Add Student', 'Admission Checker', 'Course Eligibility'))

if page == 'Home':
    st.subheader('Welcome to the Education System!')
    st.markdown("""
    <p>This platform allows you to manage student data and check admission eligibility.</p>
    <p><strong>To get started, you can:</strong></p>
    <ul>
    <li>Click on <strong>Manage Students</strong> to view student data.</li>
    <li>Click on <strong>Add Student</strong> to add new students.</li>
    <li>Click on <strong>Admission Checker</strong> to check admission eligibility.</li>
    <li>Click on <strong>Course Eligibility</strong> to see which students are eligible for specific courses.</li>
    </ul>
    """, unsafe_allow_html=True)
    
    # Image or additional information can be added here for a more visually appealing layout

    # Button to manage students
    if st.button("Manage Students"):
        st.write(student_df)  # Display student data

elif page == 'Add Student':
    st.subheader('Add New Student')
    name = st.text_input("Enter student name:")
    marks_str = st.text_input("Enter student marks:")

    try:
        marks = int(marks_str)
        if st.button('Add Student'):  # Button click to add student
            student_df = add_student(student_df, name, marks)
            if marks >= 75:
                st.success(f"{name} added successfully!")
            else:
                st.warning(f"Student {name} not added. Marks should be 75 or greater for admission.")
    except ValueError:
        st.error("Please enter a valid integer for marks.")

elif page == 'Admission Checker':
    st.subheader('Admission Checker')
    name = st.text_input("Enter student name to check admission:")

    if st.button('Check Admission'):  # Button click to check admission
        admission_status = check_admission(student_df, name)
        st.write(admission_status)

elif page == 'Course Eligibility':
    st.subheader('Course Eligibility')
    course = st.selectbox("Select a course:", ["Science", "Economics", "Humanities"])

    st.write(f"Students eligible for {course} course:")
    eligible_students = filter_students_by_course(student_df, course)
    st.write(eligible_students)
