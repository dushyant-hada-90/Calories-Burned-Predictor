# import streamlit as st
# import numpy as np
# import tensorflow as tf
# import joblib  # if you're using a scaler like StandardScaler

# # Load trained model
# model = tf.keras.models.load_model('calorie_ann_model.keras',custom_objects={"rmlse":rmlse})  # replace with your actual model path

# # Load scaler if used during training
# # scaler = joblib.load("scaler.pkl")  # Uncomment if using scaler

# st.title("Calorie Burn Prediction App")

# st.markdown("Enter your details below to predict the calories burned.")

# # Input fields
# age = st.number_input("Age", min_value=10, max_value=100, step=1)
# height = st.number_input("Height (in cm)", min_value=100, max_value=250)
# weight = st.number_input("Weight (in kg)", min_value=30, max_value=200)
# duration = st.number_input("Exercise Duration (in minutes)", min_value=1, max_value=300)
# heart_rate = st.number_input("Heart Rate (bpm)", min_value=30, max_value=220)
# body_temp = st.number_input("Body Temperature (°C)", min_value=35.0, max_value=45.0)
# sex = st.selectbox("Sex", options=["Male", "Female"])

# # Encode Sex
# sex_male = 1 if sex == "Male" else 0

# # Button to make prediction
# if st.button("Predict Calories Burned"):
#     input_data = np.array([[  duration, heart_rate, body_temp,heart_rate*duration]])
    
#     # Optional: scale input data if you used a scaler during training
#     # input_data = scaler.transform(input_data)
    
#     prediction = model.predict(input_data)
#     st.success(f"Estimated Calories Burned: {prediction[0][0]:.2f} kcal")




import streamlit as st
import numpy as np
import tensorflow as tf
import joblib

# Load trained model
model = tf.keras.models.load_model('calorie_ann_model.keras', compile=False)  # compile=False to avoid custom loss issues

# Load scaler if used
# scaler = joblib.load("scaler.pkl")

st.set_page_config(page_title="Calorie Burn Estimator", page_icon="💪")
st.title("🏋️‍♂️ Calorie Burn Estimator")
st.markdown("**Know how many calories you burn during a workout!**\n"
            "_Built for fitness freaks, gym-goers, and health enthusiasts._")

# Input fields
age = st.number_input("Age", min_value=10, max_value=100)
height = st.number_input("Height (in cm)", min_value=100, max_value=250)
weight = st.number_input("Weight (in kg)", min_value=30, max_value=200)
duration = st.number_input("Workout Duration (in minutes)", min_value=1, max_value=300)
heart_rate = st.number_input("Average Heart Rate (bpm)", min_value=30, max_value=220)
body_temp = st.number_input("Body Temperature (°C)", min_value=35.0, max_value=45.0)
sex = st.selectbox("Sex", ["Male", "Female"])

# Encode sex
sex_male = 1 if sex == "Male" else 0

# Predict button
if st.button("🔥 Predict Calories Burned"):
    input_data = np.array([[  duration, heart_rate, body_temp,heart_rate*duration]])

    # If you used a scaler
    # input_data = scaler.transform(input_data)

    with st.spinner('Crunching numbers... 🔍'):
        prediction = model.predict(input_data)

    st.success(f"✅ Estimated Calories Burned: **{prediction[0][0]:.2f} kcal**")
    st.markdown("💡 _This estimation helps tailor your workouts and diet plans._")

