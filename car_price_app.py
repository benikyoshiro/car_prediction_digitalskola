import streamlit as st
import joblib
import pandas as pd

# Load the trained Random Forest model
model = joblib.load('rf_model.pkl')

# Set Streamlit theme to 'night'
st.markdown(
    """
    <style>
    body {
        background-color: #121212;
        color: #FFFFFF;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Create a Streamlit app
st.title("Prediksi penjualan mobil bekas dengan menggunakan Random Forest")

# Additional text below the header
st.write("aplikasi untuk memprediksi harga mobil bekas berdasarkan beberapa parameter dan nilai dari pasar")

# Input fields
st.subheader("Enter Car Details:")
kms_driven = st.number_input("Kms Driven (jumlah kilometer)")
owner = st.number_input("Owner (jumlah pemilik mobil yg pernah dimiliki)")
present_price = st.number_input("Present Price (harga mobil bekas showroom saat ini)")
age = st.number_input("Age (usia mobil dari tahun beli)")
fuel_type_diesel = st.checkbox("Fuel Type Diesel (jenis bahan bakar mobil)")
fuel_type_petrol = st.checkbox("Fuel Type Petrol (jenis bahan bakar mobil)")
seller_type_individual = st.checkbox("Seller Type Individual (penjual dealer apa individu)")
transmission_manual = st.checkbox("Transmission Manual (Transmisi manual apa otomatis)")

# Predict button
if st.button("Predict"):
    data_new = pd.DataFrame({
        'Kms_Driven': [kms_driven],
        'Owner': [owner],
        'Present_Price': [present_price],
        'Age': [age],
        'Fuel_Type_Diesel': [fuel_type_diesel],
        'Fuel_Type_Petrol': [fuel_type_petrol],
        'Seller_Type_Individual': [seller_type_individual],
        'Transmission_Manual': [transmission_manual]
    })

    # Make a prediction using the loaded model
    result = model.predict(data_new)

    # Display the prediction
    st.subheader("Car Purchase Amount")
    st.write(result[0])

# Display the footer
st.sidebar.text("Kelompok 2:")
st.sidebar.text("- Edwin Purnama")
st.sidebar.text("- Dwi Maulidia")
st.sidebar.text("- Fithranto")
st.sidebar.text("- Hendy")
st.sidebar.text("- Salsabila")

# Run the app with 'streamlit run app.py' in your terminal
