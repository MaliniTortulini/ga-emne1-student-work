-- Oppgave 9: Tell rader med COUNT
-- Oppgave 9.1 Hvor mange byer og land
SELECT COUNT(*) AS CityCount
FROM city;

SELECT COUNT(*) AS CountryCount
FROM country;
-- Jeg får kun en resultatrad, selvom tabellen har mange rader, fordi COUNT(*)
-- teller alle radene og gir meg ett samlet resultat

-- Oppgave 9.2 Tell et filtrert utvalg
SELECT COUNT(*) AS LargeCityCount
FROM city
WHERE CountryCode = 'MEX'
  AND Population >= 500000;

SELECT Name, Population
FROM city
WHERE CountryCode = 'MEX'
  AND Population >= 500000;

-- Oppgave 9.3 Hvor mange verdier mangler
SELECT COUNT(*) AS LifeExpectancyCount
FROM country
WHERE LifeExpectancy IS NULL;
-- 17 land

SELECT COUNT(*) AS LifeExpectancyCount
FROM country
WHERE LifeExpectancy IS NOT NULL;
-- 222 land
-- 222 + 17 = 239 land

SELECT *
FROM country;
-- 239 land
-- Tallene stemmer fordi land uten data og land med blir til sammen 239 som er det samme som alle land til sammen