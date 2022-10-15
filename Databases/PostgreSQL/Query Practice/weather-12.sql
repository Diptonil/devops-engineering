-- https://www.hackerrank.com/challenges/weather-observation-station-12/

SELECT DISTINCT city
  FROM station
  WHERE LEFT(city, 1) NOT IN ('A', 'E', 'I', 'O', 'U') AND
        RIGHT(city, 1) NOT IN ('a', 'e', 'i', 'o', 'u');