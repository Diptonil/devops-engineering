-- https://www.hackerrank.com/challenges/weather-observation-station-3

SELECT DISTINCT city
  FROM station
  WHERE id % 2 = 0;