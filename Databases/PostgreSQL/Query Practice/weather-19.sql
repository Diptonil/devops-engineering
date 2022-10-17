-- https://www.hackerrank.com/challenges/weather-observation-station-19/

SELECT CAST(SQRT(POWER(MAX(lat_n) - MIN(lat_n), 2) + POWER(MAX(long_w) - MIN(long_w), 2)) AS DECIMAL(32, 4))
  FROM station;