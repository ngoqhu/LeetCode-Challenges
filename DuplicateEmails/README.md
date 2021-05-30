## Duplicate Emails
---------
| Status | Accepted |
| --- | --- |
| Difficulty | Easy |
| Runtime | 286ms (faster than 98.44% of other mysql submissions) |
| Submissions | 374.7k |
| Accepted | 245.6k |

Write a SQL query to find all duplicate emails in a table named `Person`.

**Table: Person**
```
+----+---------+
| Id | Email   |
+----+---------+
| 1  | a@b.com |
| 2  | c@d.com |
| 3  | a@b.com |
+----+---------+
```

For example, your query should return the following for the above table:

```
+---------+
| Email   |
+---------+
| a@b.com |
+---------+
```

**Note:** All emails are in lowercase.
