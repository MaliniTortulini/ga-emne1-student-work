-- Database ("schema"): En organisert samling av data som kan lagres, hentes og behandles
-- DBMS (Database Management System): Programvaren som brukes til å opprette, lagre og administrere databaser. MySQL er et eksempel
-- SQL: Et språk som brukes til å hente, legge til, endre og slette data i relasjonsdatabaser.
-- Tabell: En tabell samler informasjon om et bestemt tema i rader og kolonner
-- Rad: En rad inneholder informasjon om en bestemt registrering, for eksempel en by
-- Kolonne: Beskriver en egenskap som navn eller folketall. Hver kolonne har en datatype
-- Nøkler: Nøkler brukes til å identifisere rader og opprette forbindelser mellom tabeller. En primærnøkkel identifiserer hver rad unikt

-- Hvorfor følger resultatet i kolonnerekkefølgen spørringen?:
    -- Fordi SQL viser kolonner i den rekkefølgen du har skrevet dem i SELECT
-- Hvorfor endrer ikke SELECT tabellen?
    -- Fordi du henter informasjon, du "leser", du endrer eller skriver ikke på tabellen

-- Datagrip: Programmet hvor jeg skriver og kjører SQL-spørringene
-- Docker: Kjører MySQL i en container
-- MYSQL - DBMS: Håndterer databasen
-- world - Database: city, country, countrylanguage (tabellene)

-- SELECT *: Henter all data fra tabellen du velger med FROM
-- Retrieves all columns from the selected table
SELECT *
FROM city;

-- SELECT utvalgt kolonne, utvalgt kolonne: Velger kun dataen fra kolonnen/kolonnene fra tabellen du har valgt
-- Retrieves only the specified columns
SELECT Name, Population
FROM city;

-- Tabell city:
-- Kolonne Name: inneholder navn på byer i ulike land
-- CountryCode: inneholder en lanedekode med 3 bokstaver som viser hvilket land byen tilhører
-- District: inneholder hvilket distrikt/fylke byen holder til
-- Population: inneholder hvor mange som bor i hver by

-- Datatyper:
-- Id: INT
-- Name: VARCHAR
-- Population: INT
-- Navn og folketall trenger forskjellige datatyper fordi den ene inneholder tall og den andre tekst. For å hjelpe med å ikke
   -- krysse disse typene bruker man datatyper for å holde dem avskilt.

-- Primærnøkkel
-- city: her er primærnøkkelen ID
    -- Bynavnet kan ikke være en ID da flere byer rundt i verden heter det samme.
-- country: her er primærnøkkelen code

-- Fremmednøkkel
-- city.CountryCode er landekoden til landet byen ligger i. country.Code er den samme koden. MEN i country brukes denne som en primær,
-- fordi hvert land har en unik kode. Hvert land har mange byer og fordi disse ligger i samme land vil de dele koden. Derfor legges tabbelnavnet
-- og kolonnenavnet i city. Dette gjør at man skal kunne lett se koblingen mellom land og by i tabellene. På grunn av at hver rad skal kunne identifiseres
-- så kan ikke CountryCode brukes i by da mange har samme landekode. En ID blir derfor brukt som en unik nøkkel.
