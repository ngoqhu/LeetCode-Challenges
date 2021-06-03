# Write your MySQL query statement below
SELECT Score, dense_rank() OVER(ORDER BY Score DESC) AS `Rank`
FROM Scores
