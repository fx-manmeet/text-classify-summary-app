import streamlit as st
from main import run_app

def main():
    """ NLP Based App with Streamlit """
    st.title("Text Summarization and Classification with Streamlit")
    st.subheader("Natural Language Processing On the Go..")
    st.markdown("""
        #### Description
        + This is a Natural Language Processing Based App useful for basic NLP task
        Classification, Sentiment, Summarization
    """)

    run_app()

    st.sidebar.subheader("About App")
    st.sidebar.text("NLPiffy App with Streamlit")
    st.sidebar.info("Cudos to the Streamlit Team")

    st.sidebar.subheader("By")
    st.sidebar.text("Manmeet Patel")

if __name__ == '__main__':
    main()
