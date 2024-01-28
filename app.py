import streamlit as st
import pickle

st.set_page_config(
    page_title="Spam Predictor",
    page_icon="🔎"
)

loaded_model = pickle.load(open('model.pkl', 'rb'))
loaded_vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

def predict(title): 
    if title:
        new_comment = loaded_vectorizer.transform([title])
        prediction = loaded_model.predict(new_comment)
        if prediction[0] == 'spam':
            st.subheader("Predicted Result: :red[Spam]")
        else:
            st.subheader("Predicted Result: :green[Not spam]")
    else:
        st.write("Please enter the comment to check if it is a spam message or not...")

st.title("Comment Spam Detection")
st.divider()

with st.form("comment_form"):
    title = st.text_input('Enter your message')
    predict_button = st.form_submit_button("Predict")

if predict_button:
    predict(title=title)
