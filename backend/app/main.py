from fastapi import FastAPI
from pydantic import BaseModel
from app.models.predictor import classify_news
from app.api.auto_scan import router as scan_router

app = FastAPI()

app.include_router(scan_router)

class NewsInput(BaseModel):
    content: str

@app.post("/predict")
def predict_fake_news(news: NewsInput):
    prediction, emotion, confidence = classify_news(news.content)
    return {
        "prediction": prediction,
        "emotion": emotion,
        "confidence": round(confidence, 3),
        "explanation": f"The news text was classified as expressing '{emotion}' emotion.",
        "source_credibility": 0.8,
        "related_articles": []
    }
