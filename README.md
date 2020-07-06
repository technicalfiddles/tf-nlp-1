# tf-nlp-1

## Introductory Sentiment Analysis with Vader.

For a super quickly deployed app, try using Streamlit with Vader. For getting a prototype on the web quickly, deploy it on Heroku with minimal configuration requirements. 

Check out the app here:  
[https://tf-nlp-1.herokuapp.com/](https://tf-nlp-1.herokuapp.com/)

The following are needed for Heroku to run a Streamlit app:

	1. Your Streamlit app (app.py or similar)
	2. Requirements file (recommend installing pipreqs to generate)
	3. A file named Procfile that contains instructions for Heroku to run your app.

Example Procfile:  
	'''web: streamlit run --server.enableCORS false --server.port $PORT your-app-name.py'''
