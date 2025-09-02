# Fraud-Detection-LR-Rf-Xgboost
# 🚨 Fraud Detection Prediction App  

This project implements a **Fraud Detection System** using **Logistic Regression, Random Forest, and XGBoost**.  
It provides a **Streamlit web app** for predicting fraudulent transactions and comparing model performance.  

---
##  Dataset

The dataset used for this project is the [Kaggle “Credit Card Fraud Detection” dataset](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud) (publicly available).  
Place the dataset in the folder named `dataset/` and ensure the filename is preserved.


---

## 📂 Project Structure  

FRAUD_DETECTION_LR_RF_Xgboost/
│── app.py # Streamlit app for fraud detection
│── analysis_model.ipynb # Model training, evaluation & comparison
│── dataset/ # Folder holding the dataset CSV
│ └── creditcard.csv
│── logreg_pipeline.pkl # Logistic Regression trained pipeline
│── rf_pipeline.pkl # Random Forest trained pipeline
│── xgb_pipeline.pkl # XGBoost trained pipeline
│── logreg_metrics.json # Metrics for Logistic Regression
│── rf_metrics.json # Metrics for Random Forest
│── xgb_metrics.json # Metrics for XGBoost
│── requirements.txt # Required dependencies
│── README.md # Project documentation

---

## Dataset

The dataset is based on financial transaction records with the following fields:

type → Transaction type (PAYMENT, TRANSFER, CASH_OUT, DEPOSIT)

amount → Transaction amount

oldbalanceOrg → Sender’s balance before transaction

newbalanceOrig → Sender’s balance after transaction

oldbalanceDest → Receiver’s balance before transaction

newbalanceDest → Receiver’s balance after transaction

isFraud → Target variable (1 = Fraud, 0 = Legit)

Sample entries:

| step | type      | amount  | oldbalanceOrg | newbalanceOrig | oldbalanceDest | newbalanceDest | isFraud |
|------|-----------|---------|---------------|----------------|----------------|----------------|---------|
| 1    | PAYMENT   | 9839.64 | 170136.0      | 160296.36      | 0.0            | 0.0            | 0       |
| 1    | TRANSFER  | 181.00  | 181.0         | 0.00           | 0.0            | 0.0            | 1       |
| 1    | CASH_OUT  | 181.00  | 181.0         | 0.00           | 21182.0        | 0.0            | 1       |





---

## ⚙️ Installation  

Clone the repository and install dependencies:  

```bash
git clone https://github.com/your-username/FRAUD_DETECTION_LR_RF_Xgboost.git
cd FRAUD_DETECTION_LR_RF_Xgboost
pip install -r requirements.txt
load dataset from kaggle

streamlit run app.py

---



## 🖥️ Features

✅ Choose between Logistic Regression, Random Forest, or XGBoost
✅ Input transaction details (type, amount, balances, etc.)
✅ Predict whether a transaction is fraudulent or legitimate
✅ View model-specific performance metrics (precision, recall, F1-score, etc.)
✅ Interactive & user-friendly interface with Streamlit

---


##  Model Performance Comparison

Below are the classification reports and performance metrics for each model. Metrics are based on the test dataset used.

Logistic Regression

              precision    recall  f1-score   support

           0       1.00      0.95      0.97   1,906,322
           1       0.02      0.94      0.04     2,464

    accuracy                           0.95   1,908,786
   macro avg       0.51      0.94      0.51   1,908,786
weighted avg       1.00      0.95      0.97   1,908,786

Confusion Matrix:
 [[1804823  101499]
 [    151    2313]]
ROC-AUC: 0.9891  
PR-AUC: 0.5452


Random Forest
              precision    recall  f1-score   support

           0       1.00      1.00      1.00   1,906,322
           1       0.96      0.78      0.86     2,464

    accuracy                           1.00   1,908,786
   macro avg       0.98      0.89      0.93   1,908,786
weighted avg       1.00      1.00      1.00   1,908,786

Confusion Matrix:
 [[1906252      70]
 [    548    1916]]
ROC-AUC: 0.9948  
PR-AUC: 0.9402


XGBoost

              precision    recall  f1-score   support

           0       1.00      1.00      1.00   1,906,322
           1       0.40      0.99      0.57     2,464

    accuracy                           1.00   1,908,786
   macro avg       0.70      0.99      0.78   1,908,786
weighted avg       1.00      1.00      1.00   1,908,786

Confusion Matrix:
 [[1902655    3667]
 [     34    2430]]
ROC-AUC: 0.9995  
PR-AUC: 0.9379
