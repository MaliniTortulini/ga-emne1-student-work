-- Oppgave 6: Sortering og avgrensning
-- Oppgave 6.1 Land i alfabetisk rekkefølge
SELECT *
FROM country;

SELECT Name, Region
FROM country
WHERE Continent = 'Asia'
ORDER BY Region ASC;

SELECT Name, Region
FROM country
WHERE Continent = 'Asia'
ORDER BY Region;
-- Disse to er like da ASC er standard om man ikke skriver noe

-- Oppgave 6.2 De største landene etter areal
SELECT Name, SurfaceArea
FROM country
ORDER BY SurfaceArea DESC, Code ASC
LIMIT 8;

-- Oppgave 6.3 Sortering på flere kolonner
-- Distrikt er alfabetisk, hvis flere byer ligger i samme distrikt, sorter dem etter folketall
-- og til slutt har to byer i samme distrikt likt folketall, sorter dem etter ID fra lavest til høyest
SELECT Name, District, Population
FROM city
WHERE CountryCode = 'CAN'
ORDER BY District ASC, Population DESC, ID ASC;

-- Oppgave 6.4 Fem vilkårlige eller fem bestemte
SELECT Code, Name
FROM country
LIMIT 5;

SELECT Code, Name
FROM country
ORDER BY Name ASC
LIMIT 5;
-- Den første spørringen garanterer ikke hvilke land jeg får fordi jeg ikke er spesifik i det jeg vil ha
-- Derfor velger LIMIT de 5 første den finner fra tabellen