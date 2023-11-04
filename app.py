import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load the trained model
model = pickle.load(open('model.sav', 'rb'))

st.title("Customer Churn Prediction App")

# Create input fields for user to enter data
st.header("Enter Customer Information:")
tenure = st.slider("Tenure (Months)", min_value=1, max_value=72, step=1)
monthly_charges = st.number_input("Monthly Charges", min_value=0.0)
total_charges = st.number_input("Total Charges", min_value=0.0)
gender = st.radio("Gender", ["Male", "Female"])
partner = st.radio("Partner", ["Yes", "No"])
dependents = st.radio("Dependents", ["Yes", "No"])
phone_service = st.radio("Phone Service", ["Yes", "No"])
multiple_lines = st.radio("Multiple Lines", ["No", "Yes", "No Phone Service"])
internet_service = st.radio("Internet Service", ["DSL", "Fiber optic", "No"])
online_security = st.radio("Online Security", ["No", "Yes", "No Internet Service"])
online_backup = st.radio("Online Backup", ["No", "Yes", "No Internet Service"])
device_protection = st.radio("Device Protection", ["No", "Yes", "No Internet Service"])
tech_support = st.radio("Tech Support", ["No", "Yes", "No Internet Service"])
streaming_tv = st.radio("Streaming TV", ["No", "Yes", "No Internet Service"])
streaming_movies = st.radio("Streaming Movies", ["No", "Yes", "No Internet Service"])
contract = st.radio("Contract", ["Month-to-month", "One year", "Two year"])
paperless_billing = st.radio("Paperless Billing", ["Yes", "No"])
payment_method = st.radio("Payment Method", ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"])
tenure_group = st.radio("Tenure Group", ["1 - 12", "13 - 24", "25 - 36", "37 - 48", "49 - 60", "61 - 72"])

# Encode categorical variables
gender = 1 if gender == "Female" else 0
partner = 1 if partner == "Yes" else 0
dependents = 1 if dependents == "Yes" else 0
phone_service = 1 if phone_service == "Yes" else 0
multiple_lines = 0 if multiple_lines == "No" else 1 if multiple_lines == "Yes" else 2
internet_service = 0 if internet_service == "No" else 1 if internet_service == "Fiber optic" else 2
online_security = 0 if online_security == "No" else 1 if online_security == "Yes" else 2
online_backup = 0 if online_backup == "No" else 1 if online_backup == "Yes" else 2
device_protection = 0 if device_protection == "No" else 1 if device_protection == "Yes" else 2
tech_support = 0 if tech_support == "No" else 1 if tech_support == "Yes" else 2
streaming_tv = 0 if streaming_tv == "No" else 1 if streaming_tv == "Yes" else 2
streaming_movies = 0 if streaming_movies == "No" else 1 if streaming_movies == "Yes" else 2
contract = 0 if contract == "Month-to-month" else 1 if contract == "One year" else 2
paperless_billing = 1 if paperless_billing == "Yes" else 0
payment_method = 0 if payment_method == "Electronic check" else 1 if payment_method == "Mailed check" else 2 if payment_method == "Bank transfer (automatic)" else 3
tenure_group = 0 if tenure_group == "1 - 12" else 1 if tenure_group == "13 - 24" else 2 if tenure_group == "25 - 36" else 3 if tenure_group == "37 - 48" else 4 if tenure_group == "49 - 60" else 5

# Make predictions
input_data = pd.DataFrame({
    'tenure': [tenure],
    'MonthlyCharges': [monthly_charges],
    'TotalCharges': [total_charges],
    'gender': [gender],
    'Partner': [partner],
    'Dependents': [dependents],
    'PhoneService': [phone_service],
    'MultipleLines': [multiple_lines],
    'InternetService': [internet_service],
    'OnlineSecurity': [online_security],
    'OnlineBackup': [online_backup],
    'DeviceProtection': [device_protection],
    'TechSupport': [tech_support],
    'StreamingTV': [streaming_tv],
    'StreamingMovies': [streaming_movies],
    'Contract': [contract],
    'PaperlessBilling': [paperless_billing],
    'PaymentMethod': [payment_method],
    'tenure_group': [tenure_group]
})

prediction = model.predict(input_data)

st.header("Prediction:")
if prediction[0] == 1:
    st.write("The customer is likely to churn.")
else:
    st.write("The customer is not likely to churn.")
