from pymongo import MongoClient
import os

DATABASE_URL = "mongodb://localhost:27017/"
client = MongoClient(DATABASE_URL)
db = client["url_shortener_db"]
urls_collection = db["urls"]
