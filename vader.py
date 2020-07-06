import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def sentiment_analyzer_scores(sentence):
    score = analyzer.polarity_scores(sentence)
    return score


st.title('Introduction to NLP with Vader')

sentence = st.text_input("enter sentence")

st.write(sentence)

score = sentiment_analyzer_scores(sentence)
st.write(score)