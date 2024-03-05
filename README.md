Project name
- Sentiment Analysis and Text Similarity
  
Description
-This project performs sentiment analysis on Amazon product reviews using SpaCy and provides a function to determine the similarity between two sentences.

Importance
- Sentiment analysis helps in understanding customer opinions and feedback, which can be crucial for businesses to make informed decisions. Text similarity aids in tasks like duplicate detection, recommendation systems, and more.
  
Table of Contents
- Installation
- Usage
- Credits

Instalation
To use this project locally, follow these steps:

Install the required dependencies:
  pip install spacy pandas spacytextblob

Download the English language model for SpaCy:
  python -m spacy download en_core_web_sm



Usage
After installing the project, you can perform sentiment analysis and text similarity as follows:

Sentiment Analysis:
The function clean_text(whole_review_data) cleans the provided text data by converting to lowercase, removing stop words, and leading/trailing whitespaces. It returns a dictionary with original and cleaned texts.
The function sentiment_analysis(cleaned_data) analyzes the sentiment of cleaned text data using SpaCy's TextBlob extension.
Text Similarity:
The function similarity(first, second) calculates the similarity between two sentences using SpaCy's word vectors.

Credits
The project is authored by Liliana (GitHub Profile - lilypereira).
  
○ An installation section that tells other users how to install your project
locally.


