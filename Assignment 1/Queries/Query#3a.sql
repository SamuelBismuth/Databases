ALTER TABLE Products ADD COLUMN shortPrice CHAR(6) AS (CONCAT('$', UnitPrice));
SELECT ProductID, ProductName, UnitPrice, shortPrice
FROM Products;