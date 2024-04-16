import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import smtplib

"""
Number Conversion Practice
"""
import random


st.write("Welcome to the NUMBER CONVERSION PRACTICE PROGRAM.")
st.write("To get started, input what you like to practice below.")
st.write()


numbersystem = ["binary", "hexadecimal", "decimal", "octal"]

selecting = True

while selecting:
    first = st.text_input("What Number System you'd like to convert? ", key=1)
    
    second = st.text_input("What would you like to convert it to? ", key=2)
    
    if first == "binary" or first == "hexadecimal" or first == "decimal" or first == "octal" or second == "binary" or second == "hexadecimal" or second == "decimal" or second == "octal":
        st.write()
        st.write()
        st.write()
        st.write("Okay, let's practice converting", first, "to", second + ".")
        st.write("Press 'Run' above if you want to reset the program and pick another number conversion")
        running = True
        break
        
    else:
        st.write("Not a valid st.text_input. Try again.")
        continue

a = []




while running:
    for i in range(999):
        a.append(i)
    random.shuffle(a)
    number = a[0]
    

    
    if first == "binary":
        number = (str(bin(number))[2:])
        st.write("Convert", number, "to", second + ".")
        st.write()
        st.write()
        response = int(st.text_input("Answer: "),key=3)
        
        
        
        if second == "octal":
            answer = (str(oct(a[0]))[1:])
        if second == "hexadecimal":
            answer = (str(hex(a[0]))[2:])
        if second == "decimal":
            answer = a[0]
        if second == "binary":
            answer = (str(bin(a[0]))[2:])
    
              

    if first == "decimal":
        number = str(number)
        st.write("Convert", number, "to", second + ".")
        st.write()
        st.write()
        response = int(st.text_input("Answer: "),key=4)
        
        
        
        if second == "octal":
            answer = (str(oct(a[0]))[1:])
        if second == "hexadecimal":
            answer = (str(hex(a[0]))[2:])
        if second == "decimal":
            answer = a[0]
        if second == "binary":
            answer = (str(bin(a[0]))[2:])
    
    
    
    if first == "hexadecimal":
        number = (str(hex(number))[2:])
        st.write("Convert", number, "to", second + ".")
        st.write()
        st.write()
        response = int(st.text_input("Answer: "),key=5)
        
        
        
        if second == "octal":
            answer = (str(oct(a[0]))[1:])
        if second == "hexadecimal":
            answer = (str(hex(a[0]))[2:])
        if second == "decimal":
            answer = a[0]
        if second == "binary":
            answer = (str(bin(a[0]))[2:])
    

    
    if first == "octal":
        number = (str(oct(number))[1:])
        st.write("Convert", number, "to", second + ".")
        st.write()
        st.write()
        response = int(st.text_input("Answer: "),key=6)
        
        
        
        if second == "octal":
            answer = (str(oct(a[0]))[1:])
        if second == "hexadecimal":
            answer = (str(hex(a[0]))[2:])
        if second == "decimal":
            answer = a[0]
        if second == "binary":
            answer = (str(bin(a[0]))[2:])


  
    if response == int(answer):
        st.write("Correct!")
        st.write()
        st.write()
    else:
        st.write("Wrong!")
        st.write()
        st.write()