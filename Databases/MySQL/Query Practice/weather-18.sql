-- https://www.hackerrank.com/challenges/weather-observation-station-18/

SELECT CAST((MAX(lat_n) - MIN(lat_n) + MAX(long_w) - MIN(long_w)) AS DECIMAL(32, 4))
  FROM station;