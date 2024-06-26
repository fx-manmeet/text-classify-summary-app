from textblob import TextBlob
from summarizer import TransformerSummarizer

# Summarizer models
GPT2_model = TransformerSummarizer(transformer_type="GPT2", transformer_model_key="gpt2-medium")
XLNet_model = TransformerSummarizer(transformer_type="XLNet", transformer_model_key="xlnet-base-cased")

def get_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment

def summarize_text(text, model_type='gpt2', min_length=60):
    if model_type == 'gpt2':
        return ''.join(GPT2_model(text, min_length=min_length))
    elif model_type == 'XLNet':
        return ''.join(XLNet_model(text, min_length=min_length))
    else:
        return ''.join(GPT2_model(text, min_length=min_length))
