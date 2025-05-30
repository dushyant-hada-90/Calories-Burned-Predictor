# import streamlit as st
# import numpy as np
# import tensorflow as tf
# import joblib

# # --- MODEL LOADING ---
# # Load the pre-trained ANN model (compile=False avoids custom loss function issues)
# # model = tf.keras.models.load_model('calorie_ann_model.keras', compile=False)
# @st.cache_resource
# def load_model():
#     return tf.keras.models.load_model('calorie_ann_model.keras', compile=False)


# model = load_model()

# # Optional: Load a scaler if you used feature scaling during training
# # scaler = joblib.load("scaler.pkl")
# @st.cache_resource
# def load_scaler():
#     return joblib.load("scaler.pkl")

# scaler = load_scaler()


# # --- PAGE CONFIG ---
# st.set_page_config(page_title="Calorie Burn Estimator", page_icon="💪")
# st.title("🏋️‍♂️ Calorie Burn Estimator")
# st.markdown("**Know how many calories you burn during a workout!**\n"
#             "_Built for fitness freaks, gym-goers, and health enthusiasts._")

# # --- INPUT FORM ---
# # Wrap inputs in a form to prevent refreshes until submission
# with st.form("calorie_form"):
#     # User Input Fields
#     age = st.number_input("Age", min_value=10, max_value=100)
#     height = st.number_input("Height (in cm)", min_value=100, max_value=250)
#     weight = st.number_input("Weight (in kg)", min_value=30, max_value=200)
#     duration = st.number_input("Workout Duration (in minutes)", min_value=1, max_value=300)
#     heart_rate = st.number_input("Average Heart Rate (bpm)", min_value=30, max_value=220)
#     body_temp = st.number_input("Body Temperature (°C)", min_value=35.0, max_value=45.0)
#     sex = st.selectbox("Sex", ["Male", "Female"])
    
#     # Form submission button (triggers prediction only when clicked)
#     submitted = st.form_submit_button("🔥 Predict Calories Burned")

# # --- PREDICTION LOGIC ---
# if submitted:
#     # Encode sex (1 for Male, 0 for Female)
#     sex_male = 1 if sex == "Male" else 0
    
#     # Prepare input array for the model
#     input_data = np.array([[duration, heart_rate, body_temp, heart_rate * duration]])
    
#     # Optional: Scale features if a scaler was used during training
#     input_data = scaler.transform(input_data)
    
#     # Show spinner while predicting
#     with st.spinner('Crunching numbers... 🔍'):
#         prediction = model.predict(input_data)
    
#     # Display results
#     st.success(f"✅ Estimated Calories Burned: **{prediction[0][0]:.2f} kcal**")
#     st.markdown("💡 _This estimation helps tailor your workouts and diet plans._")

# # --- FOOTER ---
# st.markdown("---")
# st.markdown("Built by Dushyant Singh Hada")
# st.markdown("""
# <a href="mailto:u23ch034@ched.svnit.ac.in">
#     <img src="https://www.gstatic.com/images/icons/material/system/1x/mail_black_24dp.png" width="18" style="vertical-align:middle">
#     <span style="vertical-align:middle">Gmail</span>
# </a>
# """, unsafe_allow_html=True)


import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Calorie Burn Estimator", 
    page_icon="🔥",
    layout="centered"
)

# --- HEADER ---
st.title("💪 Calorie Burn Estimator")
st.markdown("""
    <style>
        .big-font { font-size:18px !important; }
    </style>
    <p class="big-font">Know how many calories you burn during a workout!</p>
""", unsafe_allow_html=True)
st.caption("Built for fitness freaks, gym-goers, and health enthusiasts.")

# --- INPUT FORM ---
with st.form("calorie_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        age = st.slider("Age", 10, 100, 25, help="Select your age")
        height = st.slider("Height (cm)", 100, 250, 175)
        weight = st.slider("Weight (kg)", 30, 200, 70)
        
    with col2:
        duration = st.slider("Workout Duration (min)", 1, 300, 30)
        heart_rate = st.slider("Heart Rate (bpm)", 30, 220, 120)
        body_temp = st.slider("Body Temp (°C)", 35.0, 45.0, 37.0, step=0.1)
    
    sex = st.radio("Sex", ["Male", "Female"], horizontal=True)
    submit = st.form_submit_button("🔥 Calculate Calories", type="primary")

# --- PREDICTION ---
if submit:
    with st.spinner("Calculating..."):
        # Your prediction code here
        st.success(f"Estimated burn: **350 kcal**")  # Example output

# --- FOOTER ---
st.divider()
st.markdown("---")
st.markdown("Built by Dushyant Singh Hada")
st.markdown("""
<a href="mailto:u23ch034@ched.svnit.ac.in">
    <img src="https://www.gstatic.com/images/icons/material/system/1x/mail_black_24dp.png" width="18" style="vertical-align:middle">
    <span style="vertical-align:middle">Gmail</span>
</a>
""", unsafe_allow_html=True)