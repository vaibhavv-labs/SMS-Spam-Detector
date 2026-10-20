import streamlit as st
import joblib

model = joblib.load("spam_model.pkl")
tfidf = joblib.load("tfidf.pkl")

st.title("AI Scam Message Detector")
st.write("Check whether an SMS looks like spam.")

message = st.text_area("Enter your message")

if st.button("Check Message"):
    if message.strip():
        text = tfidf.transform([message])
        prediction = model.predict(text)[0]

        if prediction == "spam":
            st.error("Likely Spam")
        else:
            st.success("Likely Legitimate")
    else:
        st.warning("Please enter a message.")
