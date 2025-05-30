



# import streamlit as st
# import numpy as np
# import tensorflow as tf
# import joblib

# # Load trained model
# model = tf.keras.models.load_model('calorie_ann_model.keras', compile=False)  # compile=False to avoid custom loss issues

# # Load scaler if used
# # scaler = joblib.load("scaler.pkl")

# st.set_page_config(page_title="Calorie Burn Estimator", page_icon="💪")
# st.title("🏋️‍♂️ Calorie Burn Estimator")
# st.markdown("**Know how many calories you burn during a workout!**\n"
#             "_Built for fitness freaks, gym-goers, and health enthusiasts._")

# # Input fields
# age = st.number_input("Age", min_value=10, max_value=100)
# height = st.number_input("Height (in cm)", min_value=100, max_value=250)
# weight = st.number_input("Weight (in kg)", min_value=30, max_value=200)
# duration = st.number_input("Workout Duration (in minutes)", min_value=1, max_value=300)
# heart_rate = st.number_input("Average Heart Rate (bpm)", min_value=30, max_value=220)
# body_temp = st.number_input("Body Temperature (°C)", min_value=35.0, max_value=45.0)
# sex = st.selectbox("Sex", ["Male", "Female"])

# # Encode sex
# sex_male = 1 if sex == "Male" else 0

# # Predict button
# if st.button("🔥 Predict Calories Burned"):
#     input_data = np.array([[  duration, heart_rate, body_temp,heart_rate*duration]])

#     # If you used a scaler
#     # input_data = scaler.transform(input_data)

#     with st.spinner('Crunching numbers... 🔍'):
#         prediction = model.predict(input_data)

#     st.success(f"✅ Estimated Calories Burned: **{prediction[0][0]:.2f} kcal**")
#     st.markdown("💡 _This estimation helps tailor your workouts and diet plans._")

# st.markdown("---")
# st.markdown("Built with ❤️ by Dushyant Singh Hada")
# st.markdown("[📧 Contact](mailto:u23ch034@ched.svnit.ac.in)")


import streamlit as st
import numpy as np
import tensorflow as tf
import joblib

# --- MODEL LOADING ---
# Load the pre-trained ANN model (compile=False avoids custom loss function issues)
model = tf.keras.models.load_model('calorie_ann_model.keras', compile=False)

# Optional: Load a scaler if you used feature scaling during training
# scaler = joblib.load("scaler.pkl")

# --- PAGE CONFIG ---
st.set_page_config(page_title="Calorie Burn Estimator", page_icon="💪")
st.title("🏋️‍♂️ Calorie Burn Estimator")
st.markdown("**Know how many calories you burn during a workout!**\n"
            "_Built for fitness freaks, gym-goers, and health enthusiasts._")

# --- INPUT FORM ---
# Wrap inputs in a form to prevent refreshes until submission
with st.form("calorie_form"):
    # User Input Fields
    age = st.number_input("Age", min_value=10, max_value=100)
    height = st.number_input("Height (in cm)", min_value=100, max_value=250)
    weight = st.number_input("Weight (in kg)", min_value=30, max_value=200)
    duration = st.number_input("Workout Duration (in minutes)", min_value=1, max_value=300)
    heart_rate = st.number_input("Average Heart Rate (bpm)", min_value=30, max_value=220)
    body_temp = st.number_input("Body Temperature (°C)", min_value=35.0, max_value=45.0)
    sex = st.selectbox("Sex", ["Male", "Female"])
    
    # Form submission button (triggers prediction only when clicked)
    submitted = st.form_submit_button("🔥 Predict Calories Burned")

# --- PREDICTION LOGIC ---
if submitted:
    # Encode sex (1 for Male, 0 for Female)
    sex_male = 1 if sex == "Male" else 0
    
    # Prepare input array for the model
    input_data = np.array([[duration, heart_rate, body_temp, heart_rate * duration]])
    
    # Optional: Scale features if a scaler was used during training
    # input_data = scaler.transform(input_data)
    
    # Show spinner while predicting
    with st.spinner('Crunching numbers... 🔍'):
        prediction = model.predict(input_data)
    
    # Display results
    st.success(f"✅ Estimated Calories Burned: **{prediction[0][0]:.2f} kcal**")
    st.markdown("💡 _This estimation helps tailor your workouts and diet plans._")

# --- FOOTER ---
st.markdown("---")
st.markdown("Built with ❤️ by Dushyant Singh Hada")
st.markdown("[📧 Contact](mailto:u23ch034@ched.svnit.ac.in)")