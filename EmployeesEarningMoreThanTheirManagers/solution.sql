# Write your MySQL query statement below
SELECT A.Name AS Employee
FROM Employee AS A
INNER JOIN Employee AS B
ON A.ManagerId = B.Id
WHERE A.Salary > B.Salary
