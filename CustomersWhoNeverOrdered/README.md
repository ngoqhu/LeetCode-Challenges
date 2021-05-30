## Customers Who Never Ordered
---------
| Status | Accepted |
| --- | --- |
| Difficulty | Easy |
| Runtime | 448ms (faster than 55.98% of other mysql submissions) |
| Submissions | 405.6k |
| Accepted | 236k |

Suppose that a website contains two tables, the `Customers` table and the Orders table. Write a SQL query to find all customers who never order anything.

**Table: Customers.**
```
+----+-------+
| Id | Name  |
+----+-------+
| 1  | Joe   |
| 2  | Henry |
| 3  | Sam   |
| 4  | Max   |
+----+-------+
```

**Table: Orders**
```
+----+------------+
| Id | CustomerId |
+----+------------+
| 1  | 3          |
| 2  | 1          |
+----+------------+
```

Using the above tables as example, return the following:

```
+-----------+
| Customers |
+-----------+
| Henry     |
| Max       |
+-----------+
```
