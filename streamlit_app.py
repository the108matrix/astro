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
            if add_student(name, marks):
                st.success(f"{name} added successfully!")
            else:
                st.warning(f"Student {name} not added. Marks should be 75 or greater for admission.")
    except ValueError:
        st.error("Please enter a valid integer for marks.")

elif page == 'Admission Checker':
    st.subheader('Admission Checker')
    name = st.text_input("Enter student name to check admission:")

    if st.button('Check Admission'):  # Button click to check admission
        admission_status = check_admission(name)
        st.write(admission_status)

elif page == 'Course Eligibility':
    st.subheader('Course Eligibility')
    course = st.selectbox("Select a course:", ["Science", "Economics", "Humanities"])

    st.write(f"Students eligible for {course} course:")
    eligible_students = filter_students_by_course(course)
    st.write(eligible_students)
