CREATE TABLE dbo.dim_stocks(
    stock_key INT NOT NULL,
    ticker VARCHAR(10) NOT NULL,
    created_date DATETIME2(6)
);