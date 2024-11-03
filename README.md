# URL Shortener

A simple URL shortener built with FastAPI and MongoDB.

## Features

- Shorten long URLs into short, manageable links.
- Retrieve the original URL from a shortened link.

## Requirements

- Python 3.8+
- FastAPI
- uvicorn
- pymongo
- hashlib

## Installation

1.Clone the repository:
   ```bash
   git clone https://github.com/ManikantaSarma45/url-shortener.git
   cd url-shortener

2.Install the required packages:

pip install -r requirements.txt

3.Start your MongoDB server:

mongod

4.Run the FastAPI application:

uvicorn main:app --reload