-- https://www.hackerrank.com/challenges/weather-observation-station-17

SELECT CAST(long_w AS DECIMAL(32, 4))
  FROM station
  WHERE lat_n > 38.7780
  ORDER BY lat_n ASC
  LIMIT 1;