import streamlit as st
import numpy as np
import tensorflow as tf
import joblib
import os

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Calorie Burn Estimator", 
    page_icon="🔥",
    layout="centered"
)


# --- GRADIENT BACKGROUND STYLE ---
st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #f6d365 0%, #fda085 100%);
        background-attachment: fixed;
    }
    [data-testid="stHeader"] {
        background: rgba(255, 255, 255, 0);
    }
    [data-testid="stSidebar"] {
        background: #ffffff33;
    }
    .big-font {
        font-size: 18px !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- MODEL LOADING ---
@st.cache_resource
def load_model():
    return tf.keras.models.load_model('calorie_ann_model.keras', compile=False)

model = load_model()

scaler = None
if os.path.exists("scaler.pkl"):
    try:
        scaler = joblib.load("scaler.pkl")
    except:
        pass

# --- HEADER ---
st.title("💪 Calorie Burn Estimator")
st.markdown('<p class="big-font">Know how many calories you burn during a workout!</p>', unsafe_allow_html=True)
st.caption("Built for fitness freaks, gym-goers, and health enthusiasts.")

# project summary
with st.expander("ℹ️ About this project"):
    st.markdown("""
    This app uses a pre-trained Artificial Neural Network (ANN) model to estimate calorie burn during workouts.
    
    **Features used**:
    - Workout Duration
    - Heart Rate
    - Body Temperature
    - Derived metrics (like HeartRate × Duration)

    🔍 Built using TensorFlow, Streamlit, and deployed on Render.
    """)

# --- INPUT FORM ---
with st.form("calorie_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        age = st.slider("Age", 15, 79, 25, help="Select your age")
        height = st.slider("Height (cm)", 120, 240, 175)
        weight = st.slider("Weight (kg)", 30, 140, 70)
        
    with col2:
        duration = st.slider("Workout Duration (min)", 1, 30, 10)
        heart_rate = st.slider("Heart Rate (bpm)", 60, 135, 110)
        body_temp = st.slider("Body Temp (°C)", 35.0, 45.0, 37.0, step=0.1)
    
    sex = st.radio("Sex", ["Male", "Female"], horizontal=True)
    submit = st.form_submit_button("🔥 Calculate Calories", type="primary")

# --- PREDICTION ---
if submit:
    if not (35.0 <= body_temp <= 45.0):
        st.error("Body temperature must be between 35.0°C and 45.0°C")
    else:
        sex_male = 1 if sex == "Male" else 0
        input_data = np.array([[duration, heart_rate, body_temp, heart_rate * duration]])
        
        if scaler:
            input_data = scaler.transform(input_data)
        
        with st.spinner('Crunching numbers... 🔍'):
            prediction = model.predict(input_data)
        
        st.success(f"✅ Estimated Calories Burned: **{prediction[0][0]:.2f} kcal**")
        st.markdown("💡 _This estimation helps tailor your workouts and diet plans._")

# --- FOOTER ---
st.divider()
st.markdown("""
---
Built with ❤️ by Dushyant Singh Hada  
[GitHub](https://github.com/dushyant-hada-90) • [LinkedIn](https://www.linkedin.com/in/dushyant-hada-7403912b0/) • [Email](mailto:dushyanthada90@gmail.com • [Kaggle](https://www.kaggle.com/u23ch034)
""")

