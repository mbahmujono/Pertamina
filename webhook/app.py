from flask import Flask, request
from pymongo import MongoClient
from dotenv import load_dotenv
from datetime import datetime

import os
load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)

# Create a MongoDB client
client = MongoClient(os.environ.get("MONGO_URI"))

# Connect to your database
db = client[os.environ.get("MONGO_DB")]

# Get your collection
collection = db[os.environ.get("MONGO_COLLECTION")]

@app.route('/webhook', methods=['POST'])
def handle_webhook():
    data = request.get_json()
    print(data)

    # Convert the timestamp string to a datetime object
    data['timestamp'] = datetime.fromisoformat(data['timestamp'])
    
    # Insert the received data into the MongoDB collection
    collection.insert_one(data)
    print("Data inserted into MongoDB.")

    return '', 200

if __name__ == "__main__":
    app.run(port=5000)
