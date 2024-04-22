import streamlit as st

def display_homepage():
  st.title("Welcome to the Education System!")
  st.write("This platform allows you to manage student data and check admission eligibility.")
  
  # Button with HTML and CSS for styling (replace "#" with your actual path)
  button_html = """
  <button class="custom-btn">Manage Students</button>
  <style>
  .custom-btn {
    background-color: #4CAF50; /* Green */
    border: none;
    color: white;
    padding: 15px 32px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    margin: 4px 2px;
    cursor: pointer;
  }
  </style>
  """
  st.write(button_html, unsafe_allow_html=True)

if __name__ == "__main__":
  display_homepage()
