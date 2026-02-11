# Customer Lifecycle Analytics

## 📌 Project Overview
Customer churn is a major challenge for subscription-based and service-driven
businesses. This project focuses on analyzing customer lifecycle data to
identify churn patterns, key retention drivers, and customer lifetime trends.

The project goes beyond basic exploratory analysis by incorporating
feature engineering, churn prediction modeling, churn risk segmentation,
and customer lifetime value (CLV) analysis to support data-driven
retention strategies.

---

## 🎯 Business Objectives
- Identify patterns and drivers of customer churn
- Understand customer behavior across demographic, financial, and engagement factors
- Predict customer churn risk using machine learning
- Estimate customer lifetime value (CLV)
- Prioritize customers for retention based on risk and value
- Translate analytics insights into actionable business recommendations

---

## 🧰 Tools & Technologies
- **Python**
- **Pandas, NumPy** – data manipulation and analysis
- **Matplotlib, Seaborn** – data visualization
- **Scikit-learn** – churn prediction modeling
- **Jupyter Notebook** – exploratory analysis and modeling
- **Streamlit** (optional extension) – interactive dashboard
- **Git & GitHub** – version control

---

## 📂 Dataset Description
The dataset represents customer-level information from a banking /
subscription-style business. It includes demographic, financial,
behavioral, and engagement-related attributes.

### Key Columns
- `creditscore`, `age`, `tenure`, `balance`, `estimatedsalary`
- `geography`, `gender`, `card_type`
- `numofproducts`, `has_credit_card`, `is_active_member`
- `complain`, `satisfaction_score`
- `churn` (target variable: 1 = exited, 0 = retained)

The dataset enables both behavioral churn analysis and lifecycle-based
segmentation.

---

## 📁 Project Structure
customer-lifecycle-analytics/
│
├── data/
│ ├── raw/
│ │ └── customer_churn_raw.csv
│ └── processed/
│ ├── customer_churn_clean.csv
│ ├── customer_churn_features.csv
│ ├── customer_churn_scored.csv
│ └── customer_lifecycle_final.csv
│
├── notebooks/
│ ├── 01_data_understanding.ipynb
│ ├── 02_exploratory_analysis.ipynb
│ ├── 03_feature_engineering.ipynb
│ ├── 04_churn_modeling.ipynb
│ └── 05_clv_analysis.ipynb
│
├── models/
│ └── churn_model.pkl
│
├── dashboard/
│ └── app.py
│
├── requirements.txt
└── README.md





---

## 📊 Analysis Workflow

### 1️⃣ Data Understanding
- Reviewed dataset structure and data types
- Validated churn target variable
- Identified numerical and categorical features
- Ensured data quality before analysis

### 2️⃣ Exploratory Data Analysis (EDA)
- Analyzed overall churn rate
- Studied churn patterns by geography, gender, age, tenure, and balance
- Evaluated engagement indicators such as activity status, complaints, and satisfaction
- Identified early signs of churn risk

### 3️⃣ Feature Engineering
- Created tenure and age segments
- Engineered engagement and satisfaction-based features
- Added behavioral churn risk indicators
- Prepared a modeling-ready dataset

### 4️⃣ Churn Prediction Modeling
- Encoded categorical variables
- Trained a logistic regression model
- Evaluated performance using precision, recall, and ROC–AUC
- Generated churn probability scores
- Segmented customers into churn risk groups

### 5️⃣ Customer Lifetime Value (CLV) Analysis
- Estimated CLV using balance and income-based proxies
- Compared CLV across churn and risk segments
- Identified high-risk, high-value customers
- Built a retention prioritization framework

---

## 🔍 Key Insights
- Customers with shorter tenure are more likely to churn
- Inactive members and customers with complaints show higher churn risk
- Low satisfaction scores strongly correlate with churn
- A small segment of customers contributes a large share of lifetime value
- High-risk, high-CLV customers represent the greatest revenue leakage

---

## 💡 Business Recommendations
- Proactively target high-risk, high-value customers with personalized retention offers
- Improve onboarding and engagement for early-tenure customers
- Monitor satisfaction and complaints as early churn signals
- Allocate retention resources based on both churn risk and customer value
- Integrate churn probability into regular customer monitoring systems

---

## 🎓 Skills Demonstrated
- Data cleaning and preparation
- Exploratory data analysis (EDA)
- Feature engineering
- Predictive modeling (classification)
- Model evaluation and interpretation
- Customer lifetime value analysis
- Business-driven decision making
- Structured project organization

---

## 📌 Conclusion
This project demonstrates an end-to-end customer lifecycle analytics
workflow, transforming raw customer data into predictive insights and
actionable retention strategies. It reflects intermediate-level data
analytics and machine learning skills aligned with real-world business
use cases.

---

## 🚀 Future Enhancements
- Deploy interactive Streamlit dashboard
- Experiment with advanced models (Random Forest, XGBoost)
- Add time-based churn analysis if historical data is available
- Integrate model predictions into a live monitoring system
