-- 01_aggregates
SELECT SUM(Population) AS total_population,
       AVG(Population) AS avg_population,
       MIN(Population) AS min_population,
       MAX(Population) AS max_population
FROM city
WHERE CountryCode = 'NOR';

-- " gir mulighet til mellomrom istedenfor _
-- AS er alias
SELECT Name, Population / 1000000 AS "pop millions"
FROM country
WHERE Population > 1000000
ORDER BY `pop millions` DESC;
-- LIMIT;
-- Heltall delt på heltall gir fortsatt desimaler i svaret

-- WHERE og HAVING
SELECT Continent, COUNT(*) AS country_count
FROM country
WHERE Population > 10000000
GROUP BY Continent
HAVING COUNT(*) >= 5
ORDER BY country_count ASC;

-- Oppgave: byer per landekode
SELECT *
FROM city;

SELECT CountryCode, COUNT(*) AS city_count, AVG(Population) AS average_population_countrycode
FROM city
GROUP BY CountryCode
HAVING COUNT(*) >= 20
ORDER BY average_population_countrycode DESC;


