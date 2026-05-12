import streamlit as st
import sqlite3
import joblib

# DATABASE
conn = sqlite3.connect("users.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    name TEXT,
    email TEXT,
    password TEXT
)
""")

conn.commit()

# MODEL LOAD
model = joblib.load("student_score_model.pkl")

# PAGE CONFIG
st.set_page_config(
    page_title="Student Score Prediction",
    page_icon="🎓",
    layout="centered"
)

# CUSTOM CSS
st.markdown("""
<style>

.stApp{
    background: linear-gradient(135deg,#141e30,#243b55);
}

.title{
    text-align:center;
    font-size:55px;
    color:white;
    font-weight:bold;
}

.subtitle{
    text-align:center;
    color:#dcdcdc;
    margin-bottom:30px;
}

div[data-baseweb="input"]{
    background:white;
    border-radius:10px;
}

.stButton > button{
    width:100%;
    height:50px;
    border:none;
    border-radius:12px;
    background:linear-gradient(to right,#00c6ff,#0072ff);
    color:white;
    font-size:18px;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

# TITLE
st.markdown("<div class='title'>🎓 Student Score Prediction</div>", unsafe_allow_html=True)

st.markdown("<div class='subtitle'>AI Powered Student Performance Predictor</div>", unsafe_allow_html=True)

# MENU
menu = st.sidebar.selectbox(
    "Menu",
    ["Home", "Signup", "Login"]
)

# HOME
if menu == "Home":

    st.write("## Welcome to Student Score Prediction App 🚀")

# SIGNUP
elif menu == "Signup":

    st.subheader("Create Account")

    name = st.text_input("Full Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Signup"):

        cursor.execute(
            "INSERT INTO users VALUES (?, ?, ?)",
            (name, email, password)
        )

        conn.commit()

        st.success("Account Created Successfully")

# LOGIN
elif menu == "Login":

    st.subheader("Login")

    email = st.text_input("Enter Email")
    password = st.text_input("Enter Password", type="password")

    if st.button("Login"):

        cursor.execute(
            "SELECT * FROM users WHERE email=? AND password=?",
            (email, password)
        )

        data = cursor.fetchone()

        if data:

            st.success("Login Successful ✅")

            st.subheader("Predict Student Score")

            hours = st.number_input(
                "Enter Study Hours",
                min_value=0.0
            )

            if st.button("Predict Score"):

                prediction = model.predict([[hours]])

                st.success(
                    f"Predicted Score = {prediction[0]:.2f}"
                )

        else:

            st.error("Wrong Email or Password")