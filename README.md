# Data Quality & Validation Script - Python

## Project Overview

This repository hosts a Python script designed to perform essential data quality and validation checks on tabular datasets (specifically CSV files). This project demonstrates foundational data engineering practices aimed at ensuring data integrity and reliability, crucial for any data-driven application or analytics pipeline.

## Why This Script is Useful

In real-world data engineering scenarios, data often arrives with inconsistencies, missing values, or duplicates. This script provides an automated way to:

* **Ensure Data Integrity:** By identifying common data quality issues such as missing values and duplicate records.
* **Provide Data Insights:** Offers a quick overview of the dataset's structure, data types, and basic statistics.
* **Support Upstream Processes:** Clean and validated data is vital for reliable analytics, machine learning model training, and reporting.

[cite_start]This aligns with my experience in automating daily reconciliation and quality checks [cite: 35] [cite_start]and developing validation and anomaly detection logic[cite: 58].

## Features

* Loads data from a specified CSV file using `pandas`.
* Reports the shape (number of rows and columns) of the dataset.
* Identifies and counts missing values per column.
* Detects and quantifies duplicate rows.
* Displays data types of each column.
* Provides basic descriptive statistics for numerical and categorical columns.

## Technologies Used

* **Python:** The core programming language for the script.
* **Pandas:** A powerful Python library used for data manipulation and analysis.

## How to Run the Script

To run this script on your local machine, follow these steps:

### 1. Prerequisites

Make sure you have Python installed (version 3.7 or higher recommended).
You also need to install the `pandas` library. If you don't have it, open your terminal or command prompt and run:

```bash
pip install pandas
