import streamlit as st

from Feature_01 import return_even
from Feature_02 import return_odd

original_list = [i for i in range(10)]

even_list = return_even(original_list)

odd_list = return_odd(original_list)
print("Hello world")
print("again")
st.write("It worked")
st.button("click me")
st.write(even_list)
st.write(odd_list)
st.write("Was luegsch")
st.write("Juhuuu")