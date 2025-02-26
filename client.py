import streamlit as st
import requests
import json

# FastAPI server URL
API_URL = "http://127.0.0.1:8000/predict"

st.title("Flower Prediction App 🌸")
st.write("Enter feature values and get predictions!")

# Input fields
feature_1 = st.number_input("Feature 1", value=0.0)
feature_2 = st.number_input("Feature 2", value=0.0)
feature_3 = st.number_input("Feature 3", value=0.0)
feature_4 = st.number_input("Feature 4", value=0.0)

features = [feature_1, feature_2, feature_3, feature_4]

if st.button("Get Prediction"):
    try:
        payload = json.dumps({"features": features})
        headers = {"Content-Type": "application/json"}
        response = requests.post(API_URL, data=payload, headers=headers)

        # Handle response
        if response.status_code == 200:
            prediction = response.json().get("prediction")
            st.success(f"Prediction: {prediction}")
        else:
            st.error(f"Error: {response.status_code} - {response.text}")
    
    except Exception as e:
        st.error(f"Request failed: {e}")
