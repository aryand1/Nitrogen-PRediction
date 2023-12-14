



import streamlit as st
import pandas as pd
import joblib
from PIL import Image

# Load the trained model only once during initialization
best_model = joblib.load('best_model.pkl')

# Define the list of allowed crop types
allowed_crop_types = [
    'rice', 'maize', 'chickpea', 'kidneybeans', 'pigeonpeas', 'mothbeans',
    'mungbean', 'blackgram', 'lentil', 'pomegranate', 'banana', 'mango', 'grapes',
    'watermelon', 'muskmelon', 'apple', 'orange', 'papaya', 'coconut', 'cotton',
    'jute', 'coffee'
]

# Streamlit app title
st.markdown("<h1 style='text-align: center; color: white;'>Nitrogen Prediction</h1>", unsafe_allow_html=True)


# Display an image from a given path
image_path = "C:/Users/aryand/Downloads/_f29f03f3-a960-4769-8c6e-b3853e1cfb11.jpeg" # Change this to your image file path
image = Image.open(image_path)
st.image(image, caption='Nutrition prediction', use_column_width=True)

# Create input boxes for user data
ph_value = st.number_input("pH:")
rainfall_value = st.number_input("Rainfall (mm):")
temperature_value = st.number_input("Temperature (°C):")
humidity_value = st.number_input("Humidity (%):")
phosphorus_value = st.number_input("Phosphorus (mg/kg):")
potassium_value = st.number_input("Potassium (mg/kg):")

# Add a red warning message for Crop Type
st.markdown("<font color='red'>Select one Crop Type</font>", unsafe_allow_html=True)

# Create checkboxes for Crop Type selection
selected_crop_type = st.selectbox("Crop Type:", allowed_crop_types)

# Create a button to predict Nitrogen
if st.button("Predict Nitrogen"):
    # Create a pandas DataFrame with the input data
    user_data = pd.DataFrame([[ph_value, rainfall_value, temperature_value, humidity_value, phosphorus_value, potassium_value, selected_crop_type]],
                             columns=['ph', 'rainfall', 'temperature', 'humidity', 'phosphorus', 'potassium', 'label'])

    # Perform predictions using the best model
    user_predictions = best_model.predict(user_data)

    # Display the predicted Nitrogen value
    st.write("Predicted Nitrogen Value: {:.2f}".format(user_predictions[0]))

