-- https://www.hackerrank.com/challenges/earnings-of-employees/

SELECT MAX(salary * months), COUNT(name)
  FROM employee
  WHERE (salary * months) = (SELECT MAX(salary * months)
                               FROM employee);