-- https://www.hackerrank.com/challenges/weather-observation-station-16/

SELECT CAST(lat_n AS DECIMAL(32, 4))
  FROM station
  WHERE lat_n > 38.7780
  ORDER BY lat_n ASC
  LIMIT 1;