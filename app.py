import streamlit as st
import numpy as np
import pickle
import base64
import os

# --- Load Model and Scaler ---
model = pickle.load(open(r"C:\Users\ADMIN\Desktop\Crop Recommendation System Final Project\model.pkl", "rb"))      
scaler = pickle.load(open(r"C:\Users\ADMIN\Desktop\Crop Recommendation System Final Project\minmaxscaler.pkl", "rb"))  

# --- Crop Dictionary with Display Names and Image Paths ---
crop_dict = {
    1: ('Rice', 'static/crops/rice.jpg'),
    2: ('Maize', 'static/crops/maize.jpg'),
    3: ('Jute', 'static/crops/jute.jpg'),
    4: ('Cotton', 'static/crops/cotton.jpg'),
    5: ('Coconut', 'static/crops/coconut.jpg'),
    6: ('Papaya', 'static/crops/papaya.jpg'),
    7: ('Orange', 'static/crops/orange.jpg'),
    8: ('Apple', 'static/crops/apple.jpg'),
    9: ('Muskmelon', 'static/crops/muskmelon.jpg'),
    10: ('Watermelon', 'static/crops/watermelon.jpg'),
    11: ('Grapes', 'static/crops/grapes.jpg'),
    12: ('Mango', 'static/crops/mango.jpg'),
    13: ('Banana', 'static/crops/banana.jpg'),
    14: ('Pomegranate', 'static/crops/pomegranate.jpg'),
    15: ('Lentil', 'static/crops/lentil.jpg'),
    16: ('Blackgram', 'static/crops/blackgram.jpg'),
    17: ('Mungbean', 'static/crops/mungbean.jpg'),
    18: ('Mothbeans', 'static/crops/mothbeans.jpg'),
    19: ('Pigeonpeas', 'static/crops/pigeonpeas.jpg'),
    20: ('Kidneybeans', 'static/crops/kidneybeans.jpg'),
    21: ('Chickpea', 'static/crops/chickpea.jpg'),
    22: ('Coffee', 'static/crops/coffee.jpg'),
}

# --- Background Image CSS ---
def set_bg(image_path):
    with open(image_path, 'rb') as img_file:
        img = img_file.read()
    b64_img = base64.b64encode(img).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpeg;base64,{b64_img}");
            background-size: cover;
            background-attachment: fixed;
        }}
        .glass {{
            background: rgba(255, 255, 255, 0.85);
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 4px 30px rgba(0,0,0,0.2);
        }}
        .title {{
            font-size: 3rem;
            text-align: center;
            color: #2E7D32;
            font-weight: bold;
        }}
        .subtitle {{
            font-size: 1.2rem;
            text-align: center;
            color: #1B5E20;
        }}
        .crop-result {{
            text-align: center;
            background-color: #ffffffcc;
            border-left: 6px solid #4caf50;
            padding: 1rem;
            border-radius: 10px;
        }}
        .crop-result h2 {{
            color: #388e3c;
        }}
        .crop-img {{
            display: flex;
            justify-content: center;
            margin-top: 1rem;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# --- Apply Background ---
set_bg(r"C:\Users\ADMIN\Desktop\Crop Recommendation System Final Project\Image.jpg")  # 🔁 Update path to your background image

# --- Title & Subtitle ---
st.markdown('<div class="title"> 🌱Smart Crop</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI-Powered Recommendation System Based on Soil & Weather Parameters</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
...


col1, col2 = st.columns(2)
with col1:
    N = st.number_input("Nitrogen (N)", 0, 140, 50)
    K = st.number_input("Potassium (K)", 0, 200, 50)
    humidity = st.number_input("Humidity (%)", 0.0, 100.0, 50.0)
    rainfall = st.number_input("Rainfall (mm)", 0.0, 300.0, 100.0)

with col2:
    P = st.number_input("Phosphorous (P)", 0, 140, 50)
    temperature = st.number_input("Temperature (°C)", 0.0, 50.0, 25.0)
    ph = st.number_input("Soil pH", 0.0, 14.0, 6.5)

# --- Prediction Button ---
if st.button("🌱 Recommend Best Crop"):
    features = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    scaled = scaler.transform(features)
    prediction = model.predict(scaled)[0]

    crop_name, crop_img_path = crop_dict.get(prediction, ("Unknown", ""))

    st.markdown(
        f"""
        <div class="crop-result">
            <h4>🌿 Based on your inputs, the best crop to grow is:</h4>
            <h2>{crop_name}</h2>
        </div>
        """, unsafe_allow_html=True
    )

    # Show Crop Image
    if os.path.exists(crop_img_path):
        st.markdown('<div class="crop-img">', unsafe_allow_html=True)
        st.image(crop_img_path, width=300, caption=f"{crop_name}")
        st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
