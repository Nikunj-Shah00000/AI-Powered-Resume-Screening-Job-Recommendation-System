# AI-Powered-Resume-Screening-Job-Recommendation-System

# AI-Powered Resume Screening & Job Recommendation System

## ML Bubble 2026 – Machine Learning Awareness & Skill Building Challenge

### Overview

The **AI-Powered Resume Screening & Job Recommendation System** is a Machine Learning application that automates resume classification based on textual content. It uses Natural Language Processing (NLP) techniques and a supervised machine learning model to classify resumes into different job categories.

The project aims to reduce manual effort in recruitment by automatically identifying the most suitable job domain for a candidate based on their resume.

---

## Problem Statement

Recruiters often receive hundreds or thousands of resumes for a single job opening. Manual screening is time-consuming, inconsistent, and prone to human error.

This project provides an intelligent solution that:

* Automatically analyzes resume text
* Predicts the most suitable job category
* Helps recruiters shortlist candidates faster
* Improves hiring efficiency

---

## Objectives

* Build an automated resume classification system
* Apply Natural Language Processing techniques
* Train a machine learning model for prediction
* Evaluate model performance using standard metrics
* Develop a simple web interface using Streamlit

---

## Technologies Used

| Technology   | Purpose                     |
| ------------ | --------------------------- |
| Python       | Programming Language        |
| Pandas       | Data Processing             |
| NumPy        | Numerical Computing         |
| Scikit-learn | Machine Learning            |
| NLTK         | Natural Language Processing |
| Matplotlib   | Data Visualization          |
| Seaborn      | Visualization               |
| Joblib       | Model Serialization         |
| Streamlit    | Web Application             |
| Git & GitHub | Version Control             |

---

## Machine Learning Pipeline

1. Load Resume Dataset
2. Clean Resume Text
3. Remove Stopwords
4. TF-IDF Feature Extraction
5. Train Logistic Regression Model
6. Evaluate Model
7. Save Trained Model
8. Deploy Using Streamlit

---

## Project Structure

```text
ML_Bubble_2026/
│
├── app.py
├── train.py
├── predict.py
├── preprocess.py
├── requirements.txt
├── dataset/
├── model/
├── results/
├── report/
├── presentation/
└── README.md
```

---

## Dataset

The project uses a publicly available Resume Dataset containing resumes categorized into multiple job roles.

Example categories include:

* Data Science
* HR
* Java Developer
* Testing
* DevOps
* Python Developer
* Business Analyst
* Web Designing
* Mechanical Engineer
* Electrical Engineer

---

## Machine Learning Model

**Algorithm**

* Logistic Regression

**Feature Extraction**

* TF-IDF Vectorizer

---

## Evaluation Metrics

The model is evaluated using:

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix

The generated reports are stored in the `results/` directory.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/ML_Bubble_2026.git
```

Navigate to the project directory:

```bash
cd ML_Bubble_2026
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Download the NLTK resources:

```bash
python download_nltk.py
```

Train the model:

```bash
python train.py
```

Generate evaluation reports:

```bash
python evaluate.py
```

Run the application:

```bash
streamlit run app.py
```

---

## Screenshots

Add screenshots of:

* Home Page
* Resume Input Screen
* Prediction Result
* Confusion Matrix
* Classification Report

---

## Future Improvements

* Resume ranking based on job descriptions
* Skill extraction using Named Entity Recognition (NER)
* Support for PDF and DOCX resume uploads
* Deep learning models (BERT/RoBERTa)
* Cloud deployment
* Explainable AI techniques for prediction interpretation

---

## Author

**ML_Nerds**

Department of Computer Science

ML Bubble 2026 Submission

---

## License

This project is intended for academic and educational purposes.
