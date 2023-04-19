import streamlit as st
import pandas as pd

st.header("""
Max of three numbers """)

st.subheader('User inputs')

def user_input_features():
  num1 = st.number_input("Enter the first number", min_value = -999999999, max_value = 999999999, step = 1)
  num2 = st.number_input("Enter the second number", min_value = -999999999, max_value = 999999999, step = 1)
  num3 = st.number_input("Enter the third number", min_value = -999999999, max_value = 999999999, step = 1)

  numbers = [num1, num2, num3]
  return numbers
numbers = user_input_features()
res = max(numbers)

if st.button('Find Largest Number'):
    st.write("Result : Largest number is ")
    st.write(res)
