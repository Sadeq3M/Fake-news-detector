# Backend Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY ./app /app
COPY ./requirements.txt /app/requirements.txt

RUN pip install --upgrade pip \
 && pip install -r requirements.txt \
 && python -m nltk.downloader punkt stopwords \
 && python -m spacy download en_core_web_sm

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
