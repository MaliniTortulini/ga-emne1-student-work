-- Oppgave 4: Filtrer rader med WHERE
-- Oppgave 4.1 Byer i Japan
SELECT Name, District, Population
From city
WHERE CountryCode = 'JPN';

-- Oppgave 4.2 Søramerikanske land
SELECT Name, Population
FROM country
WHERE Continent = 'South America';

-- Oppgave 4.3 Små land etter areal
SELECT Name, SurfaceArea
FROM country
WHERE SurfaceArea < 10000;

SELECT Name, SurfaceArea
FROM country
WHERE SurfaceArea = 10000;
-- Forskjellen på < og <= er at < kun skal finne dem som er mindre og <= skal finne dem som er lik OG mindre

-- Oppgave 4.4 Et annet distrikt
SELECT Name, CountryCode, District
FROM city
WHERE District <> 'California'
-- Denne spørrringen henter mer enn amerikanske byer fordi vi ikke har filtrert på Countrycode
-- for å se på landet USA. Derfor ser vi alle byer i land uten om byer fra California distriktet