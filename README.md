# 🏦 Customer Churn Prediction Dashboard

An interactive Machine Learning project that predicts customer churn using a Random Forest model and provides a business intelligence dashboard built with Streamlit.

---

## 📌 Project Overview

This project analyzes banking customer data to predict churn and understand key factors driving customer retention or exit. It combines machine learning with an interactive dashboard to support business decision-making.

The system helps:
- Identify customers at risk of leaving
- Understand behavioral patterns behind churn
- Provide actionable business insights through visual analytics

---

## 🎯 Problem Statement

Customer churn leads to significant revenue loss in financial institutions. The goal is to build a predictive system that identifies customers likely to churn so that retention strategies can be applied in advance.

---

## 📊 Dataset Information

- Dataset: European Bank Customer Dataset  
- Target Variable: `Exited` (1 = Churn, 0 = Retained)

### Features Used

**Core Features:**
- CreditScore
- Age
- Tenure
- Balance
- NumOfProducts
- HasCrCard
- IsActiveMember
- EstimatedSalary

**Encoded Features:**
- Geography_Germany
- Geography_Spain
- Gender_Male

**Engineered Features:**
- Balance_Salary_Ratio
- Product_Density
- Age_Tenure_Interaction

---

## ⚙️ Tech Stack

- Python
- Pandas, NumPy
- Scikit-learn (Random Forest)
- Streamlit (Web App)
- Plotly (Interactive Visualizations)

---

## 🧠 Machine Learning Workflow

### 1. Data Preprocessing
- Handling missing values
- Encoding categorical variables
- Converting boolean features to numeric format

### 2. Feature Engineering
- Balance-to-salary ratio
- Product usage density
- Age-tenure interaction

### 3. Model Training
- Random Forest Classifier
- Trained on structured banking dataset

### 4. Evaluation Metrics
- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC

---

## 📈 Dashboard Features

### 🔮 Churn Prediction
- Real-time customer churn prediction
- Probability score output
- Risk classification (Low / Medium / High)

### 📊 Business Analytics
- Age vs churn distribution
- Balance vs churn analysis
- Salary vs churn behavior
- Product usage impact
- Geography-based churn trends

### 🧠 Insights Engine
- Automatically generated business insights based on dataset trends

### 📉 Visualizations
- Interactive Plotly charts
- Risk gauge meter
- Feature importance ranking

---

## 🖥️ Application Interface

- Sidebar input panel for customer data entry
- Interactive filters for dataset exploration
- Real-time prediction output
- Dynamic charts and KPIs
- Business intelligence section

---

## 📁 Project Structure
hurn-dashboard/
│
├── app.py
├── rf_model.pkl
├── model_columns.pkl
├── European_Bank.csv
├── requirements.txt
└── README.md

---

## 🚀 Installation & Setup

### 1. Clone Repository
```bash
git clone https://github.com/your-username/churn-dashboard.git
cd churn-dashboard
pip install -r requirements.txt
streamlit run app.py

## 📈 Dashboard Features

- Real-time customer churn prediction using a Random Forest model
- Churn probability score with risk classification (Low, Medium, High)
- Interactive customer input panel for instant predictions
- Churn risk gauge visualization for quick decision-making
- Age vs Churn analysis to identify vulnerable customer segments
- Balance vs Churn analysis to understand financial behavior patterns
- Salary vs Churn visualization for income-based insights
- Product usage analysis to evaluate customer engagement
- Geography-based churn comparison across customer groups
- Feature importance visualization to identify key churn drivers
- Interactive filters for customized data exploration

---

## 📊 Key Business Insights

- Customers aged 40+ show a higher tendency to churn compared to younger customers.
- Lower product adoption is strongly associated with increased churn risk.
- Customers with higher account balances exhibit greater sensitivity to churn.
- Inactive members are significantly more likely to leave the bank.
- Customer location plays an important role in churn behavior and retention patterns.
- Customer engagement metrics provide stronger predictive power than salary-related factors.
- Retained customers generally demonstrate higher levels of product usage and activity.

---

## 💼 Business Impact

This solution enables banks to:

- Identify high-risk customers before they churn.
- Improve customer retention through targeted intervention strategies.
- Optimize marketing and customer engagement campaigns.
- Reduce revenue loss associated with customer attrition.
- Support data-driven decision-making using predictive analytics.
- Prioritize retention efforts toward the most valuable customer segments.
- Enhance overall customer lifetime value and profitability.
- Transform customer data into actionable business intelligence.

## 👨‍💻 Author

**Jiya**


