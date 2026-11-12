-- 02_joins
-- INNER JOIN beholder bare par som gir treff
-- uten ON kombineres hver by med hvert land
SELECT country.name AS country_name, city.Name AS city_name
FROM city
INNER JOIN country
ON CountryCode = Code
WHERE Continent = 'Europe'
ORDER BY country.Name;

-- INNER JOIN, 3 tabeller
-- Landets Capital kobles til byens ID. Språkets CountryCode kobles til landets Code
-- Et land kan gi flere rader hvis flere språk er offisielle
SELECT country.Name AS country_name,
       city.Name AS city_name,
       countrylanguage.Language
FROM country
INNER JOIN city ON country.Capital = city.ID
INNER JOIN countrylanguage ON country.Code = countrylanguage.CountryCode
WHERE country.Continent = 'Europe'
AND countrylanguage.IsOfficial = 'T'
ORDER BY country_name ASC;

-- LEFT JOIN, Alt i country blir med og hvis en by ikke matcher blir verdien NULL
-- Alle rader fra venstre tabell beholdes
-- Ved manglende treff får kolonnene fra høyre tabell verdien NULL
SELECT country.Name AS country_name,
       city.Name AS city_name
FROM country
LEFT JOIN city ON city.CountryCode = country.Code
WHERE city.Name IS NULL
ORDER BY country_name;

-- RIGHT JOIN
SELECT country.Name AS country_name,
       city.Name AS city_name
FROM city
RIGHT JOIN world.country
    ON city.CountryCode = country.Code
ORDER BY country.Name, city.Name;


-- Oppgave land og hovedsteder
SELECT *
FROM country;

SELECT *
FROM city;

SELECT country.Name, city.Name AS capital
FROM country
LEFT JOIN city
ON country.Capital = city.ID
ORDER BY country.Name ASC;

-- Vanlig teknikk for å finne rader uten treff i høyre tabell
-- Land uten registrerte byer
SELECT country.Code, country.Name
FROM country
LEFT JOIN city
ON city.CountryCode = country.Code
WHERE city.ID IS NULL;

-- LEFT JOIN med betingelser
-- Behold land uten store byer
SELECT country.Name, city.Name
FROM country
LEFT JOIN city
ON city.CountryCode = country.Code
AND city.Population > 1000000
ORDER BY country.Name ASC;