-- Oppgave 1 Land i tre regioner
SELECT Name, Region, Population, SurfaceArea
FROM country
WHERE (Region = 'Caribbean'
   OR Region = 'Polynesia'
   OR Region = 'Micronesia')
  AND Population >= 100000
  AND SurfaceArea < 10000
ORDER BY Region ASC, Population DESC, CODE ASC;

SELECT COUNT(*) AS SmallRegionCount
FROM country
WHERE (Region = 'Caribbean'
    OR Region = 'Polynesia'
    OR Region = 'Micronesia')
  AND Population >= 100000
  AND SurfaceArea < 10000;
-- Jeg kontrollerer at begge spøøringene bruker de samme WHERE-betingelsene
-- Den første viser landende, mens den andre teller dem med COUNT(*).
-- Jeg sammenligner antall rader fra den første spørringen med resultatet fra COUNT(*)
-- for å kontrollere at de stemmer


-- Oppgave 2 Offisielle språk
SELECT *
FROM countrylanguage;

SELECT CountryCode, Language, Percentage
FROM countrylanguage
WHERE CountryCode = 'IND'
  AND IsOfficial = 'T'
ORDER BY Percentage DESC, Language ASC;

SELECT CountryCode, Percentage
FROM countrylanguage
WHERE Language = 'Spanish'
  AND IsOfficial = 'T'
ORDER BY Percentage DESC;

SELECT COUNT(*) AS SpanishSpeakingCountries
FROM countrylanguage
WHERE Language = 'Spanish'
  AND IsOfficial = 'T';
-- Generelt antall rader i CountryLanguage er ikke det samme som antall land, fordi et land
-- kan ha flere språk


-- Oppgave 3 To forskjellige måter å telle på
SELECT COUNT(*) AS CountryCount
FROM country;

-- COUNT(kolonnenavn) teller bare radene der denne kolonnen har en verdi som ikke er NULL.
SELECT COUNT(LifeExpectancy) AS KnownLifeExpectancyCount
FROM country;
-- Forskjellen på * og kolonnenavn inni COUNT er at * betyr alle rader i country tabellen,
-- mens kolonnenavn betyr alle radene inni country, unntatt dem med NULL som data
-- Hvis jeg bytter ut LifeExpectancy med Code som er primærnøkkelen så får jeg likt antall
-- som * fordi primærnøkkelen skal aldri være NULL.


-- Oppgave 4 Undersøk like bynavn
SELECT ID, Name, CountryCode, District
FROM city
WHERE Name = 'San Jose'
ORDER BY CountryCode ASC, ID ASC;
-- Grunnen til at jeg kan se alle med samme navn og likevel identifisere en bestemt rad er på
-- grunn av ID. Jeg kan bruke ID for å hente den unike raden.

SELECT ID, Name, CountryCode, District
FROM city
WHERE ID = '859';


-- Oppgave 5 Et tomt utvalg
SELECT Name, Population
FROM city
ORDER BY Population DESC
LIMIT 1;

SELECT Name, Population
FROM city
WHERE Population > 10500000
ORDER BY Population DESC;

SELECT COUNT(*) AS HigherThanMombayCount
FROM city
WHERE Population > 10500000;
-- Den andre spørringen viser ingen rader fordi det ikke finnes data på at en by har flere innbyggere en Mombay
-- COUNT(*) viser en rad med 0 fordi dataen tilsier at det er 0, derfor er det en rad som viser at det er 0


-- Oppgave 6 Dine egene spørsmål
-- Vis CountryCode 'JPN'  med, hvor distriktet er fra Osaka, mer enn 70 000 innbyggere og 'NLD'
SELECT *
FROM city
WHERE CountryCode = 'NLD'
   OR (CountryCode = 'JPN'
   AND District = 'Osaka'
   AND Population > 70000);

-- Vis en by med 8 bokstaver og har a som første bokstav
SELECT *
FROM city
WHERE Name LIKE 'a_______';

-- vis en toppliste med byer som har fire bokstaver og størst antall innbyggere
SELECT *
FROM city
WHERE Name LIKE '____'
ORDER BY Population DESC
LIMIT 10;

-- Finn ut hvor mange språk det finnes
SELECT COUNT(*) AS LanguagesInTheWorldCount
FROM countrylanguage
WHERE IsOfficial = 'T';