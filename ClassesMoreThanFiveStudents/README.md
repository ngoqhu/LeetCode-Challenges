## Big Countries
---------
| Status | Accepted |
| --- | --- |
| Difficulty | Easy |
| Runtime | 233ms (faster than 93.8% of other mysql submissions) |
| Submissions | 286k |
| Accepted | 117.3k |

There is a table `courses` with columns: *student* and *class*.

Please list out all classes which have more than or equal to 5 students.

For example, the table:

```
+---------+------------+
| student | class      |
+---------+------------+
| A       | Math       |
| B       | English    |
| C       | Math       |
| D       | Biology    |
| E       | Math       |
| F       | Computer   |
| G       | Math       |
| H       | Math       |
| I       | Math       |
+---------+------------+
```
Should output:

```
+---------+
| class   |
+---------+
| Math    |
+---------+
```

**Note:**
The students should not be counted duplicate in each course.
