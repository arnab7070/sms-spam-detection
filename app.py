import streamlit as st
import pickle

st.set_page_config(
    page_title="Spam Predictor",
    page_icon="🔎"
)

loaded_model = pickle.load(open('model.pkl', 'rb'))
loaded_vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

def predict(new_comment): 

    prediction = loaded_model.predict(new_comment)
    if title: 
        if prediction[0] == 'spam':
            st.subheader("This comment is :red[spam].")
        else:
            st.subheader("This comment is :green[not spam].")
    else:
        st.write("Please enter the comment to check if it is a spam message or not...")

st.title("Comment Spam Detection")
st.divider()
title = st.text_input('Enter your message')
new_comment = loaded_vectorizer.transform([title])
if st.button("Predict"): predict(new_comment=new_comment)