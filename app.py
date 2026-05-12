import streamlit as st
import sqlite3
import joblib
import pandas as pd

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
model = joblib.load("student_model.pkl")
columns = joblib.load("model_columns.pkl")

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
st.markdown(
    "<div class='title'>🎓 Student Score Prediction</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>AI Powered Student Performance Predictor</div>",
    unsafe_allow_html=True
)

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

        st.success("Account Created Successfully ✅")

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

            st.subheader("📊 Enter Student Details")

            hours_studied = st.number_input(
                "Hours Studied",
                0.0,
                24.0
            )

            attendance = st.number_input(
                "Attendance %",
                0.0,
                100.0
            )

            previous_scores = st.number_input(
                "Previous Scores",
                0.0,
                100.0
            )

            sleep_hours = st.number_input(
                "Sleep Hours",
                0.0,
                24.0
            )

            motivation_level = st.selectbox(
                "Motivation Level",
                ["Low", "Medium", "High"]
            )

            teacher_quality = st.selectbox(
                "Teacher Quality",
                ["Poor", "Average", "Good"]
            )

            school_type = st.selectbox(
                "School Type",
                ["Public", "Private"]
            )

            internet_access = st.selectbox(
                "Internet Access",
                ["Yes", "No"]
            )

            family_income = st.selectbox(
                "Family Income",
                ["Low", "Medium", "High"]
            )

            parental_involvement = st.selectbox(
                "Parental Involvement",
                ["Low", "Medium", "High"]
            )

            parental_education = st.selectbox(
                "Parental Education",
                ["School", "College"]
            )

            peer_influence = st.selectbox(
                "Peer Influence",
                ["Negative", "Neutral", "Positive"]
            )

            learning_resources = st.selectbox(
                "Learning Resources",
                ["Low", "Medium", "High"]
            )

            activities = st.selectbox(
                "Extracurricular Activities",
                ["Yes", "No"]
            )

            if st.button("Predict Exam Score"):

                input_data = {
                    "Hours_Studied": hours_studied,
                    "Attendance": attendance,
                    "Previous_Scores": previous_scores,
                    "Sleep_Hours": sleep_hours,
                    "Motivation_Level": motivation_level,
                    "Teacher_Quality": teacher_quality,
                    "School_Type": school_type,
                    "Internet_Access": internet_access,
                    "Family_Income": family_income,
                    "Parental_Involvement": parental_involvement,
                    "Parental_Education_Level": parental_education,
                    "Peer_Influence": peer_influence,
                    "Learning_Resources": learning_resources,
                    "Extracurricular_Activities": activities
                }

                input_df = pd.DataFrame([input_data])

                input_df = pd.get_dummies(input_df)

                input_df = input_df.reindex(
                    columns=columns,
                    fill_value=0
                )

                prediction = model.predict(input_df)

                st.success(
                    f"🎯 Predicted Exam Score: {round(prediction[0], 2)}"
                )

        else:

            st.error("Wrong Email or Password ❌")