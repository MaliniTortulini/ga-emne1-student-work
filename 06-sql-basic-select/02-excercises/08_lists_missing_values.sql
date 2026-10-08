-- Oppgave 8: Lister og manglende verdier
-- Oppgave 8.1 Tre land med IN
SELECT Name, CountryCode, Population
FROM city
WHERE CountryCode IN ('FRA', 'ESP', 'PRT')
  AND Population >= 300000
ORDER BY CountryCode, Name;

SELECT Name, CountryCode, Population
FROM city
WHERE (CountryCode = 'FRA'
    OR CountryCode = 'ESP'
    OR CountryCode = 'PRT')
  AND Population >= 300000
ORDER BY CountryCode, Name;

-- Oppgave 8.3 Manglende levealder
SELECT Name, LifeExpectancy
FROM country
WHERE LifeExpectancy IS NULL;
-- En mangelde verdi her betyr ikke at de kun blir 0 år, det betyr at vi ikke har
-- data om levealder i disse landene av ulike grunner

-- Oppgave 8.4 Registrert levealder
SELECT Name, LifeExpectancy
FROM country
WHERE LifeExpectancy IS NOT NULL
ORDER BY LifeExpectancy DESC, Code ASC
LIMIT 10;