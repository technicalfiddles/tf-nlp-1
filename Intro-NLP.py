import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def sentiment_analyzer_scores(sentence):
    score = analyzer.polarity_scores(sentence)
    return score

st.title('Intro to Natural Language Processing')


sentence = st.text_input("enter sentence below")
st.write(sentence)

score = sentiment_analyzer_scores(sentence)
st.write(score)

st.write('Compound > 0 indicates positive sentiment.  \nCompound < 0 indicates negative sentiment.')



st.write("  \n")
st.header('Tutorial - how to make this yourself!')

st.markdown('Tools Used:  \n'
    '- Python  \n'
    '- Vader Sentiment Analyzer  \n'
    '- Streamlit  \n'
    '- Heroku')

st.write("First, install dependencies:")  
st.code("pip install streamlit \npip install vaderSentiment")

st.write("Next, start building your app.  \n"
    "This app is simple enough that you can write it in any text editor (notepad, sublime, etc.)  \n"
    "Let's look at the entire app, as it is only a few lines of code.")
st.code("import streamlit as st \n"
    "from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer \n"
    "analyzer = SentimentIntensityAnalyzer() \n"
    " \n"
    "def sentiment_analyzer_scores(sentence):\n"
    "   score = analyzer.polarity_scores(sentence) \n"
    "   return score \n"
    " \n"
    "st.title('Intro to Natural Language Processing') \n"
    "st.markdown('Tools Used: \\n'\n"
    "   '- Python  \\n'\n"
    "   '- Vader Sentiment Analyzer  \\n'\n"
    "   '- Streamlit  \\n'\n"
    "   '- Heroku')   \n"
    "  \n"
    "sentence = st.text_input('enter sentence below') \n"
    "st.write(sentence) \n"
    " \n"
    "score = sentiment_analyzer_scores(sentence) \n"
    "st.write(score) \n"
    "st.write('Compound > 0 indicates positive sentiment.  \\nCompound < 0 indicates negative sentiment.')")


st.write("That's the entire app!  \n"
    " \n"
    "Streamlit allows you to add interactivity with little effort \n"
    "For example, let's look at the following code and the resulting interactive text box:")
with st.echo(code_location='above'):
    my_sentence = st.text_input("enter sentence")
    st.write(my_sentence)

st.write("Go ahead and enter something in the text box - you'll see it displayed right above this line!")

st.markdown("Any time you see 'st', it is applying a method from the streamlit library:  \n"
        "- st.title --> gives you a title..  \n"
        "- st.write --> prints to your webpage..  \n"
        "- st.markdown --> displays text formatted as markdown..")

st.write("References:  \n"
"Vader: https://medium.com/analytics-vidhya/simplifying-social-media-sentiment-analysis-using-vader-in-python-f9e6ec6fc52f  \n"
"Streamlit --> Heroku: https://discuss.streamlit.io/t/hosting-streamlit-on-heroku/132/13")