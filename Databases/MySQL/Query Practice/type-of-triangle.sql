-- https://www.hackerrank.com/challenges/what-type-of-triangle

SELECT
  CASE
    WHEN A = B AND B = C AND A + B > C AND A + C > B AND B + C > A
      THEN "Equilateral"
    WHEN (A = B OR A = C OR B = C) AND A + B > C AND A + C > B AND B + C > A
      THEN "Isosceles"
    WHEN A + B <= C OR A + C <= B OR B + C <= A
      THEN "Not A Triangle"
    ELSE "Scalene"
  END AS text
  FROM triangles;