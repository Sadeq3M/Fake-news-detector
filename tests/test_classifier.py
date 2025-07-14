from app.models.predictor import classify_news

def test_prediction():
    label, confidence = classify_news("Breaking: NASA finds alien life on Mars!")
    assert label in ["real", "fake"]
    assert 0 <= confidence <= 1
