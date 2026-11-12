-- Oppgave 6 Endre tabellstrukturen
-- Oppgave 6.1 Legg til en status
ALTER TABLE animals
ADD COLUMN status VARCHAR(20) NOT NULL DEFAULT 'new';

INSERT INTO animals(name, species, area_id)
VALUES ('Nova', 'cat', '1');
-- vekt og innkomstdato får null, mens status får new


-- Oppgave 6.2 Endre standardverdien
ALTER TABLE animals
MODIFY COLUMN status VARCHAR(20) NOT NULL DEFAULT 'available';

INSERT INTO animals(name, species, weight, area_id)
VALUES ('Oreo', 'cat', '5.5', '1');
-- her ble status available, mens de andre før er new

-- Oppgave 6.3 Gi navnefeltene mer plass
ALTER TABLE animals
MODIFY COLUMN name VARCHAR(60) NOT NULL;

SELECT *
FROM animals;

--  Forskjellen på ATLER TABLE og UPDATE er at ALTER TABLE endrer struktruen på selve tabellen,
-- i mens UPDATE endrer dataen inni tabellen
-- kolonnedefinisjonen endres av ALTER og verdiene i en eller flere rader er UPDATE


-- Oppgave 6.4 Fjern en kolonne og en tabell
CREATE TABLE scratch_lables(
    id INT AUTO_INCREMENT PRIMARY KEY,
    label VARCHAR(40)
);

INSERT INTO scratch_lables(label)
VALUES ('Temporary label');

SELECT *
FROM scratch_lables;

ALTER TABLE scratch_lables
DROP COLUMN label;
-- kun id 1 står igjen

DROP TABLE scratch_lables;
-- [42S02][1146] Table 'animal_center.scratch_lables' doesn't exist

-- Forskjellen på de to operasjonene er at den ene sletter en hel kolonne og
-- den andre sletter en hel tabell med alle kolonnene og radene

SELECT *
FROM scratch_lables;



-- Oppgave 7 Oppdater bestemte rader
-- Oppgave 7.1 To dyr med samme navn
-- Luna the cat = ID 1
UPDATE animals
SET weight = 3.90
WHERE id = 1;
-- Jeg brukte id for å finne spesifikt den Luna jeg skulle endre
-- hadde jeg brukt name i stedet for id så hadde jeg endra begge dyrene som heter Luna, men kaninen Luna veier ikke 3.90

-- Oppgave 7.2 To endringer i en setning
UPDATE animals
SET name = 'Rex Jr', weight = 19.20
WHERE id = 3;

-- Oppgave 7.3 Flytt et dyr
-- Kaninen Luna = ID 6
-- Quiet zone = ID 4
UPDATE animals
SET area_id = 4
WHERE id = 6;
-- Jeg endrer fremmednøkkelen i stedet for avdelingsnavnet fordi hvert dyr er koblet til rommet med FK
-- Avdelingsnavnet er ikke koblet til dyr

-- Oppgave 7.4 En kjent verdi blir ukjent igjen
UPDATE animals
SET weight = 14.60
WHERE id = 4;

UPDATE animals
SET weight = NULL
WHERE id = 4;

SELECT *
FROM animals
WHERE weight IS NULL;
-- Forskjellen på NULL og 0 i vekt kolonnen er at 0 er 0kg og null er at vi ikke vet vekten enda eller at den ikke er registrert
    -- weight = NULL er feil fordi vi skal ikke gi verdien NULL, vi skal beskrive at vi ikke har data IS NULL

-- En UPDATE uten WHERE påvirker alle radene fordi du ikke spesifiserer hvilken rad du ønsker å endre, så
-- den antar du da mener alle.



-- Oppgave 8 Slett data i rikig rekkefølge
-- Opggave 8.1 Fjern en testregistrering
DELETE FROM animals
WHERE id = 10;

-- Oppgave 8.2 En avdeling er fortsatt i bruk
SELECT *
FROM areas
WHERE name = 'Small animals';
-- id 3

DELETE FROM areas
WHERE id = 3;
-- [23000][1451] Cannot delete or update a parent row: a foreign key constraint fails (`animal_center`.`animals`, CONSTRAINT `animals_ibfk_1` FOREIGN KEY (`area_id`) REFERENCES `areas` (`id`))
-- det er fortsatt et dyr i small animals avdelingen, den må flyttes til an annen avdeling før bygningen rives

UPDATE animals
SET area_id = 4
WHERE id = 5;
-- nå som Pip er flyttet kan avdelingen slettes
DELETE FROM areas
WHERE id = 3;

-- Oppgave 8.3 Kontroller sluttresultatet
SELECT *
FROM animals
WHERE area_id = 4;
-- 2 kaniner

SELECT *
FROM animals;
-- 7 dyr

SELECT *
FROM areas;
-- 3 avdelinger

-- DELETE fjerner ikke hele tabellen da dens jobb er å slette rader
-- DROP TABLE passer ikke når målet er å bare slette Oreo fordi Oreo er en rad i en hel tabell



-- Oppgave 9 Les en modell som allerede finnes
-- Oppgave 9.1 Primærnøkler med andre navn
-- Primærnøkelen til country er Code og countrylanguage har countryCode og Language som primærnøkler
-- countryLanguage har en sammensatt primærnøkkel
-- En språkverdi alene er ikke nok til å identifisere en rad i countryLanguage fordi, et land kan ha flere språk

-- Oppgave 9.2
-- Flere språkrader kan ha samme countryCode fordi, et land kan ha flere språk. Dette er det samme med animal_shelter tabellen
-- Flere dyr kan ha samme area_id fordi, flere dyr kan være i samme avdeling


-- Oppgave 10 Les og rett SQL
-- Oppgave 10.1 Komma og paranteser
-- CREATE TABLE scratch_tags (
-- id INT AUTO_INCREMENT,
-- label VARCHAR(30) NOT NULL
-- PRIMARY KEY (id),
-- );

-- Det skal være komma mellom definisjoner slik at programmet vet når en definisjon starter og slutter
-- det skal ikke være et komma etter den siste definisjonen
CREATE TABLE scratch_tags (
id INT AUTO_INCREMENT,
label VARCHAR(30) NOT NULL,
PRIMARY KEY (id)
);

-- Oppgave 10.2 Kolonner og verdier
-- INSERT INTO animals (name, species, area_id)
-- VALUES ('Tyra', 'cat');

INSERT INTO animals (name, species, area_id)
VALUES ('Tyra', 'cat', 1);

-- Oppgave 10.3 Gyldig SQL med feil utvalg
-- UPDATE animals
-- SET weight = 2.50
-- WHERE name = 'Luna';
-- Vi må bruke id'en til kaninen Luna. Med name endrer vi alle dyr som heter Luna

-- Oppgave 10.4 Sletting er ikke en SELECT
-- DELETE * FROM animals
-- WHERE name = 'Nova';
SELECT *
FROM animals
WHERE name = 'Nova';

DELETE
FROM animals
WHERE id = 8;