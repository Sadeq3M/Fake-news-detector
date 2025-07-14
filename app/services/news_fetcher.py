import os
import requests
from dotenv import load_dotenv

load_dotenv()  # ✅ Load environment variables

API_KEY = os.getenv("NEWSAPI_KEY")  # ✅ Make sure this is defined

def fetch_headlines(country="us", page_size=5):
    url = "https://newsapi.org/v2/top-headlines"
    params = {
        "apiKey": API_KEY,
        "country": country,
        "pageSize": page_size,
    }
    response = requests.get(url, params=params)
    data = response.json()

    if data.get("status") != "ok":
        raise Exception(f"NewsAPI error: {data}")

    return [
        {"title": article["title"], "source": article["source"]["name"]}
        for article in data["articles"]
    ]
