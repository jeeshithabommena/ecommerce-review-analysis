import re
import pandas as pd
import nltk
from nltk.corpus import stopwords
from textblob import TextBlob

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# 1. Load raw data
df = pd.read_csv('data/raw_reviews.csv', low_memory=False)
print("Loaded:", df.shape)

# 2. Keep useful columns and rename them
df = df[['name', 'reviews.date', 'reviews.rating', 'reviews.text', 'reviews.title']]
df = df.rename(columns={
    'name': 'product_name',
    'reviews.date': 'review_date',
    'reviews.rating': 'rating',
    'reviews.text': 'review_text',
    'reviews.title': 'review_title'
})

# 3. Remove missing values and duplicates
df = df.dropna(subset=['review_text', 'rating'])
df = df.drop_duplicates(subset=['review_text'])
print("After cleaning:", df.shape)

# 4. Clean text (used for word clouds)
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'[^a-z\s]', '', text)
    return ' '.join(w for w in text.split() if w not in stop_words)

df['cleaned_review'] = df['review_text'].apply(clean_text)

# 5. Sentiment on the ORIGINAL text (keeps words like "not")
def get_sentiment(text):
    polarity = TextBlob(str(text)).sentiment.polarity
    if polarity > 0.1:
        return 'Positive'
    elif polarity < -0.1:
        return 'Negative'
    return 'Neutral'

df['sentiment'] = df['review_text'].apply(get_sentiment)

# 6. Compare sentiment with star ratings
print(pd.crosstab(df['rating'], df['sentiment']))

# 7. Save for the dashboard
df.to_csv('data/reviews_with_sentiment.csv', index=False)
print("Saved data/reviews_with_sentiment.csv")