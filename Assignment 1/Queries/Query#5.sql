# This query suscribe for all suppliers the product which have been buy the most number of time by the client in the month ‫‪07.1996‬‬
# And who much money client buy it.

SELECT 

CompanyName,
ProductName, 
MAX(orderedCount) as `Ordered count`,
SUM(Quantity * UnitPrice - Discount * (UnitPrice * Quantity)) as `Total price`

FROM (

	SELECT
    
    sup.CompanyName, 
    pro.ProductName, 
    COUNT(ord.CustomerID) as orderedCount,
    ordDet.Quantity,
    ordDet.UnitPrice,
    ordDet.Discount
    
	FROM 
    
    Products AS pro
	INNER JOIN `Order Details` AS ordDet ON  pro.ProductID = ordDet.ProductID
	INNER JOIN Orders AS ord ON ordDet.OrderID = ord.OrderID 
	INNER JOIN Suppliers AS sup ON sup.SupplierID = pro.SupplierID

	WHERE 

	ord.OrderDate BETWEEN '1996-07-00' AND '1996-07-31'

	GROUP BY ordDet.ProductID
    
) AS subQuery

GROUP BY CompanyName