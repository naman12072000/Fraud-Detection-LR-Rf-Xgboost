import streamlit as st
import pandas as pd
import joblib
import json

# Load models
models = {
    "Logistic Regression": joblib.load("logreg_pipeline.pkl"),
    "Random Forest": joblib.load("rf_pipeline.pkl"),
    "XGBoost": joblib.load("xgb_pipeline.pkl")
}

# Load metrics
metrics = {}
for name, file in zip(
    ["Logistic Regression", "Random Forest", "XGBoost"],
    ["logreg_metrics.json", "rf_metrics.json", "xgb_metrics.json"]
):
    with open(file, "r") as f:
        metrics[name] = json.load(f)

# Streamlit UI
st.title("Fraud Detection Prediction App")

model_choice = st.selectbox("Choose Model", list(models.keys()))

st.markdown("Please enter the transaction details:")

transaction_type = st.selectbox("Transaction Type", ["PAYMENT", "TRANSFER", "CASH_OUT", "DEPOSIT"])
amount = st.number_input("Amount", min_value=0.0, value=1000.0)
oldbalanceOrg = st.number_input("Old Balance (Sender)", min_value=0.0, value=10000.0)
newbalanceOrig = st.number_input("New Balance (Sender)", min_value=0.0, value=9000.0)
oldbalanceDest = st.number_input("Old Balance (Receiver)", min_value=0.0, value=0.0)
newbalanceDest = st.number_input("New Balance (Receiver)", min_value=0.0, value=0.0)

if st.button("Predict"):
    input_data = pd.DataFrame([{
        "type": transaction_type,
        "amount": amount,
        "oldbalanceOrg": oldbalanceOrg,
        "newbalanceOrig": newbalanceOrig,
        "oldbalanceDest": oldbalanceDest,
        "newbalanceDest": newbalanceDest
    }])
    
    model = models[model_choice]
    prediction = model.predict(input_data)[0]

    st.subheader(f"Prediction: {int(prediction)}")
    if prediction == 1:
        st.error("🚨 This transaction may be fraudulent!")
    else:
        st.success("✅ This transaction looks legitimate.")

    st.divider()
    st.subheader(f"📊 Model Performance ({model_choice})")
    st.json(metrics[model_choice])
