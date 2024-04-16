import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import smtplib

"""
TSA Study Guide
"""
import random

def split_file_by_bracket(file_path):

    with open(file_path, 'r') as file:

        file_contents = file.read()

        result_list = file_contents.split('[')
        
        result_list = [item.strip() for item in result_list if item.strip()]
                                          
        return result_list

def split_file_by_bracket2(file_path):

    with open(file_path, 'r') as file:

        file_contents = file.read()
        
        answer_list = file_contents.split('@')
        
        answer_list = [item.strip() for item in answer_list if item.strip()]
                                          
        return answer_list


file_path = 'studyguide.txt'
result = split_file_by_bracket(file_path)
answer = split_file_by_bracket2(file_path)

counter = 0

score = 0

order = []

for i in range(135):
    order.append(i)

random.shuffle(order)
st.text(order)

for i in range(len(result)):
    
    st.text(str(result[order[i]])[3:len(result[order[i]])])
    answer[i] = str(answer[order[i]])[len(answer[order[i]])-1:len(answer[order[i]])]
    
    #st.text(answer[i])
    
    user = st.text_input("Your Answer: ")
    
    
    if user == answer[i]:
        st.text("Correct!")
        score += 1
    else:
        st.text("Wrong!")
    
    st.text()
    st.text()
    st.text()
    
    counter += 1
    if counter == 135:
        st.text()
        st.text()
        st.text()
        st.text()
        st.text("You reached the end of this Practice Test, your score was: " + str(score) + " out of 135 questions correct.")
        break