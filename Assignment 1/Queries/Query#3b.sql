SELECT ProductID, ProductName, UnitPrice, CAST((CONCAT('$', UnitPrice)) AS CHAR(6)) AS 'shortPrice'
FROM Products;