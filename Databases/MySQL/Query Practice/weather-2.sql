-- https://www.hackerrank.com/challenges/weather-observation-station-2/

SELECT CAST(SUM(lat_n) AS DECIMAL(32, 2)), 
       CAST(SUM(long_w) AS DECIMAL(32, 2))
  FROM station;