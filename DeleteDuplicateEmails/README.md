## Delete Duplicate Emals
---------
| Status | Accepted |
| --- | --- |
| Difficulty | Easy |
| Runtime | 1654ms (faster than 60.96% of other mysql submissions) |
| Submissions | 332.2k |
| Accepted | 155.4k |

Write a SQL query to **delete** all duplicate email entries in a table named `Person`, keeping only unique emails based on its smallest `Id`.

**Table: Person**
```
+----+------------------+
| Id | Email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
| 3  | john@example.com |
+----+------------------+
Id is the primary key column for this table.
```

For example, after running your query, the above `Person` table should have the following rows:
```
+----+------------------+
| Id | Email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
+----+------------------+
```
Note:
Your output is the whole `Person` table after executing your sql. Use delete statement.
