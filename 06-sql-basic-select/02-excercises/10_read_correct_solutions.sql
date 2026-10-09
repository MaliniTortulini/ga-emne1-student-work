-- Oppgave 10: Les og rett spørringer
-- Oppgave 10.1 Tegn har forsvunnet

-- Spørringen skal hente både bynavn og folketall.
-- SELECT Name Population
-- FROM city
-- WHERE CountryCode = 'ITA';

SELECT Name, Population
FROM city
WHERE CountryCode = 'ITA';
-- første spørring: kun Population kom opp
-- la til komma mellom Name og Pop
-- Oppgave løst


-- Oppgave 10.2 Tekstverdier
-- Spørringen skal hente navn og folketall for byer i Italia. Forklar forskjellen på et kolonnenavn og en tekstverdi.
    -- Et kolonnenavn forteller hvilken informasjon som finnes i kolonnen, mens en tekstverdi er selve informasjonen som er lagret i kolonnen
-- SELECT Name, Population
-- FROM city
-- WHERE CountryCode = ITA;

SELECT Name, Population
FROM city
WHERE CountryCode = 'ITA';
-- første spørring: [42S22][1054] Unknown column 'ITA' in 'where clause'
-- lagt til '' rundt ITA
-- Oppgaven løst


-- Oppgave 10.3 Hvilke byer slipper gjennom
-- Målet er å finne byer i Egypt eller Marokko med mer enn én million innbyggere.
-- Forklar hvilke egyptiske byer den opprinnelige spørringen tillater, og hvorfor den rettede spørringen stiller samme folketallskrav til begge landene.
-- SELECT Name, CountryCode, Population
-- FROM city
-- WHERE CountryCode = 'EGY'
   -- OR CountryCode = 'MAR' AND Population > 1000000;

SELECT Name, CountryCode, Population
FROM city
WHERE (CountryCode = 'EGY'
    OR CountryCode = 'MAR')
  AND Population > 1000000;
-- første spørring: land i egypt viser innbyggertall under 1 000 000
-- la til () rundt begge CountryCode
-- oppgave løst
-- Forklaring: Den første spørringen henter alle byer fra Epypt, også de med under 1 000 000
-- innbyggere, fordi AND behandles før OR. Ved å sette paranteser rundt landekodene gjelder folketallskravet
-- for både Egypt og Marokko

-- Oppgave 10.4 Tomt resultat betyr ikke alltid riktige betingelser
-- Spørringen skal finne land uten registrert statsoverhode. Rett betingelsen og forklar hvorfor det ikke er nok å
-- kontrollere at koden kjører uten feilmelding.
-- SELECT Name, HeadOfState
-- FROM country
-- WHERE HeadOfState = NULL;

SELECT Name, HeadOfState
FROM country
WHERE HeadOfState IS NULL;
-- første spørring: ingenting kommer opp
-- byttet = NULL med IS NULL
-- oppgave løst
-- Forklaring: I SQL kan du ikke bruke vanlig likhetssammenligning for å undersøke om en veri er NULL.
-- Resultatet blir UNKNOWN, ikke TRUE. WHERE tar bare med rader der bertingelsen er TRUE, derfor får man ingen resultater.
-- Du får ingen feilmelding for det ikke er en feil som typefeil ovs.. Du får bare resultatet UNKNOWN, som er et svar.