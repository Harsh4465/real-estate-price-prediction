import joblib
import pandas as pd

# Load model
model = joblib.load("../models/price_model.pkl")

# Load columns (from training data)
df = pd.read_csv("../data/final_realestate_data.csv")
df_encoded = pd.get_dummies(df, columns=["Location"], drop_first=True)
feature_columns = df_encoded.drop(["Title", "Price"], axis=1).columns

print("=== Real Estate Price Predictor ===")

area = int(input("Enter Area (sqft): "))
bhk = int(input("Enter BHK: "))
location = input("Enter Location (e.g., Bangalore, Delhi, Mumbai): ")

# Create input row
input_data = {"Area": area, "BHK": bhk}

for col in feature_columns:
    if col.startswith("Location_"):
        input_data[col] = 1 if col == f"Location_{location}" else 0

input_df = pd.DataFrame([input_data])

# Predict
prediction = model.predict(input_df)[0]

print("\nPredicted Property Price: ₹", round(prediction, 2))
