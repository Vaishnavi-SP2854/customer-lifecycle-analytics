import streamlit as st
import pandas as pd
import numpy as np
import joblib


import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_PATH = os.path.join(
    BASE_DIR, "data", "processed", "customer_lifecycle_final.csv"
)

MODEL_PATH = os.path.join(
    BASE_DIR, "models", "churn_model.pkl"
)

df = pd.read_csv(DATA_PATH)
model = joblib.load(MODEL_PATH)


# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Customer Lifecycle Analytics Dashboard",
    layout="wide"
)

st.title("📊 Customer Lifecycle Analytics Dashboard")
st.markdown("Analyze churn risk, customer value, and retention priorities")
st.write(DATA_PATH)



# -----------------------------
# Load Data & Model
# -----------------------------
@st.cache_data
def load_data():
    return pd.read_csv("../data/processed/customer_lifecycle_final.csv")

@st.cache_resource
def load_model():
    return joblib.load("../models/churn_model.pkl")

df = load_data()
model = load_model()

st.write("📂 Data path being used:")
st.code(DATA_PATH)

df = pd.read_csv("../data/processed/customer_lifecycle_final.csv")


# -----------------------------
# KPI Section
# -----------------------------
st.subheader("📌 Key Metrics")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Customers", len(df))
col2.metric("Churn Rate (%)", round(df["churn"].mean() * 100, 2))
col3.metric("High Risk Customers", (df["risk_segment"] == "High Risk").sum())
col4.metric("Critical Priority Customers", (df["retention_priority"] == "Critical Priority").sum())

st.divider()

# -----------------------------
# Filters
# -----------------------------
st.subheader("🔍 Customer Segmentation Filters")

risk_filter = st.multiselect(
    "Select Risk Segment",
    df["risk_segment"].unique(),
    default=df["risk_segment"].unique()
)

priority_filter = st.multiselect(
    "Select Retention Priority",
    df["retention_priority"].unique(),
    default=df["retention_priority"].unique()
)

filtered_df = df[
    (df["risk_segment"].isin(risk_filter)) &
    (df["retention_priority"].isin(priority_filter))
]

st.write(f"Filtered Customers: {len(filtered_df)}")

st.dataframe(filtered_df.head(20), use_container_width=True)

st.divider()

# -----------------------------
# Visualizations
# -----------------------------
st.subheader("📈 Insights")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Churn Risk Distribution")
    st.bar_chart(df["risk_segment"].value_counts())

with col2:
    st.markdown("### Retention Priority Distribution")
    st.bar_chart(df["retention_priority"].value_counts())

st.divider()

# -----------------------------
# CLV Analysis
# -----------------------------
st.subheader("💰 Customer Lifetime Value (CLV)")

st.metric("Average CLV", round(df["clv"].mean(), 2))
st.line_chart(df["clv"].sort_values().reset_index(drop=True))

st.divider()

# -----------------------------
# Churn Prediction Section
# -----------------------------
st.subheader("🧠 Predict Churn Risk (Input-Based)")

with st.form("churn_prediction_form"):
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.slider("Age", 18, 80, 35)
        tenure = st.slider("Tenure (years)", 0, 10, 3)
        balance = st.number_input("Account Balance", 0.0, 300000.0, 50000.0)

    with col2:
        num_products = st.selectbox("Number of Products", [1, 2, 3, 4])
        is_active = st.selectbox("Active Member", [0, 1])
        has_card = st.selectbox("Has Credit Card", [0, 1])

    with col3:
        satisfaction = st.slider("Satisfaction Score", 1, 5, 3)
        complain = st.selectbox("Has Complaint", [0, 1])
        salary = st.number_input("Estimated Salary", 0.0, 200000.0, 60000.0)

    submit = st.form_submit_button("Predict Churn Risk")

# -----------------------------
# Prediction Output (ONLY after click)
# -----------------------------
if submit:
    input_data = pd.DataFrame([{
        "age": age,
        "tenure": tenure,
        "balance": balance,
        "numofproducts": num_products,
        "is_active_member": is_active,
        "has_credit_card": has_card,
        "satisfaction_score": satisfaction,
        "complain": complain,
        "estimatedsalary": salary
    }])

    input_encoded = pd.get_dummies(input_data)
    model_features = model.feature_names_in_

    for col in model_features:
        if col not in input_encoded.columns:
            input_encoded[col] = 0

    input_encoded = input_encoded[model_features]

    churn_prob = model.predict_proba(input_encoded)[0][1]

    st.success(f"🔮 Predicted Churn Probability: {round(churn_prob * 100, 2)}%")

    if churn_prob >= 0.6:
        st.error("⚠️ High Churn Risk – Immediate retention action recommended")
    elif churn_prob >= 0.3:
        st.warning("⚠️ Medium Churn Risk – Monitor closely")
    else:
        st.info("✅ Low Churn Risk – Customer likely to stay")

