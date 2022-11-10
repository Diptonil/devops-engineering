-- https://www.hackerrank.com/challenges/african-cities/

SELECT City.name
  FROM City
  INNER JOIN Country ON City.CountryCode = Country.Code
  WHERE Country.Continent = 'Africa';