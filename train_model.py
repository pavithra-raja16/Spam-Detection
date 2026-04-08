# train_model.py

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

# Step 1: Create simple dataset
data = {
    'text': [
        "Win money now",
        "Hello friend",
        "Free offer available",
        "How are you",
        "Claim your prize now",
        "Let's meet tomorrow"
    ],
    'label': [1, 0, 1, 0, 1, 0]   # 1 = Spam, 0 = Not Spam
}

df = pd.DataFrame(data)

# Step 2: Split input and output
X = df['text']
y = df['label']

# Step 3: Convert text to numbers
vectorizer = CountVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# Step 4: Train model
model = MultinomialNB()
model.fit(X_vectorized, y)

# Step 5: Save model + vectorizer
with open("model.pkl", "wb") as f:
    pickle.dump((model, vectorizer), f)

print("✅ Model trained successfully!")
print("📁 model.pkl file created")