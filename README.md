# 🛡️ AI Scam Message Detector

A simple Machine Learning project that classifies SMS messages as **Spam** or **Legitimate** using Python.

## 🌐 Live Demo

🔗 **Try the Live Application:** [https://ai-scam-message-detector.streamlit.app/](https://ai-scam-message-detector.streamlit.app/)

---

## 🚀 Project Overview

This project demonstrates the complete ML workflow:

- Dataset loading and exploration
- Data cleaning and visualization
- TF-IDF text feature extraction
- Model training using Multinomial Naive Bayes
- Evaluation using accuracy, precision, recall, and F1-score
- Saving the trained model
- Building a Streamlit web application

## 🧰 Tech Stack

- Python
- Pandas
- Matplotlib
- Scikit-learn
- Joblib
- Streamlit

## 📂 Project Structure

```text
ai-scam-message-detector/
├── .gitignore
├── AI Scam Message Detector.ipynb
├── SMSSpamCollection
├── app.py
├── requirements.txt
├── spam_model.pkl
├── tfidf.pkl
└── README.md
```

## ⚙️ Run Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the app:

```bash
streamlit run app.py
```

## 🧠 How It Works

1. SMS messages are converted into numerical features using TF-IDF.
2. A Multinomial Naive Bayes classifier learns from labelled examples.
3. The trained model predicts whether a new message resembles spam or legitimate SMS.

## ⚠️ Disclaimer

This is an educational project. Predictions may be incorrect and should not be used as the sole basis for deciding whether a message is safe.

## 👨‍💻 Author

Built by [@vaibhavv-labs](https://github.com/vaibhavv-labs) as a hands-on Machine Learning project.
