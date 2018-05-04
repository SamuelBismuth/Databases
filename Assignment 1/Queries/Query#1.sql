SELECT CompanyName, City
FROM Suppliers
WHERE SupplierID IN (SELECT SupplierID 
FROM Products
WHERE CategoryID = (SELECT CategoryID
FROM Categories
WHERE CategoryName = 'Confections'
))