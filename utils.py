import joblib
import os
from nlp import get_sentiment, summarize_text

# Load models
MNB_model = joblib.load(os.path.join('email_models', 'pipeline_modelMNB.pkl'))
CNB_model = joblib.load(os.path.join('email_models', 'pipeline_modelCNB.pkl'))
SVC_model = joblib.load(os.path.join('email_models', 'pipeline_modelSVC.pkl'))

def load_model(model_name):
    if model_name == 'Multinomial Naive Bayes':
        return MNB_model
    elif model_name == 'Complement Naive Bayes':
        return CNB_model
    elif model_name == 'Support Vector Classifier':
        return SVC_model
    else:
        return SVC_model

def perform_spam_detection(message, model_name):
    model = load_model(model_name)
    return model.predict([message])[0]

def perform_sentiment_analysis(message):
    return get_sentiment(message)

def perform_summarization(message, model_name):
    return summarize_text(message, model_type=model_name)
