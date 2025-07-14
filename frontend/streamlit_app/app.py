import streamlit as st
import requests

st.set_page_config(page_title="📰 Fake News Detector", layout="wide")

st.title("🧠 Real-Time News Analysis")

# ---- Live News Section ----
st.subheader("🔎 Automated News Scan")

with st.spinner("Fetching live headlines..."):
    try:
        res = requests.get("http://localhost:8000/scan?country=us&limit=10")
        news_items = res.json()["results"]
    except Exception as e:
        st.error(f"Failed to fetch news: {e}")
        news_items = []

for item in news_items:
    col1, col2 = st.columns([4, 1])
    with col1:
        st.markdown(f"**{item['headline']}**  \n*{item['source']}*")
    with col2:
        label = "🟢 REAL" if item['prediction'] == "real" else "🔴 FAKE"
        st.metric(label=label, value=f"{item['confidence']*100:.1f}%")

    st.progress(min(item['confidence'], 1.0))
    st.caption(f"Emotion: `{item['emotion']}`")
    st.markdown("---")

# ---- Manual Input Section ----
st.subheader("📝 Manual News Check")

text_input = st.text_area("Paste a news article to analyze manually", height=150)

if st.button("Analyze"):
    with st.spinner("Analyzing..."):
        try:
            res = requests.post("http://localhost:8000/predict", json={"content": text_input})
            data = res.json()
            st.success(f"Prediction: {data['prediction'].upper()} (Confidence: {data['confidence']*100:.1f}%)")
            st.info(f"Detected Emotion: {data['emotion']}")
            st.caption(f"Explanation: {data['explanation']}")
        except Exception as e:
            st.error(f"Error: {e}")
