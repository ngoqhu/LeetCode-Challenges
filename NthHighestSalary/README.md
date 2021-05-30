## Nth Highest Salary
---------
| Status | Accepted |
| --- | --- |
| Difficulty | Medium |
| Runtime | 425ms (faster than 20.48% of other mysql submissions) |
| Submissions | 491k |
| Accepted | 166k |

Write a SQL query to get the n<sup>th</sup> highest salary from the `Employee` table.

```
+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
```
For example, given the above Employee table, the n<sup>th</sup> highest salary where `n = 2` is `200`. If there is no n<sup>th</sup> highest salary, then the query should return `null.`

```
+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| 200                    |
+------------------------+
```
