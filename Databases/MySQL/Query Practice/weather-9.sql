-- https://www.hackerrank.com/challenges/weather-observation-station-9/

SELECT DISTINCT city
  FROM station
  WHERE city NOT LIKE 'A%' AND
        city NOT LIKE 'E%' AND
        city NOT LIKE 'I%' AND
        city NOT LIKE 'O%' AND
        city NOT LIKE 'U%';