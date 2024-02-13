import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import smtplib


st.title('Welcome to the _**SHS Computer Science Site**_!')
st.header('This brand new site, coded in Python with hosting/library provided by _Streamlit.io_, is for all things Computer Science within Sahuarita High School, this website will provide resources for things such as the CS TSA Test.')

st.divider()

suggestions = st.text_input('Have any suggestions? Feedback such as bugs or even suggestions can help make the site better!')

if suggestions != "":

  # creates SMTP session
  s = smtplib.SMTP('smtp.gmail.com', 587)
  # start TLS for security
  s.starttls()
  # Authentication
  s.login("sender_email_id", "sender_email_id_password")
  # message to be sent
  message = "Message_you_need_to_send"
  # sending the mail
  s.sendmail("sender_email_id", "receiver_email_id", message)
  # terminating the session
  s.quit()