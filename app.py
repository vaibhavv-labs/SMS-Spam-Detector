import streamlit as st
import joblib

# Page configuration
st.set_page_config(
    page_title="AI Scam Message Detector",
    page_icon="🛡️",
    layout="centered"
)

# Load model and vectorizer with caching
@st.cache_resource
def load_artifacts():
    model = joblib.load("spam_model.pkl")
    tfidf = joblib.load("tfidf.pkl")
    return model, tfidf

model, tfidf = load_artifacts()

st.title("🛡️ AI Scam Message Detector")
st.write("Analyze SMS, smishing, or text messages to detect spam, phishing, and fraudulent content.")

# Quick sample buttons
st.markdown("**Quick test examples:**")
col1, col2, col3 = st.columns(3)
sample_msg = ""
if col1.button("🎁 Prize Scam"):
    sample_msg = "URGENT! You have won a FREE cash prize! Call now to claim your reward!"
if col2.button("⚠️ Account Phishing"):
    sample_msg = "Dear customer, KYC verification is pending for your account. Update immediately to prevent block: http://sbi-kyc.net"
if col3.button("💬 Normal SMS"):
    sample_msg = "Hey, are we still meeting at 6 pm?"

message = st.text_area("Enter your message:", value=sample_msg, height=120)

if st.button("Check Message", type="primary"):
    if message.strip():
        text_vec = tfidf.transform([message])
        
        # Retrieve class index for 'spam' and 'ham'
        classes = list(model.classes_)
        spam_idx = classes.index("spam")
        ham_idx = classes.index("ham")
        
        # Calculate posterior probabilities
        probabilities = model.predict_proba(text_vec)[0]
        spam_prob = float(probabilities[spam_idx])
        ham_prob = float(probabilities[ham_idx])
        
        st.markdown("---")
        st.subheader("Analysis Result")
        
        # Display result based on calibrated thresholds
        if spam_prob >= 0.50:
            st.error(f"🚨 **Likely Spam / Scam** (Risk: {spam_prob * 100:.1f}%)")
            st.progress(spam_prob)
        elif spam_prob >= 0.30:
            st.warning(f"⚠️ **Suspicious / Moderate Risk** (Spam Score: {spam_prob * 100:.1f}%)")
            st.progress(spam_prob)
            st.caption("This message contains patterns or vocabulary frequently associated with spam or smishing attempts.")
        else:
            st.success(f"✅ **Likely Legitimate** (Confidence: {ham_prob * 100:.1f}%)")
            st.progress(spam_prob)
            
        col_ham, col_spam = st.columns(2)
        col_ham.metric("Legitimate Probability", f"{ham_prob * 100:.1f}%")
        col_spam.metric("Spam Probability", f"{spam_prob * 100:.1f}%")
        
        # Check if words were in vocabulary
        if text_vec.nnz == 0:
            st.info("ℹ️ *Notice: None of the words in this message were found in the training vocabulary. The prediction is based on baseline priors.*")
    else:
        st.warning("Please enter a message to analyze.")
