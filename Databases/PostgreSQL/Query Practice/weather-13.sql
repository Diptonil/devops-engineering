-- https://www.hackerrank.com/challenges/weather-observation-station-13/

SELECT CAST(SUM(lat_n) AS DECIMAL(32, 4))
  FROM station
  WHERE lat_n > 38.7880 AND lat_n < 137.2345;