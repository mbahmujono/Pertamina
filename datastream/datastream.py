import pandas as pd
import requests
import random
import json
from datetime import datetime
import time
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

# Function to generate random sales data
def generate_data():
    stations = [f"Pertamina_{i}" for i in range(1, 101)]
    cities = ["City_A", "City_B", "City_C", "City_D", "City_E"]
    provinces = ["Province_1", "Province_2", "Province_3", "Province_4", "Province_5"]  # Example province names
    kecamatans = [f"Kecamatan_{i}" for i in range(1, 21)]  # Example kecamatan

    data = {
        "station": random.choice(stations),
        "city": random.choice(cities),
        "province": random.choice(provinces),
        "kecamatan": random.choice(kecamatans),
        "sales": random.uniform(500, 10000),  # Random sales value
        "timestamp": datetime.now().isoformat()
    }
    return data


# Function to post data to a webhook
def post_data_to_webhook(data):
    webhook_url = os.environ.get("WEBHOOK_URL")  # Fetch webhook URL from environment
    if webhook_url is None:
        print("Webhook URL not found in environment.")
        return

    headers = {'Content-Type': 'application/json'}
    response = requests.post(webhook_url, data=json.dumps(data), headers=headers)
    print(f"Data posted to webhook. Status Code: {response.status_code}")


# Main function to generate and post data every 10 minutes
def main():
    while True:
        sales_data = generate_data()
        df = pd.DataFrame([sales_data])
        print(df)
        post_data_to_webhook(sales_data)
        time.sleep(5)  # Wait for 10 minutes


if __name__ == "__main__":
    main()
