import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

import matplotlib.pyplot as plt
import seaborn as sns

from preprocess import clean_text

# -----------------------------
# Load Dataset
# -----------------------------
print("Loading Dataset...")

df = pd.read_csv("../dataset/phishing_email.csv")

print(df.head())

# -----------------------------
# Data Cleaning
# -----------------------------
df["EmailText"] = df["EmailText"].apply(clean_text)

# -----------------------------
# Feature Extraction (TF-IDF)
# -----------------------------
vectorizer = TfidfVectorizer(stop_words="english")

X = vectorizer.fit_transform(df["EmailText"])

y = df["Label"]

# -----------------------------
# Split Dataset
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# -----------------------------
# Train Model
# -----------------------------
print("\nTraining Model...")

model = LogisticRegression()

model.fit(X_train, y_train)

print("Training Completed!")

# -----------------------------
# Prediction
# -----------------------------
y_pred = model.predict(X_test)

# -----------------------------
# Accuracy
# -----------------------------
accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy :", round(accuracy * 100, 2), "%")

print("\nClassification Report\n")

print(classification_report(y_test, y_pred))

# -----------------------------
# Confusion Matrix
# -----------------------------
cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(6,5))

sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=["Phishing","Safe"],
    yticklabels=["Phishing","Safe"]
)

plt.title("Confusion Matrix")

plt.xlabel("Predicted")

plt.ylabel("Actual")

plt.savefig("../screenshots/confusion_matrix.png")

plt.show()

# -----------------------------
# -----------------------------
# Save Model
# -----------------------------
import os
import joblib

os.makedirs("../models", exist_ok=True)

joblib.dump(model, "../models/phishing_model.pkl")
joblib.dump(vectorizer, "../models/vectorizer.pkl")

print("================================")
print("Model Saved Successfully!")
print("================================")

# Save confusion matrix
plt.savefig("../screenshots/confusion_matrix.png")

# Close graph
plt.close()