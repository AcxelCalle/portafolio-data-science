# Applied Data Science & Computer Vision Portfolio

This repository contains end-to-end projects focused on machine learning, database management, and computer vision. It demonstrates the practical application of programming and statistical modeling to solve real-world operational challenges.

## Project Index

### 1. E-Commerce Predictive Analytics & Machine Learning (UNI Project)
* **Tech Stack:** Python, Pandas, SQL, Scikit-Learn, XAI.
* **Description:** An end-to-end data pipeline for an e-commerce platform, scaling from Exploratory Data Analysis (EDA) to classification modeling and business strategy formulation, developed during advanced technical training at UNI.
* **Key Implementations:**
  * **Machine Learning & Tuning:** Trained and evaluated classification models (Random Forest, Logistic Regression) utilizing cross-validation and dynamic decision threshold adjustments to optimize predictive performance.
  * **Explainable AI (XAI):** Implemented interpretability techniques to decode the algorithms' decision-making processes at both global (feature importance) and local (individual predictions) levels.
  * **Business Strategy:** Translated XAI insights, combined with EDA and structured SQL queries, into actionable conclusions and strategic recommendations to improve the e-commerce platform's operations.

### 2. [Elegancias Calle ERP Mobil App] Custom Inventory & Financial Management System
* **Tech Stack:** Python, Flet (UI/UX), SQLite, Regular Expressions (Regex).
* **Description:** A tailored mobile application designed to optimize the inventory and financial tracking of a garment rental business.
* **Key Implementations:**
  * **Data Validation & Cleaning:** Designed robust data entry pipelines using custom Regex patterns to validate alpha-numeric garment codes, replacing manual errors with automated syntax checks.
  * **Relational Database Design:** Structured a localized SQLite database with optimized queries to handle real-time inventory availability, rental histories, and financial balances.
  * **Business Intelligence:** Built a descriptive financial dashboard within the app to monitor cash flow and item rotation KPIs.
* *Note: The source code is private due to proprietary business logic, but a full video demonstration is available in the project folder.*

### 3. RobotFace: Real-Time Computer Vision Tracking
* **Tech Stack:** Python, OpenCV, NumPy.
* **Description:** A computer vision application featuring a digital robot interface that actively detects and tracks human facial coordinates in real time.
* **Key Implementations:**
  * Implementation of cascade classifiers for face detection.
  * Optimization of frame processing pipelines to ensure low-latency responsiveness.

### 4. [Credit Risk Analytics] Credit Risk Assessment & Portfolio Quality
* **Tech Stack:** Power BI, Python (Pandas, Seaborn), DAX, Data Cleaning.
* **Description:** An interactive, end-to-end dashboard designed to evaluate the financial health of a loan portfolio, calculate banking risk metrics, and demographically profile defaulting customers. 
* **Key Implementations:**
  * **Python Embedded Visuals:** Integrated Python scripts directly within the Power BI engine to overcome native visual limitations, generating advanced statistical charts (KDE Probability Density and Hexbins) to model the continuous relationship between income, age, and loan amounts.
  * **Financial KPIs (DAX):** Computed critical banking sector indicators, including the NPL Ratio (Non-Performing Loans - 24.69%) and the total monetary Exposure at Default (S/ 77.1M).
  * **ETL & Data Transformation:** Pre-processed and cleaned the raw dataset using Python to ensure data integrity prior to ingestion into Power BI's relational model.
* *[View Interactive Power BI Dashboard](https://app.powerbi.com/reportEmbed?reportId=02178b67-7ac1-4925-b006-a99bab9cc089&autoAuth=true&ctid=717b9a79-1b91-41ab-a6f7-a579b46a9b41&actionBarEnabled=true)*
