from transformers import pipeline
import mlflow
import datetime
from app.core.preprocessing import preprocess

mlflow.set_tracking_uri("/app/mlruns")
mlflow.set_experiment("fake-news-emotion")  # ✅ add this line

classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")

def classify_news(text: str):
    preprocessed_text = preprocess(text)
    result = classifier(preprocessed_text)[0]
    label = result["label"].lower()
    confidence = float(result["score"])

    with mlflow.start_run():
        mlflow.set_tag("model_name", "j-hartmann/emotion-english-distilroberta-base")
        mlflow.log_param("label", label)
        mlflow.log_param("text_snippet", preprocessed_text[:100])
        mlflow.log_metric("confidence", confidence)
        mlflow.set_tag("timestamp", str(datetime.datetime.now()))

    # Rule-based fake news logic
    fake_emotions = {"anger", "fear", "surprise"}
    prediction = "fake" if label in fake_emotions and confidence > 0.4 else "real"

    return prediction, label, confidence
