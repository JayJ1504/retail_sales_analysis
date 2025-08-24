import streamlit as st
import pandas as pd
import joblib
import os

model_path = os.path.join("model", "retail_sales_forecaster.pkl")
model = joblib.load(model_path)

st.title("🛍️ Retail Sales Forecasting App")
st.write("Predict weekly sales using historical, economic, and promotional data.")

# --- Section 1: Store Info ---
st.header(" Store Information")
col1, col2 = st.columns(2)
with col1:
    store = st.number_input("Store ID", min_value=1, step=1)
with col2:
    dept = st.number_input("Department ID", min_value=1, step=1)
is_holiday = st.selectbox("Is Holiday?", ["No", "Yes"])
is_holiday = 1 if is_holiday == "Yes" else 0

# --- Section 2: Economic Indicators ---
st.header(" Economic Indicators")
col3, col4 = st.columns(2)
with col3:
    temperature = st.number_input("Temperature", value=70.0)
    cpi = st.number_input("CPI", value=200.0)
with col4:
    fuel_price = st.number_input("Fuel Price", value=3.0)
    unemployment = st.number_input("Unemployment Rate", value=7.0)

# --- Section 3: Markdown Promotions ---
st.header(" Markdown Promotions")
col5, col6 = st.columns(2)
with col5:
    markdown1 = st.number_input("MarkDown1", value=0.0)
    markdown2 = st.number_input("MarkDown2", value=0.0)
    markdown3 = st.number_input("MarkDown3", value=0.0)
with col6:
    markdown4 = st.number_input("MarkDown4", value=0.0)
    markdown5 = st.number_input("MarkDown5", value=0.0)

# --- Section 4: Lag Features ---
st.header(" Lag Features")
col7, col8 = st.columns(2)
with col7:
    lag1 = st.number_input("Lag_1 (Sales 1 week ago)", value=0.0)
    lag2 = st.number_input("Lag_2 (Sales 2 weeks ago)", value=0.0)
with col8:
    lag3 = st.number_input("Lag_3 (Sales 3 weeks ago)", value=0.0)
    rolling_mean_4 = st.number_input("Rolling Mean (Last 4 Weeks)", value=0.0)


input_data = pd.DataFrame({
    "Store": [store],
    "Dept": [dept],
    "IsHoliday": [is_holiday],
    "Temperature": [temperature],
    "Fuel_Price": [fuel_price],
    "CPI": [cpi],
    "Unemployment": [unemployment],
    "MarkDown1": [markdown1],
    "MarkDown2": [markdown2],
    "MarkDown3": [markdown3],
    "MarkDown4": [markdown4],
    "MarkDown5": [markdown5],
    "Lag_1": [lag1],
    "Lag_2": [lag2],
    "Lag_3": [lag3],
    "Rolling_Mean_4": [rolling_mean_4]
})

# --- Prediction ---
if st.button(" Predict Sales"):
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Weekly Sales: **${prediction:,.2f}**")
