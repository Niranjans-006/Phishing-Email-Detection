# Phishing Email Detection Model

## 📌 Project Description

This project is a Machine Learning-based Phishing Email Detection System developed using Python and Scikit-learn. The model analyzes email text and classifies it as either **Phishing** or **Safe** using TF-IDF feature extraction and Logistic Regression.

---

## 🚀 Features

- Detects phishing and legitimate emails
- Email text preprocessing
- TF-IDF feature extraction
- Logistic Regression classification
- Displays model accuracy
- Generates confusion matrix
- Predicts custom email input

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Joblib

---

## 📂 Project Structure

```
Phishing-Email-Detection/
│
├── dataset/
│   └── phishing_email.csv
│
├── models/
│   ├── phishing_model.pkl
│   └── vectorizer.pkl
│
├── screenshots/
│   └── confusion_matrix.png
│
├── src/
│   ├── train.py
│   ├── predict.py
│   ├── preprocess.py
│   └── utils.py
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

Install the required libraries:

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

Run the application:

```bash
python app.py
```

Choose:

- **1** → Train Model
- **2** → Predict Email

---

## 📊 Model Workflow

1. Load the dataset
2. Clean email text
3. Convert text into TF-IDF features
4. Train Logistic Regression model
5. Evaluate accuracy
6. Generate confusion matrix
7. Save trained model
8. Predict new email

---

## 📈 Output

- Email Classification (Phishing / Safe)
- Accuracy Score
- Confusion Matrix
- Trained Model (.pkl)

---

## 🎯 Future Improvements

- Use a larger phishing email dataset
- Improve model accuracy
- Build a web interface using Streamlit
- Deploy the project online

---

## 👨‍💻 Developed By

**Niranjan S**

Computer Science and Engineering Student
