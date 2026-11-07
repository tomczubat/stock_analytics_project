CREATE TABLE dbo.fact_daily_performance(
    date DATE NOT NULL,
    stock_key INT NOT NULL,
    open_price DECIMAL(18,4),
    high_price DECIMAL(18,4),
    low_price DECIMAL(18,4),
    close_price DECIMAL(18,4),
    volume BIGINT,
    previous_close DECIMAL(18,4),
    daily_return_pct DECIMAL(18,6),
    daily_change DECIMAL(18,4)
);