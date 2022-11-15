-- https://www.hackerrank.com/challenges/weather-observation-station-14/

SELECT CAST(MAX(lat_n) AS DECIMAL(32, 4))
  FROM station
  WHERE lat_n < 137.2345;