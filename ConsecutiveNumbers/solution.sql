# Write your MySQL query statement below
SELECT DISTINCT log1.Num AS ConsecutiveNums
FROM
    Logs log1,
    Logs log2,
    Logs log3
WHERE
    log1.Id = log2.Id - 1
    AND log2.Id = log3.Id - 1
    AND log1.Num = log2.Num
    AND log2.Num = log3.Num
