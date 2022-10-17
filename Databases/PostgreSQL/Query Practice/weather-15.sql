-- https://www.hackerrank.com/challenges/weather-observation-station-15

SELECT CAST(long_w AS DECIMAL(32, 4))
  FROM station
  WHERE lat_n < 137.2345
  ORDER BY lat_n DESC
  LIMIT 1;