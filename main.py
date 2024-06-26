import streamlit as st
from utils import load_model, perform_spam_detection, perform_sentiment_analysis, perform_summarization

def run_app():
    # Spam detection
    if st.checkbox("Do Spam Detection"):
        st.subheader("Put your message")
        message = st.text_area("Enter Text", "Type Here ..", key='k1')
        detection_options = st.selectbox("Choose Classifier", ['Multinomial Naive Bayes', 'Complement Naive Bayes', 'Support Vector Classifier'])
        if st.button("Detect"):
            detection_result = perform_spam_detection(message, detection_options)
            st.success(detection_result)
    
    # Sentiment Analysis
    if st.checkbox("Show Sentiment Analysis"):
        st.subheader("Analyse Your Text")
        message = st.text_area("Enter Text", "Type Here ..", key='k2')
        if st.button("Analyze"):
            result_sentiment = perform_sentiment_analysis(message)
            st.success(result_sentiment)

    # Summarization
    if st.checkbox("Show Text Summarization"):
        st.subheader("Summarize Your Text")
        msg = st.text_area("Enter Text", "Type Here ..", key='k3')
        summary_options = st.selectbox("Choose Summarizer", ['gpt2', 'XLNet'])
        if st.button("Summarize"):
            summary_result = perform_summarization(msg, summary_options)
            st.success(summary_result)
