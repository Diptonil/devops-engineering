-- https://www.hackerrank.com/challenges/japan-population/

SELECT SUM(population)
  FROM city
  WHERE countrycode = 'JPN';