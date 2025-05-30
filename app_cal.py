# import streamlit as st
# # --- PAGE CONFIG ---
# st.set_page_config(
#     page_title="Calorie Burn Estimator", 
#     page_icon="🔥",
#     layout="centered"
# )



# # setting background
# import base64

# def get_base64_of_bin_file(bin_file):
#     with open(bin_file, 'rb') as f:
#         data = f.read()
#     return base64.b64encode(data).decode()

# image_path = "images/background.jpg"  # relative path to your image inside project folder
# img_base64 = get_base64_of_bin_file(image_path)

# page_bg_img = f"""
# <style>
# body {{
#   background-image: url("data:image/jpg;base64,{img_base64}");
#   background-size: cover;
#   background-repeat: no-repeat;
#   background-attachment: fixed;
# }}
# </style>
# """

# st.markdown(page_bg_img, unsafe_allow_html=True)


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

# # --- HEADER ---
# st.title("💪 Calorie Burn Estimator")
# st.markdown("""
#     <style>
#         .big-font { font-size:18px !important; }
#     </style>
#     <p class="big-font">Know how many calories you burn during a workout!</p>
# """, unsafe_allow_html=True)
# st.caption("Built for fitness freaks, gym-goers, and health enthusiasts.")

# # --- INPUT FORM ---
# with st.form("calorie_form"):
#     col1, col2 = st.columns(2)
    
#     with col1:
#         age = st.slider("Age", 15, 79, 25, help="Select your age")
#         height = st.slider("Height (cm)", 120, 240, 175)
#         weight = st.slider("Weight (kg)", 30, 140, 70)
        
#     with col2:
#         duration = st.slider("Workout Duration (min)", 1, 30,10)
#         heart_rate = st.slider("Heart Rate (bpm)", 60, 135, 110)
#         body_temp = st.slider("Body Temp (°C)", 35.0, 45.0, 37.0, step=0.1)
    
#     sex = st.radio("Sex", ["Male", "Female"], horizontal=True)
#     submit = st.form_submit_button("🔥 Calculate Calories", type="primary")

# # --- PREDICTION ---
# if submit:
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
# st.divider()
# st.markdown("Built by Dushyant Singh Hada")
# st.markdown("[📧 Gmail](mailto:u23ch034@ched.svnit.ac.in)")



import streamlit as st
import base64
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

# --- BACKGROUND IMAGE ---
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

image_path = "images/background.jpg"
if os.path.exists(image_path):
    img_base64 = get_base64_of_bin_file(image_path)
    st.markdown(
        f"""
        <style>
        [data-testid="stAppViewContainer"] {{
            background-image: url("data:image/jpg;base64,{img_base64}");
            background-size: cover;
            background-attachment: fixed;
        }}
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
st.markdown("Built by Dushyant Singh Hada  •  [📧 Gmail](mailto:u23ch034@ched.svnit.ac.in)")