-- Oppgave 5: Kombiner betingelser
-- Oppgave 5.1 Store brasilianske byer
SELECT Name, Population
FROM city
WHERE CountryCode = 'BRA'
   AND Population >= 500000;

-- Oppgave 5.2 Et intervall for folketall
SELECT Name, Population
FROM country
WHERE Population >= 2000000
  AND Population <= 8000000;

-- Oppgave 5.3 To land og ett felles krav
SELECT Name, CountryCode, Population
FROM city
WHERE (CountryCode = 'AUS' OR CountryCode = 'NZL')
  AND Population > 200000;
-- Her bruker jeg () rundt begge landene fordi da
-- må byen være fra Australia eller New Zealand, og uansett hvilket land den ligger i,
-- må den ha over 200 000 innbyggere.

-- Uten hadde jeg fått:
-- Alle byer fra Australia, uansett folketall
-- Bare byer fra New Zealand med over 200000 innbyggere