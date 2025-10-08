# customer-lifetime-value-project
# End-to-End Customer Segmentation & CLV Prediction Dashboard

## 📊 Project Overview

This project is an end-to-end data science project focused on analyzing customer behavior for an e-commerce business. The primary goal is to segment customers based on their purchasing history using RFM analysis and to predict their future value (Customer Lifetime Value - CLV). All insights are presented in a fully interactive web dashboard built with Streamlit.

---

## ✨ Key Features

- **RFM Customer Segmentation:** Categorizes customers into distinct, actionable segments like 'Loyal', 'At-Risk', and 'Warm Leads'.
- **Predictive Modeling:** Utilizes an XGBoost model to predict a customer's spending over the next 90 days.
- **Interactive Dashboard:** A user-friendly web application that allows business users to visualize segment distributions, analyze segment characteristics, and filter the customer database.

---

## 🛠️ Tech Stack

- **Programming Language:** Python
- **Data Manipulation:** Pandas, NumPy
- **Machine Learning:** Scikit-learn, XGBoost
- **Data Visualization:** Plotly, Matplotlib, Seaborn
- **Web Application:** Streamlit

---

## 📈 Key Insights

- **"Monetary is King":** A customer's total past spending is the single most powerful predictor of their future value.
- **High-Value, At-Risk Segment Identified:** Discovered a crucial "Shouldn't Lose" segment of previously high-value customers who are now inactive, representing the most critical group for reactivation campaigns.

---

## 🖼️ Dashboard Preview

<img width="1910" height="955" alt="image" src="https://github.com/user-attachments/assets/a9d29004-1ddd-4a4b-a2f6-30f3a244b489" />


---

## 🚀 How to Run the Project

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Guythong/customer-lifetime-value-project.git](https://github.com/Guythong/customer-lifetime-value-project.git)
    cd customer-lifetime-value-project
    ```
2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run the Streamlit app:**
    ```bash
    streamlit run app.py
    ```
