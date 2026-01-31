# ✈️ Flight Fare Trend Tracker & Predictor

This project is an end-to-end Data Science application developed as part of an **internship program**.  
It focuses on collecting flight fare data, analyzing historical price trends, and predicting future flight prices using time series forecasting.  
An interactive **Streamlit web application** is also developed to visualize trends and forecasts.

---

## 🎯 Objective

The main objectives of this project are:
- To collect flight fare data through web scraping
- To analyze historical flight price trends
- To perform feature engineering and data preprocessing
- To build a time series forecasting model using Prophet
- To deploy a user-friendly web application for visualization and prediction

---

## 🧠 Technologies Used

- **Programming Language:** Python  
- **Libraries & Tools:**
  - pandas, numpy
  - matplotlib, seaborn, plotly
  - scikit-learn
  - prophet
  - streamlit
- **IDE:** Visual Studio Code  
- **Version Control:** Git & GitHub  

---

## 📂 Project Structure

Flight_Fare_Trend_Tracker/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│ ├── flight_fares.csv
│ └── cleaned_flight_fares.csv
│
├── models/
│ └── prophet_model.pkl
│
├── notebooks/
│ ├── Web_Scraping_and_Dataset_Generation.ipynb
│ ├── EDA_and_Feature_Engineering.ipynb
│ └── Flight_Fare_Time_Series_Forecasting.ipynb
│
├── Report/
│ └── flight_fare_predictor.pdf
│
└── PPT/
└── Flight Fare Trend Tracker & Price Prediction.pptx


---

## 🔄 Project Workflow

1. **Web Scraping & Dataset Generation**
   - Flight fare data is collected and stored in CSV format.

2. **Exploratory Data Analysis (EDA)**
   - Price trend analysis
   - Route-wise fare comparison
   - Visualization of historical patterns

3. **Feature Engineering**
   - Data cleaning
   - Date and time-based transformations
   - Aggregation for time series modeling

4. **Time Series Forecasting**
   - Model built using Facebook Prophet
   - Forecasts future flight prices based on historical data

5. **Web Application Development**
   - Built using Streamlit
   - Displays historical trends and future price forecasts interactively

---

## ▶️ How to Run the Project

### Step 1: Clone the Repository
```bash
git clone https://github.com/prajyotpadol-dev/Flight_Fare_Trend_Tracker.git
cd Flight_Fare_Trend_Tracker

### Step 2: Install Required Libraries
pip install -r requirements.txt

### Step 3: Run the Streamlit App
streamlit run app.py

The application will be available at:
http://localhost:8501
