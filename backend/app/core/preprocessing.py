import re
import nltk
import spacy
from nltk.corpus import stopwords

nltk_stopwords = set(stopwords.words("english"))
nlp = spacy.load("en_core_web_sm", disable=["parser", "ner"])

def clean_text(text: str) -> str:
    # Remove URLs, mentions, non-ASCII characters
    text = re.sub(r"http\S+|www\S+|@\w+", "", text)
    text = re.sub(r"[^\x00-\x7F]+", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def lemmatize_and_filter(text: str) -> str:
    doc = nlp(text)
    return " ".join([
        token.lemma_.lower()
        for token in doc
        if token.is_alpha and token.lemma_.lower() not in nltk_stopwords
    ])

def preprocess(text: str) -> str:
    cleaned = clean_text(text)
    return lemmatize_and_filter(cleaned)
