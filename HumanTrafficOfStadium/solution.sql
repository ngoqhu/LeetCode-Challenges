# Write your MySQL query statement below
WITH subQ AS (
    SELECT
        s1.id AS id1,
        s2.id AS id2,
        s3.id AS id3
    FROM Stadium s1
        JOIN Stadium s2 ON s1.id + 1 = s2.id
        JOIN Stadium s3 ON s1.id + 2 = s3.id
    WHERE
        s1.people >= 100
        AND s2.people >= 100
        AND s3.people >= 100
)

SELECT *
FROM Stadium
WHERE id IN (SELECT id1 FROM subQ)
    OR id IN (SELECT id2 FROM subQ)
    OR id IN (SELECT id3 FROM subQ)
    
