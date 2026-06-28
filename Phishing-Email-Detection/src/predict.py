import os
import joblib

from preprocess import clean_text

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "..", "models", "phishing_model.pkl")
VECTORIZER_PATH = os.path.join(BASE_DIR, "..", "models", "vectorizer.pkl")

if not os.path.exists(MODEL_PATH):
    print("❌ Model not found!")
    print("Please train the model first.")
    exit()

model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

print("========== PHISHING EMAIL DETECTOR ==========\n")

email = input("Paste Email Here:\n\n")

email = clean_text(email)

vector = vectorizer.transform([email])

prediction = model.predict(vector)

print("\nPrediction :", prediction[0].upper())