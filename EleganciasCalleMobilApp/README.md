# Elegancias Calle ERP: Inventory & Financial Management System

## 📌 Project Overview
This project represents a complete **Digital Transformation** initiative for a traditional garment rental business. The primary objective was to migrate the company's operations from vulnerable, manual paper notebook ledgers to a robust, automated digital ecosystem. 

Built with Python and Flet, this desktop/mobile application centralizes inventory tracking, financial flows, and customer management into a single intuitive interface.

*Note: The source code for this repository is kept private to protect proprietary business logic and branding. However, a full demonstration and architectural breakdown are provided below.*

## 🎥 Video Demonstration
Watch the system in action (UI, workflows, and dashboard):

https://github.com/user-attachments/assets/df26134a-64ca-4e56-93db-c9606b001441

## 🛠️ Tech Stack
* **Frontend (UI/UX):** `Flet` (Python)
* **Backend & Database:** `Python`, `SQLite`
* **Data Processing & Validation:** `Regular Expressions (Regex)`

## 🧠 System Architecture & Key Implementations

### 1. Relational Database Management (SQLite)
The core of the application is a localized, highly optimized SQLite database designed to handle the complete lifecycle of a garment. I engineered specific relational tables and queries to manage:
* **Rentals & Sales:** Tracking outgoing inventory, associating garments with specific clients, and registering financial transactions.
* **Returns & Reception:** Updating inventory availability in real-time upon item return.
* **Data Export Pipeline:** Built an automated export module that extracts transactional data into structured formats (CSV/Excel). This is crucial for bridging software development with Data Science, allowing for post-processing and detailed exploratory data analysis (EDA) of seasonal trends and revenue.

### 2. UI/UX Color-Coded Status System
To facilitate quick decision-making for non-technical staff, I implemented a dynamic, visual status indicator system using specific color codes:
* 🟢 **Green:** Garment is currently available in the store or successfully returned.
* 🔴 **Red:** Garment is currently rented out or pending return.
* ⚫ **Black:** Specific inventory statuses (e.g., sold, under maintenance, or inactive).
This UI logic directly queries the database and updates the frontend instantly, drastically reducing human error during peak business hours.

### 3. Business Intelligence Dashboard
Migrating from a physical notebook to a digital database unlocked the ability to track KPIs. I integrated a descriptive dashboard within the app that visualizes:
* Daily and monthly cash flows.
* Inventory rotation metrics (identifying top-performing vs. underperforming assets).

### 4. Data Validation (Regex)
To ensure the integrity of the database, I designed robust data entry pipelines using custom Regex patterns. This prevents staff from inputting invalid alphanumeric garment codes, replacing manual syntax errors with automated backend checks.

---
*“True digital transformation is not just about writing code; it’s about understanding the business process and designing a system that makes the user's daily work faster, safer, and measurable.”*
