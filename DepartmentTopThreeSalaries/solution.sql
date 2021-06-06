WITH res AS (
    SELECT
        d.Name AS 'Department',
        e.Name AS 'Employee',
        e.Salary AS 'Salary',
        DENSE_RANK() OVER ( PARTITION BY e.DepartmentId
                            ORDER BY e.Salary DESC  
                          ) AS subres
    FROM Employee e
    LEFT JOIN Department d
    ON e.DepartmentId = d.Id
)

SELECT Department, Employee, Salary
FROM res
WHERE subres <= 3
