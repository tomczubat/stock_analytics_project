CREATE OR ALTER VIEW dbo.vw_stock_reporting
AS
SELECT 
    date,
    YEAR(date) AS year,
    MONTH(date) AS month,
    DATEPART(MONTH, date) AS month_num,
    DATEPART(QUARTER, date) AS quarter,
    ticker,
    open_price,
    high_price,
    low_price,
    close_price,
    volume

FROM dbo.fact_daily_performance