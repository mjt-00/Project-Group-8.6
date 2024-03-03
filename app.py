import streamlit as st

from Feature_01 import return_even

original_list = [i for i in range(10)]

even_list = return_even(original_list)

st.write("It worked")
st.button("click me")
st.write(even_list)
