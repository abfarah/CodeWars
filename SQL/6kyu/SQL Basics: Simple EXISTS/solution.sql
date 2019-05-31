SELECT id, name
FROM Departments
WHERE EXISTS (SELECT name  FROM Sales WHERE Sales.department_id = Departments.id AND price > 98);
