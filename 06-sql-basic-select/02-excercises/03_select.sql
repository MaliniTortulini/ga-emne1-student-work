-- Oppgave 3: Velg kolonner med SELECT
-- Oppgave 3.1: Utforsk tabellen
SELECT *
FROM country;
-- Code betyr landekode
-- Name betyr navn på landet
-- Continent betyr hvilket kontinent landet tilhører
-- Population inneholder antall mennesker som bor i landet

-- Oppgave 3.2: En kort landoversikt
SELECT Code, Name, Continent
FROM country;

SELECT Name, Code, Continent
FROM country;

-- Oppgave 3.3: Andre opplysninger om byene
SELECT Name, CountryCode, District
From city;
