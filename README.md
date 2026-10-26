# Stock Analytics Data Engineering Project

## Overview

This project demonstrates a modern data engineering workflow using Python, PySpark, SQL, GitHub Actions, and Databricks. The pipeline ingests stock market data from external APIs, applies data quality checks and transformations, and produces analytics-ready datasets for reporting and visualization.

## Architecture

```text
Stock API
    |
    v
Bronze Layer (Raw Data)
    |
    v
Silver Layer (Cleaned & Validated Data)
    |
    v
Gold Layer (Business Metrics)
    |
    v
Power BI / Analytics
```

## Technologies

- Python
- PySpark
- SQL
- Delta Lake
- Git & GitHub
- GitHub Actions
- Databricks
- Azure Key Vault
- Great Expectations
- Power BI

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

## Folder Descriptions

| Folder | Purpose |
|----------|----------|
| `.github/workflows` | CI/CD pipelines for automated testing and deployment |
| `data/raw` | Raw stock API data before transformation |
| `data/processed` | Processed datasets for analysis |
| `src/ingestion` | API ingestion code |
| `src/transformations` | Silver-layer data cleansing and enrichment |
| `src/models` | Gold-layer business logic and analytics tables |
| `src/quality` | Data quality and validation checks |
| `src/utils` | Shared helper functions |
| `sql/silver` | SQL transformations for Silver layer |
| `sql/gold` | SQL transformations for Gold layer |
| `tests` | Unit and integration tests |

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

## Data Quality Checks

- Null values
- Duplicate records
- Invalid ticker symbols
- Missing trading dates
- Negative prices
- Schema drift

## CI/CD Pipeline

1. Runs unit tests
2. Executes Python linting
3. Executes SQL linting
4. Validates code formatting
5. Deploys approved code to Databricks

## Skills Demonstrated

- Data Ingestion
- API Integration
- PySpark Development
- SQL Development
- Data Modeling
- Data Quality Engineering
- Delta Lake
- Git Version Control
- CI/CD
- Databricks
- Azure Integration
- Power BI Reporting

## Future Enhancements

- Incremental loading
- Streaming market data
- Additional stock APIs
- Sentiment analysis from financial news
- Data observability dashboards
- Real-time analytics
