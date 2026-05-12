import streamlit as st
from database import login_user

st.set_page_config(page_title="Login")

st.title("🔐 Login Page")

email = st.text_input("Enter Email")

password = st.text_input("Enter Password", type="password")

if st.button("Login"):

    result = login_user(email, password)

    if result:

        st.success("Login Successful")

        st.switch_page("pages/predict.py")

    else:

        st.error("Wrong Email or Password")