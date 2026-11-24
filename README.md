# 🏥 MediBuddy – Medical Insurance Charges Prediction

## 📌 Project Overview

MediBuddy Medical Insurance Charges Prediction is a Machine Learning project developed to estimate medical insurance charges based on customer demographic, health, and lifestyle information.

The project analyzes customer information such as age, gender, BMI, smoking habits, number of children, and geographical region to predict estimated medical insurance expenses.

An interactive web application is developed using Streamlit, allowing users to enter customer details and obtain insurance charge predictions.

## 🎯 Project Objectives

- Analyze medical insurance customer data.
- Understand the relationship between customer characteristics and insurance charges.
- Perform Exploratory Data Analysis (EDA).
- Identify important factors influencing insurance expenses.
- Develop and evaluate multiple Machine Learning regression models.
- Perform hyperparameter tuning and model comparison.
- Select the best-performing prediction model.
- Build an interactive insurance prediction application using Streamlit.

## 📊 Dataset Information

The dataset contains 1,338 customer records.

### Input Features

| Feature | Description |
|---|---|
| Age | Age of the customer |
| Sex | Gender of the customer |
| BMI | Body Mass Index |
| Children | Number of dependent children |
| Smoker | Smoking status |
| Region | Customer geographical region |

### Target Variable

- `charges in INR` – Medical insurance charges.

## 🔍 Project Workflow

1. Data Collection and Understanding
2. Data Cleaning and Preprocessing
3. Exploratory Data Analysis (EDA)
4. Outlier Detection and Investigation
5. Categorical Feature Encoding
6. Feature Selection
7. Train-Test Split
8. Feature Scaling where required
9. Machine Learning Model Development
10. Model Evaluation and Comparison
11. Hyperparameter Tuning
12. Final Model Selection – XGBoost
13. Model Serialization using Joblib
14. Streamlit Web Application Development

## 🤖 Machine Learning Models

The project explores the following regression algorithms:

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- Gradient Boosting Regressor
- XGBoost Regressor

### 🏆 Best Performing Model: XGBoost Regressor

XGBoost Regressor was selected as the final model for predicting medical insurance charges based on the model evaluation results.

## 📈 Final Model Performance

| Evaluation Metric | Result |
|---|---:|
| R² Score | 86.54% |

The selected XGBoost model achieved an R² score of 86.54% on the test dataset.

## 💻 Streamlit Web Application

The project includes an interactive web application with four sections:

### 1. Dashboard
- Project overview
- Dataset information
- Selected Machine Learning model
- Model performance metrics

### 2. Insurance Prediction
- Enter customer information
- Select gender and smoking status
- Enter age, BMI, and number of children
- Select geographical region
- Generate estimated insurance charges

### 3. About Project
- Project objective
- Machine Learning workflow
- Algorithms used
- Model evaluation results

### 4. About Company
- MediBuddy company overview
- Healthcare services
- Company information

## 🛠️ Technologies Used

**Programming Language**
- Python

**Data Analysis**
- Pandas
- NumPy

**Data Visualization**
- Matplotlib
- Seaborn

**Machine Learning**
- Scikit-learn
- XGBoost

**Model Deployment**
- Streamlit
- Joblib

**Development Environment**
- Jupyter Notebook
- VS Code

## 📂 Project Structure

```text
MediBuddy-Medical-Insurance-Prediction/
│
├── app/
│   ├── app.py
│   ├── medibuddy_best_model.pkl
│   ├── requirements.txt
│   └── README.md
│
├── notebooks/
│   └── MediBuddy_Insurance_Analysis.ipynb
│
├── dataset/
│   └── insurance.csv
│
└── README.md
```

*Adjust the folder structure to match the files actually uploaded to your repository.*

## 🚀 How to Run the Project

### Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/MediBuddy.git
```

### Step 2: Navigate to the Project Folder

```bash
cd MediBuddy
```

### Step 3: Create a Virtual Environment

```bash
python -m venv .venv
```

### Step 4: Activate the Environment

Windows:

```bash
.venv\Scripts\activate
```

### Step 5: Install Dependencies

```bash
pip install -r app/requirements.txt
```

### Step 6: Run the Streamlit Application

```bash
cd app
streamlit run app.py
```

The application will open in your browser.

## 📌 Key Learning Outcomes

- Data cleaning and preprocessing
- Exploratory Data Analysis
- Feature engineering and categorical encoding
- Regression model development
- Model evaluation using MAE, RMSE, and R²
- Hyperparameter tuning
- XGBoost model development
- Model saving and loading using Joblib
- Building an interactive Streamlit application

## ⚠️ Disclaimer

This application provides Machine Learning-based estimated medical insurance charges for educational and demonstration purposes. Predictions are not actual insurance quotations or guaranteed policy premiums.

