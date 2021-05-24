## Combine Two Tables
---------
| Status | Accepted |
| --- | --- |
| Difficulty | Medium |
| Runtime | 265ms (faster than 97.93% of other python submissions) |
| Memory usage | 0B (less than 100% of other python submissions) |
| Submissions | 569.8k |
| Accepted | 372.4k |

Write a SQL query for a report that provides the following information for each person in the Person table, regardless if there is an address for each of those people:
`FirstName, LastName, City, State`

**Table: Person**
```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| PersonId    | int     |
| FirstName   | varchar |
| LastName    | varchar |
+-------------+---------+
PersonId is the primary key column for this table.
```

**Table Address**
```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| AddressId   | int     |
| PersonId    | int     |
| City        | varchar |
| State       | varchar |
+-------------+---------+
AddressId is the primary key column for this table.
```
