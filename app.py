import streamlit as st
import joblib
import pandas as pd

st.set_page_config(page_title="Real Estate Price Predictor")

# Load model
model = joblib.load("../models/price_model_rf.pkl")

# Load feature columns
df = pd.read_csv("../data/final_realestate_data.csv")
df_encoded = pd.get_dummies(df, columns=["Location"], drop_first=True)
feature_columns = df_encoded.drop(["Title", "Price"], axis=1).columns

st.title("🏠 Real Estate Price Predictor(Random Forest Model)")

area = st.number_input("Area (sqft)", min_value=300, max_value=20000, value=1200)
bhk = st.selectbox("BHK", [1, 2, 3, 4, 5])

location = st.selectbox(
    "Location",
    sorted(df["Location"].unique())
)

if st.button("Predict Price"):
    input_data = {"Area": area, "BHK": bhk}

    for col in feature_columns:
        if col.startswith("Location_"):
            input_data[col] = 1 if col == f"Location_{location}" else 0

    input_df = pd.DataFrame([input_data])
    prediction = model.predict(input_df)[0]

    st.success(f"Predicted Property Price: ₹ {round(prediction, 2)}")
