-- https://leetcode.com/problems/duplicate-emails/

SELECT DISTINCT email
  FROM Person
  WHERE email IN (SELECT email
                   FROM Person
                   GROUP BY email
                   HAVING COUNT(email) > 1);