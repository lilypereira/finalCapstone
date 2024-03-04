import spacy
import pandas as pd
from spacytextblob.spacytextblob import SpacyTextBlob


# Load spaCy model and add textblob extension
nlp = spacy.load("en_core_web_sm")
nlp.add_pipe('spacytextblob')

def preprocess_text(reviews):
    #Preprocess text data by removing stopwords and performing basic cleaning
    doc = nlp(reviews)
    # Remove stopwords and punctuation
    cleaned_text = [token.text.lower() for token in doc if not token.is_stop and token.is_punct]
    return " ".join(cleaned_text)

# Function to test sentiment in clean data
def sentimenT_analisys(cleaned_data):
    for key, value in cleaned_data.items():
        doc = nlp(value)
        print(f'\nReview: {key, value}')
        print(f'Sentiment: {doc._.blob.polarity}')
    
# Load amazon dataset
amazon_ds = pd.read_csv('amazon_product_reviews.csv', sep= ',', low_memory=False)

# Clean Data
amazon_ds = amazon_ds.dropna(subset=['reviews.text'])
reviews_data = amazon_ds['reviews.text'].iloc[[15, 34, 67, 200, 350, 550, 1500, 3500, 7000, 10000,
11500, 16500, 18000, 19500, 25000, 34000]]

# Perform sentiment analysis
sentimenT_analisys(reviews_data)

# Load a medium-sized English model
nlp = spacy.load('en_core_web_md')

# Compare similarity of two product reviews
review_of_choice1 = amazon_ds['reviews.text'].iloc[4000]
review_of_choice2 = amazon_ds['reviews.text'].iloc[33500]

# Calculate similarity score
similarity_score = nlp(review_of_choice1).similarity(nlp(review_of_choice2))

# Print the reviews and similarity score
print(f'\nReview One: {review_of_choice1}')
print(f'Review Two: {review_of_choice2}')
#print(f'Similarity: {similarity_score (review1, review2)}')
print(f'Similarity between review one and review 2: {similarity_score}')
