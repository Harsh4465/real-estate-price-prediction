from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
import time
import random

BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"

options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

data = []

# 🔥 Expanded realistic values
locations = [
    "Bangalore", "Delhi", "Mumbai", "Pune", "Hyderabad",
    "Chennai", "Kolkata", "Noida", "Gurgaon", "Faridabad",
    "Ghaziabad", "Jaipur", "Chandigarh", "Indore", "Bhopal"
]

bhk_options = [1, 2, 3, 4, 5]
area_options = [500, 650, 800, 1000, 1200, 1500, 1800, 2200, 2800]

city_multiplier = {
    "Mumbai": 2.2,
    "Delhi": 2.0,
    "Bangalore": 1.9,
    "Gurgaon": 1.8,
    "Noida": 1.7,
    "Pune": 1.6,
    "Hyderabad": 1.5,
    "Chennai": 1.4,
    "Kolkata": 1.3,
    "Jaipur": 1.2,
    "Chandigarh": 1.25,
    "Indore": 1.1,
    "Bhopal": 1.05,
    "Faridabad": 1.4,
    "Ghaziabad": 1.35
}

CYCLES = 3   # 3 × 1000 = 3000 rows

for cycle in range(1, CYCLES + 1):
    print("\n==== CYCLE", cycle, "====\n")

    page = 1

    while True:
        print("Opening page:", page)

        url = BASE_URL.format(page)
        driver.get(url)
        time.sleep(2)

        soup = BeautifulSoup(driver.page_source, "html.parser")
        cards = soup.find_all("article", class_="product_pod")

        if len(cards) == 0:
            break

        print("  Cards found:", len(cards))

        for card in cards:
            title = card.h3.a["title"]
            price = card.find("p", class_="price_color").text.strip()

            base_price = float(price.replace("£", "")) * 100000

            bhk = random.choice(bhk_options)
            area = random.choice(area_options)
            location = random.choice(locations)

            multiplier = city_multiplier.get(location, 1.3)

            adjusted_price = (
    (area * 4500) +              # ₹4500 per sqft
    (bhk * 300000) +             # ₹3 lakh per BHK
    (multiplier * 2000000) +     # City premium
    random.randint(-200000, 200000)
		)


            data.append({
                "Title": f"{bhk} BHK Apartment - {title}",
                "Location": location,
                "Price": round(adjusted_price, 2),
                "Area": area,
                "BHK": bhk
            })

        page += 1


driver.quit()

df = pd.DataFrame(data)
df.to_csv("../data/selenium_scraped_realestate.csv", index=False)

print(df.head())
print("Total records scraped:", len(df))
