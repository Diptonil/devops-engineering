-- https://www.hackerrank.com/challenges/the-blunder/

SELECT CEIL(AVG(salary) - AVG(ROUND(REPLACE(salary, '0', ''))))
  FROM employees;