import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

st.set_page_config(page_title="E-Commerce Review Analysis", layout="wide")
st.title("🛒 E-Commerce Review Analysis Dashboard")

@st.cache_data
def load_data():
    return pd.read_csv('data/reviews_with_sentiment.csv')

df = load_data()

st.sidebar.header("Filters")
products = sorted(df['product_name'].dropna().unique())
selected = st.sidebar.selectbox("Product", ['All'] + products)
filtered = df if selected == 'All' else df[df['product_name'] == selected]
st.write(f"Showing **{len(filtered)}** reviews")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Sentiment Distribution")
    order = ['Positive', 'Neutral', 'Negative']
    counts = filtered['sentiment'].value_counts().reindex(order, fill_value=0)
    fig1, ax1 = plt.subplots()
    ax1.bar(order, counts.values, color=['green', 'gray', 'red'])
    st.pyplot(fig1)

with col2:
    st.subheader("Rating Distribution")
    ratings = filtered['rating'].value_counts().sort_index()
    fig2, ax2 = plt.subplots()
    ax2.bar(ratings.index.astype(int).astype(str), ratings.values, color='skyblue')
    st.pyplot(fig2)

st.subheader("Word Cloud")
choice = st.radio("Sentiment:", ['Positive', 'Negative', 'Neutral'], horizontal=True)
text = ' '.join(filtered[filtered['sentiment'] == choice]['cleaned_review'].dropna())

if text.strip():
    wc = WordCloud(width=800, height=400, background_color='white').generate(text)
    fig3, ax3 = plt.subplots(figsize=(10, 5))
    ax3.imshow(wc, interpolation='bilinear')
    ax3.axis('off')
    st.pyplot(fig3)
else:
    st.write("Not enough data for this selection.")

st.subheader("Sample Reviews")
st.dataframe(filtered[['product_name', 'rating', 'sentiment', 'review_text']]
             .sample(min(10, len(filtered))))