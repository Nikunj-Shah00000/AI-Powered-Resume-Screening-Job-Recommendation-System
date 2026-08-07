import streamlit as st
import joblib
import re
import nltk
from nltk.corpus import stopwords

# Define stop_words and clean_resume function locally
stop_words = set(stopwords.words("english"))

def clean_resume(text):
    text = re.sub(r"http\S+", " ", text)
    text = re.sub(r"RT|cc", " ", text)
    text = re.sub(r"#\S+", " ", text)
    text = re.sub(r"@\S+", " ", text)
    text = re.sub(r"[^\w\s]", " ", text)
    text = re.sub(r"\d+", " ", text)
    text = re.sub(r"\s+", " ", text)
    
    words = text.lower().split()
    
    words = [word for word in words if word not in stop_words]
    
    return " ".join(words)

# ----------------------------
# Load Saved Model
# ----------------------------
model = joblib.load("model/classifier.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")
encoder = joblib.load("model/encoder.pkl")

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="AI Resume Screening",
    page_icon="📄",
    layout="centered",
)

st.title("📄 AI Resume Screening & Job Recommendation System")
st.write(
    "Paste the text of a resume below to classify it into the most likely job category."
)

# ----------------------------
# Input Area
# ----------------------------
resume_text = st.text_area(
    "Resume Text",
    height=300,
    placeholder="Paste the complete resume here...",
)

# ----------------------------
# Prediction
# ----------------------------
if st.button("Predict Category"):
    if resume_text.strip() == "":
        st.warning("Please enter resume text.")
    else:
        cleaned = clean_resume(resume_text)
        
        features = vectorizer.transform([cleaned])
        
        prediction = model.predict(features)
        
        category = encoder.inverse_transform(prediction)[0]
        
        st.success(f"Predicted Category: **{category}**")
