# Credit Risk Assessment & Portfolio Quality Dashboard

## 📌 Project Overview
This project is an end-to-end Business Intelligence and Data Science solution applied to the financial sector. The primary objective was to analyze a massive credit history dataset to evaluate loan portfolio health, model default behavior, and identify high-risk demographic profiles.

The project stands out by bridging structured corporate data analysis (DAX) with advanced statistical modeling using Python embedded directly within Power BI.

* **Dataset:** [Credit Risk Assessment (Kaggle)](https://www.kaggle.com/datasets/urvishvekariya/credit-risk-assessment)
* **Interactive Dashboard:** [View Power BI Report](https://app.powerbi.com/reportEmbed?reportId=02178b67-7ac1-4925-b006-a99bab9cc089&autoAuth=true&ctid=717b9a79-1b91-41ab-a6f7-a579b46a9b41&actionBarEnabled=true)

## 🛠️ Tech Stack & Tools
* **Data Wrangling (ETL):** `Python` (Pandas).
* **Data Modeling & Financial Math:** `Power BI`, `DAX`.
* **Advanced Visualization:** Power BI Native Engine + `Python` Scripts (`Seaborn`, `Matplotlib`).

## 🧠 Architecture & Methodology

### 1. Data Cleaning (Python Data Wrangling)
Prior to loading the data into Power BI, Python was utilized for dataset preprocessing. This pipeline included handling null values, normalizing categorical variables (e.g., loan intent and home ownership), and treating statistical outliers that could skew income or loan averages.

### 2. Financial KPIs & Data Modeling (DAX)
The relational data model was structured to enable the dynamic calculation of critical corporate risk metrics:
* **NPL Ratio (Non-Performing Loans):** Monitoring the percentage of the portfolio currently in default (24.69%).
* **Exposure at Default (EAD):** Quantifying the actual financial impact (S/ 77.1M) against the total active portfolio (S/ 312.4M).
* **Average DTI (Debt-to-Income) Ratio:** Evaluating the client's repayment capacity and financial leverage.

### 3. Statistical Modeling (In-App Python)
To surpass Power BI's native graphical limitations regarding continuous data distributions, Python scripts were injected directly into the report canvas:
* **KDE (Kernel Density Estimate):** Generated topological contour maps to visualize the probability density concentration between *Annual Income* and *Age*, pinpointing the core target market cluster.
* **Hexbin Plots:** Utilized hexagonal binning to correlate *Loan Amount* with *Age*, mitigating the overplotting issues typical of massive scatter plots and revealing high-density transaction areas.

### 4. Default Demographic Profiling
The dashboard features cross-filtering capabilities to analyze how housing status (Rent, Mortgage, Own), credit history length, and assigned risk grades (A-G) directly impact a client's probability of default.

---
*This project demonstrates the ability to merge traditional corporate business intelligence with the quantitative rigor of statistical data science.*
