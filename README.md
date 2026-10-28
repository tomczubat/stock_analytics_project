# Stock Analytics Data Engineering Project

## Overview

This project demonstrates a modern Microsoft data engineering workflow using Python, SQL, Microsoft Fabric, GitHub, and Power BI.

The solution ingests stock market data from external APIs, stores and processes the data using a Medallion Architecture (Bronze, Silver, and Gold layers), and delivers analytics-ready datasets for business intelligence and reporting.

The project follows industry-standard data engineering practices including source control, pull requests, data quality validation, dimensional modeling, and CI/CD automation.

---

## Architecture

```text
Yahoo Finance API
        |
        v
Python Ingestion
        |
        v
Fabric Lakehouse

Bronze Layer
(Raw Stock Data)
        |
        v

Silver Layer
(Validated & Cleansed Data)
        |
        v

Gold Layer
(Business Metrics)

        |
        v

Fabric Warehouse
(Fact & Dimension Tables)

        |
        v

Power BI Reports & Dashboards
```

---

## Technologies

- Python
- SQL
- Microsoft Fabric
- Fabric Lakehouse
- Fabric Data Warehouse
- Delta Tables
- Power BI
- Git
- GitHub
- GitHub Actions
- Azure Key Vault
- Great Expectations

---

## Project Goals

- Build a modern end-to-end analytics platform
- Demonstrate Medallion Architecture principles
- Implement data quality validation
- Develop dimensional data models
- Automate deployment through CI/CD
- Deliver business intelligence through Power BI
- Gain hands-on experience with Microsoft Fabric

---

## Project Structure

```text
stock_analytics_project/
│
├── .github/
│   └── workflows/
│       └── deploy.yml
│
├── data/
│   ├── raw/
│   └── processed/
│
├── src/
│   ├── ingestion/
│   ├── transformations/
│   ├── models/
│   ├── quality/
│   ├── utils/
│   └── main.py
│
├── sql/
│   ├── silver/
│   └── gold/
│
├── tests/
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Current Progress

### Completed

✅ Git repository initialization

✅ Virtual environment setup

✅ GitHub repository and branching strategy

✅ Pull request workflow

✅ Stock API ingestion using yfinance

✅ Bronze layer development

✅ Parquet-based raw data storage

### In Progress

⬜ Silver-layer transformations

⬜ Data quality validation

⬜ Gold-layer metric calculations

⬜ Fabric Lakehouse implementation

⬜ Fabric Warehouse implementation

⬜ Power BI dashboard development

⬜ GitHub Actions CI/CD deployment

---

## Data Model

### Fact Tables

- FactStockPrices
- FactDailyReturns
- FactTradingVolume

### Dimension Tables

- DimCompany
- DimDate
- DimSector
- DimExchange

---

## Data Quality Checks

The Silver layer will validate:

- Null values
- Duplicate records
- Invalid ticker symbols
- Missing trading dates
- Negative pricing values
- Invalid volume values
- Schema drift

---

## Medallion Architecture

### Bronze Layer

Stores raw stock market data exactly as received from source systems.

Example fields:

- Date
- Ticker
- Open
- High
- Low
- Close
- Volume

### Silver Layer

Performs data cleansing and validation:

- Remove duplicates
- Validate prices
- Validate volume
- Standardize schemas
- Handle missing values

### Gold Layer

Builds business-ready datasets:

- Daily returns
- Trading metrics
- Moving averages
- Historical performance trends
- Aggregated reporting datasets

---

## CI/CD Pipeline

GitHub Actions will automate:

1. Unit testing
2. Python linting
3. SQL linting
4. Code formatting validation
5. Deployment to Microsoft Fabric

---

## Skills Demonstrated

- Data Engineering
- Data Ingestion
- API Integration
- Python Development
- SQL Development
- Dimensional Modeling
- Data Quality Engineering
- Microsoft Fabric
- Lakehouse Architecture
- Data Warehouse Design
- Git Version Control
- Pull Request Workflow
- CI/CD
- Power BI Reporting

---

## Future Enhancements

- Incremental loading
- Additional market data providers
- Company fundamentals data
- Financial news sentiment analysis
- Fabric notebooks
- Fabric pipelines
- Real-time market data processing
- Data observability monitoring
- Automated data quality alerting