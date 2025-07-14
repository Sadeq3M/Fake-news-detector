from fastapi import APIRouter
from app.services.news_fetcher import fetch_headlines
from app.models.predictor import classify_news

router = APIRouter()

@router.get("/scan")
def scan_news(country: str = "us", limit: int = 5):
    # ✅ Define headlines first
    articles = fetch_headlines(country=country, page_size=limit)
    results = []

    for article in articles:
        title = article["title"]
        source = article["source"]
        prediction, emotion, confidence = classify_news(title)
        results.append({
            "headline": title,
            "source": source,
            "prediction": prediction,
            "emotion": emotion,
            "confidence": round(confidence, 3),
        })

    return {"results": results}
