-- Hent alle kolonner fra tabellen city
-- ; semikolon avslutter SQL setningen
SELECT *
FROM city;

-- Velg kolonne du trenger
SELECT Name, Population
FROM city;

-- WHERE: velg bestemte rader
SELECT Name, Population
FROM city
WHERE CountryCode = 'NOR';

-- Sammenlikning av tall
-- tall skrives uten anførselstegn
SELECT Name, Population
FROM city
WHERE Population > 1000000;

-- Oppgave 1: finn svenske byer
SELECT *
From city
WHERE CountryCode = 'SWE';

-- Flere betingelser: AND og OR
-- To krav samtidig
SELECT Name, Population
From city
WHERE CountryCode = 'NOR'
  AND Population > 200000;

-- Flere betingeser, noen må oppfylles
SELECT Name, Population
FROM city
WHERE (CountryCode = 'NOR'
           OR CountryCode = 'SWE')
  AND Population > 200000;

-- ORDER BY sorterer resultatet
-- ASC (ascending) betyr synkende rekkefølge. Standard når retning ikke er oppgitt
-- DESC (descending) betyr synkende rekkefølge
-- Uten order by har vi ingen garanti for hvilken rekkefølge dataene vises
SELECT Name, Population
FROM city
WHERE CountryCode = 'NOR'
ORDER BY Population DESC;

-- LIMIT et begrenset antall rader
SELECT Name, Population
FROM city
ORDER BY  Population DESC, ID ASC
LIMIT 5;

-- Oppgave 2: store byer i Sverige
SELECT Name, Population
FROM city
WHERE CountryCode = 'SWE'
    AND Population > 100000
ORDER BY Population DESC;

-- LIKE søke etter mønster
-- Land som begynner på N, ikke n. (Case sensitiv)
-- % betyr null eller flere tegn
-- _ betyr nøyaktig ettt tegn
-- N% betyr at navnet begynner på N
-- %land% finner alle navn som inneholdet "land"
SELECT Name
FROM country
WHERE Name LIKE 'N%'
ORDER BY Name;

-- IN en av flere verdier
-- IN sjekker at verdien finnes i listen
SELECT Name, Population
FROM city
WHERE CountryCode IN
      ('NOR', 'SWE', 'DNK')
ORDER BY CountryCode, Name;

-- NULL når en verdi mangler
-- Ikke det samme som 0 eller tom tekst
-- Bruk IS NULL, ikke = NULL
-- IS NOT NULL finner radene der en verdi er registrert
SELECT Name, IndepYear
FROM country
WHERE IndepYear IS NULL;

-- COUNT() hvor mange rader?
-- COUNT(*) teller radene som oppfyller betingelsen
-- Uten WHERE teller vi alle radene i tabellen
-- AS ("alias") gir resultatkolonnen et alias (nytt navn når den vises, den endrer ikke kolonnenavnet)
SELECT COUNT(*) AS CityCount
FROM city
WHERE CountryCode = 'NOR';

-- Oppgave 3: tell land i Europa
SELECT COUNT(*) AS CountryCount
From country
WHERE Continent = 'Europe'
  AND Population > 5000000;