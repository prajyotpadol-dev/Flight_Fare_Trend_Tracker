# ================================
# Flight Fare Trend Tracker App
# ================================

import pandas as pd
import streamlit as st
from prophet import Prophet
import matplotlib.pyplot as plt

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(
    page_title="Flight Fare Trend Tracker & Predictor",
    page_icon="✈️",
    layout="wide"
)

# -------------------------------
# Title
# -------------------------------
st.title("✈️ Flight Fare Trend Tracker & Predictor")
st.write("Predict future flight fares using historical pricing data.")

# -------------------------------
# Load Data
# -------------------------------
@st.cache_data
def load_data():
    return pd.read_csv("data/flight_fares.csv", parse_dates=["scrape_date"])

df = load_data()

# -------------------------------
# Sidebar Filters
# -------------------------------
st.sidebar.header("🔍 Filter Options")

origin = st.sidebar.selectbox("Select Origin", sorted(df["origin"].unique()))
destination = st.sidebar.selectbox("Select Destination", sorted(df["destination"].unique()))

# -------------------------------
# Filtered Data
# -------------------------------
filtered_df = df[
    (df["origin"] == origin) &
    (df["destination"] == destination)
]

# -------------------------------
# Historical Fare Trend
# -------------------------------
st.subheader("📊 Historical Fare Trend")

# Initialize prophet_df safely
prophet_df = pd.DataFrame()

if filtered_df.empty:
    st.warning("No data available for the selected route.")
else:
    daily_avg = (
        filtered_df
        .groupby("scrape_date")["price"]
        .mean()
        .reset_index()
    )

    st.line_chart(daily_avg.set_index("scrape_date"))

    prophet_df = daily_avg.rename(
        columns={"scrape_date": "ds", "price": "y"}
    )

# -------------------------------
# Price Forecast
# -------------------------------
st.subheader("📈 Price Forecast")

if prophet_df.shape[0] < 2:
    st.warning("⚠️ Not enough data to build forecast. Please select a different route.")
else:
    model = Prophet()
    model.fit(prophet_df)

    future = model.make_future_dataframe(periods=7)
    forecast = model.predict(future)

    fig = model.plot(forecast)
    st.pyplot(fig)
