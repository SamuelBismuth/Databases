SELECT productName, SupplierID
FROM Products
WHERE SupplierID IN (SELECT SupplierID
FROM Suppliers 
WHERE CompanyName IN ('Exotic Liquids', 'Grandma Kelly''s Homestead')
)