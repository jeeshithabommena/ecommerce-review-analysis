# 🛒 E-Commerce Review Analysis System

A system that analyzes e-commerce product reviews to understand customer sentiment, with an interactive dashboard.

## Problem Statement
Businesses receive thousands of reviews and cannot read them all. This project automates review analysis using NLP.

## Tech Stack
- Python, Pandas, NumPy
- NLTK, TextBlob (sentiment analysis)
- Matplotlib, WordCloud (visualization)
- Streamlit (dashboard)

## Features
- Cleaned and analyzed 34,000+ Amazon product reviews
- Sentiment classification (Positive / Negative / Neutral) using TextBlob
- Comparison of text sentiment with star ratings
- Interactive dashboard with product filter, charts, and word clouds

## Key Insight
Text sentiment does not always match star ratings. Among 1-star reviews, 161 were classified as Positive in tone.

## How to Run
```bash
git clone https://github.com/jeeshithabommena/ecommerce-review-analysis.git
cd ecommerce-review-analysis
pip install -r requirements.txt
python analysis.py
streamlit run app.py
```

## Dataset
Consumer Reviews of Amazon Products (Datafiniti, via Kaggle)