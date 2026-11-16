CREATE TABLE dbo.fact_daily_performance (
    [date] DATE,
    ticker VARCHAR(10),
    open_price DECIMAL(18,4),
    high_price DECIMAL(18,4),
    low_price DECIMAL(18,4),
    close_price DECIMAL(18,4),
    volume BIGINT
);
