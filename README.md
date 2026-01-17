# Automated Crypto Market ETL Pipeline
**A Production-Grade Data Engineering Project**

## System Overview
This repository features a fully automated **ETL (Extract, Transform, Load)** pipeline designed to monitor cryptocurrency market volatility. The system is engineered to run 24/7 without manual intervention, demonstrating proficiency in API integration, data cleaning, and CI/CD automation.

### Key Technical Features
* **Modular Architecture:** Divided into independent scripts for Data Extraction (`data_fetcher.py`), Transformation (`data_processor.py`), and Orchestration (`main.py`) for maximum maintainability.
* **Automated Data Persistence:** The system archives live market data into a time-series CSV database every hour, growing by 24 records daily.
* **Resilient Engineering:** Integrated `try-except` blocks and timeout management to handle API rate limits and network instability gracefully.
* **CI/CD Orchestration:** Powered by **GitHub Actions**, utilizing cron-scheduling to manage cloud-based execution and automated Git commits.

---

## Live Data Preview
This project maintains a live history of market movements. Below is a preview of the automatically generated dataset:

![Market Data Screenshot](data_preview.png)

---

## Project Structure
* `data_fetcher.py`: Handles REST API communication and raw data ingestion.
* `data_processor.py`: Cleans JSON payloads and transforms them into structured Pandas DataFrames.
* `main.py`: The central orchestrator managing the end-to-end ETL flow.
* `.github/workflows/main.yml`: The automation script defining the hourly cloud execution.

---

## ⚙️ How to Run Locally
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Execute the orchestrator: `python main.py`
