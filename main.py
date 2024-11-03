from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from pymongo import MongoClient
import hashlib

app = FastAPI()

# MongoDB setup
client = MongoClient("mongodb://localhost:27017/")
db = client.url_shortener_db
url_collection = db.urls

class URLModel(BaseModel):
    original_url: str

@app.post("/shorten")
async def shorten_url(url: URLModel):
    # Create a hash of the URL
    url_hash = hashlib.md5(url.original_url.encode()).hexdigest()[:6]
    url_collection.insert_one({"_id": url_hash, "original_url": url.original_url})
    return {"shortened_url": f"http://127.0.0.1:8000/{url_hash}"}

@app.get("/{url_hash}")
async def redirect_url(url_hash: str):
    url_data = url_collection.find_one({"_id": url_hash})
    if url_data:
        return RedirectResponse(url_data["original_url"])
    raise HTTPException(status_code=404, detail="URL not found")
