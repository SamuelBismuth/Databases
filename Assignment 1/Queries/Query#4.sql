# The return must be the name of the client.
# For each of them, employee (which handle the command) and the shipper have 's' as first leter of their name.
# We also need to add the sum of the command.

SELECT Cust.ContactName, SUM(OrdDet.Quantity * OrdDet.UnitPrice - OrdDet.Discount * (OrdDet.UnitPrice * OrdDet.Quantity)) AS total

FROM Orders Ord

INNER JOIN `Order Details` OrdDet
ON Ord.OrderID = OrdDet.OrderId

INNER JOIN Customers Cust
ON Ord.CustomerID = Cust.CustomerID

LEFT OUTER JOIN Shippers Ship
ON Ord.ShipVia = Ship.ShipperID 

WHERE 

Ord.EmployeeID IN (
SELECT EmployeeID 
FROM Employees 
WHERE FirstName
LIKE 's%')

AND

Ord.ShipVia IN (
SELECT ShipperID 
FROM Shippers
WHERE CompanyName
LIKE 's%')

group by ContactName;


