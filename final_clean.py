import pandas as pd

df = pd.read_csv("../data/selenium_scraped_realestate.csv")

# Remove duplicates
df = df.drop_duplicates()

# Ensure correct data types
df["Price"] = df["Price"].astype(float)
df["Area"] = df["Area"].astype(int)
df["BHK"] = df["BHK"].astype(int)

# Remove unrealistic values
df = df[(df["Price"] > 500000) & (df["Price"] < 50000000)]
df = df[(df["Area"] > 300) & (df["Area"] < 5000)]
df = df[(df["BHK"] > 0) & (df["BHK"] < 10)]

# Save final clean file
df.to_csv("../data/final_realestate_data.csv", index=False)

print("Final clean dataset ready!")
print("Rows:", len(df))
print(df.head())
