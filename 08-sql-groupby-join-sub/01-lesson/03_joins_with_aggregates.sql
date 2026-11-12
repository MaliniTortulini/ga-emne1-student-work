-- 03 JOIN og GROUP BY sammen
SELECT country.Code, country.Name, COUNT(city.ID) AS city_count
FROM country
LEFT JOIN city
ON city.CountryCode = country.Code
GROUP BY country.Code, country.Name
ORDER BY  city_count DESC;

-- COALESCE
-- SUM ignorerer NULL, men gir NULL når ingen verdier kan summeres
-- COALESCE(verdi, 0) gir verdien hvis den finnes, hvis ikke 0
-- COUNT(kolonne) gir allerede 0 uten treff
SELECT country.Code, country.Name, COALESCE(SUM(city.Population), 0) AS sum_city_pop
FROM country
LEFT JOIN city
ON city.CountryCode = country.Code
GROUP BY country.Code, country.Name
ORDER BY sum_city_pop DESC;