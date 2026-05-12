import streamlit as st

st.set_page_config(
    page_title="Student Score Prediction",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# HIDE SIDEBAR + CUSTOM UI
st.markdown("""
<style>

/* Hide Sidebar */
[data-testid="stSidebar"] {
    display: none;
}

/* Main Background */
.stApp {
    background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
    overflow: hidden;
}

/* Title */
.title {
    text-align: center;
    font-size: 70px;
    font-weight: bold;
    color: white;
    margin-top: 50px;
    animation: glow 2s infinite alternate;
}

/* Subtitle */
.subtitle {
    text-align: center;
    color: #cfcfcf;
    font-size: 25px;
    margin-bottom: 50px;
}

/* Glass Card */
.glass {
    width: 60%;
    margin: auto;
    padding: 50px;
    border-radius: 25px;
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(15px);
    box-shadow: 0px 0px 40px rgba(0,0,0,0.5);
    animation: fade 1.5s ease;
}

/* Buttons */
.stButton > button {
    width: 100%;
    height: 60px;
    border-radius: 15px;
    border: none;
    font-size: 22px;
    font-weight: bold;
    color: white;
    background: linear-gradient(to right, #00c6ff, #0072ff);
    transition: 0.3s;
}

/* Button Hover */
.stButton > button:hover {
    transform: scale(1.05);
    box-shadow: 0px 0px 20px #00c6ff;
}

/* Glow Animation */
@keyframes glow {
    from {
        text-shadow: 0px 0px 15px #00c6ff;
    }

    to {
        text-shadow: 0px 0px 35px #0072ff;
    }
}

/* Fade Animation */
@keyframes fade {
    from {
        opacity: 0;
        transform: translateY(40px);
    }

    to {
        opacity: 1;
        transform: translateY(0px);
    }
}

</style>
""", unsafe_allow_html=True)

# TITLE
st.markdown("""
<div class="title">
🎓 Student Score Prediction
</div>
""", unsafe_allow_html=True)

# SUBTITLE
st.markdown("""
<div class="subtitle">
AI Powered Student Performance Predictor
</div>
""", unsafe_allow_html=True)

# CARD START
st.markdown('<div class="glass">', unsafe_allow_html=True)

st.write("")

col1, col2, col3 = st.columns([1,1,1])

with col2:

    c1, c2 = st.columns(2)

    with c1:
        if st.button("🔐 Login"):
            st.switch_page("pages/login.py")

    with c2:
        if st.button("📝 Signup"):
            st.switch_page("pages/signup.py")

st.markdown("</div>", unsafe_allow_html=True)