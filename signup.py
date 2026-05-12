import streamlit as st
from database import add_user

st.set_page_config(page_title="Signup")

st.title("📝 Signup Page")

name = st.text_input("Full Name")

email = st.text_input("Email")

password = st.text_input("Password", type="password")

if st.button("Create Account"):

    add_user(name, email, password)

    st.success("Account Created Successfully")