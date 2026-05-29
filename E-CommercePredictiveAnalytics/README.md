# E-Commerce Predictive Analytics & Strategy Formulation

* [ProyectoUNI.ipynb](https://nbviewer.org/github/AcxelCalle/portafolio-data-science/blob/main/E-CommercePredictiveAnalytics/ProyectoUNI.ipynb): The main Jupyter Notebook containing the full code, from data cleaning to model deployment and XAI visualizations.

## 📌 Project Overview
This project, developed as part of the advanced Data Science for Business specialization at the Universidad Nacional de Ingeniería (UNI), bridges the gap between raw transactional data and actionable corporate strategy. 

The primary objective was to build a robust end-to-end machine learning pipeline to predict customer behavior and, more importantly, decode those predictions using Explainable AI (XAI) to generate strategic business recommendations.

## 🛠️ Tech Stack & Tools
* **Data Processing:** `pandas`, `numpy` (Data wrangling).
* **Machine Learning:** `scikit-learn` (Random Forest, Logistic Regression).
* **Model Evaluation:** Cross-Validation, ROC-AUC, Dynamic Decision Threshold Adjustment.
* **Explainability (XAI):** Feature Importance, Local and Global Interpretability techniques.

## 🧠 Methodology & Pipeline

### 1. Data Structuring & EDA
* **Database Synchronization:** Extracted and consolidated datasets using SQL queries to map user behavior across the platform.
* **Exploratory Data Analysis (EDA):** Handled missing values, identified underlying distributions, and engineered features to capture purchasing patterns.

### 2. Predictive Modeling & Optimization
* Trained baseline and ensemble classification models (**Logistic Regression** and **Random Forest**).
* Applied **K-Fold Cross-Validation** to ensure the model's robustness and prevent overfitting.
* **Threshold Tuning:** Instead of relying on default probabilities (0.5), the decision threshold was mathematically adjusted to optimize the trade-off between precision and recall, aligning the algorithm with the specific financial goals of the business.

### 3. Explainable AI (XAI)
In corporate environments, a "black box" model is not enough. I applied XAI principles to understand exactly *why* the models made their decisions:
* **Global Interpretability:** Identified the macroeconomic variables and platform features that hold the most weight in overall user conversion.
* **Local Interpretability:** Analyzed specific individual predictions to understand why a particular user was classified as a high or low-probability buyer.

### 4. Business Strategy & Recommendations
The final phase translated mathematical outputs into business language. Based on the EDA and XAI findings, I formulated strategic recommendations to:
* Optimize targeted marketing campaigns.
* Improve platform retention plans.
* Reallocate resources towards the features that statistically drive the most value.

