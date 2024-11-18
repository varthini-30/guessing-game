import streamlit as st
import random
st.title("Welcome to guessing game")
lower_num=0
higher_num=100
num=random.randint(lower_num,higher_num)
st.title("game starts now,are you ready ton play")
st.write(f"guess a number between (lower_num)and(higher_num)")
guessing_num=st.number_input("Enter a number from 0 to 100")
if st.button("check"):
    if guessing_num<num:
        st.write("your guess is too low")
    if guessing_num>num:
        st.write("your guess is too high")
    elif guessing_num==num:
        st.write("Congratulation")
    else:
        st.write("True")