# 🏠 Real Estate Price Prediction using Machine Learning

An end-to-end Data Science project that predicts residential property prices based on area, number of bedrooms (BHK), and location. The project integrates web scraping, machine learning, deployment, and business intelligence visualization.

---

## 🚀 Project Highlights

- Automated data scraping using BeautifulSoup and Selenium  
- Data preprocessing and feature engineering  
- Machine Learning models: Linear Regression & Random Forest  
- High-accuracy Random Forest model (R² ≈ 0.995)  
- Interactive Streamlit web application for real-time predictions  
- PowerBI dashboard for market insights and visualization  

---

## 🧠 Tech Stack

- **Programming:** Python  
- **Libraries:** Pandas, NumPy, Scikit-learn  
- **Web Scraping:** BeautifulSoup, Selenium  
- **ML Models:** Linear Regression, Random Forest  
- **Deployment:** Streamlit, CLI  
- **Visualization:** PowerBI  

---

## 📊 Project Screenshots

### Streamlit Web App
![Streamlit App](screenshots/streamlit_app.png)

### PowerBI Dashboard
![PowerBI Dashboard](screenshots/powerbi_dashboard.png)

### CLI Prediction Output
![CLI Output](screenshots/cli_output.png)

---

## 📂 Project Structure

real-estate-price-prediction/
│
├── app/
│ ├── app.py
│ └── predict_cli.py
│
├── data/
│ └── final_realestate_data.csv
│
├── models/
│ ├── price_model.pkl
│ └── price_model_rf.pkl
│
├── powerbi/
│ └── RealEstate_Dashboard.pbix
│
├── screenshots/
│ ├── streamlit_app.png
│ ├── powerbi_dashboard.png
│ ├── cli_output.png
│ └── dataset_preview.png
│
└── report/
└── Real_Estate_Price_Prediction_Report.pdf

