import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import joblib

# Load clean data
df = pd.read_csv("../data/final_realestate_data.csv")

# Encode Location
df_encoded = pd.get_dummies(df, columns=["Location"], drop_first=True)

# Features & Target
X = df_encoded.drop(["Title", "Price"], axis=1)
y = df_encoded["Price"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Random Forest model
model = RandomForestRegressor(
    n_estimators=200,
    max_depth=15,
    min_samples_split=5,
    random_state=42
)

model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Metrics
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Save model
joblib.dump(model, "price_model_rf.pkl")

print("Random Forest model trained successfully!")
print("MAE:", round(mae, 2))
print("R2 Score:", round(r2, 3))
print("Model saved as price_model_rf.pkl")
