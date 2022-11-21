-- https://leetcode.com/problems/employees-earning-more-than-their-managers/

SELECT E1.name AS Employee
  FROM Employee E1
  INNER JOIN Employee E2 ON E1.managerId = E2.id
  WHERE E1.salary > E2.salary;