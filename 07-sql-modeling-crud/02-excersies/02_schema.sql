-- Oppgave 1 ER modell
-- En rad i areas-tabellen representerer en avdeling i dyresenteret
-- En rad i animales-tabellen representerer et dyr i dyresenteret

-- Jeg valgte VARCHAR til name og species fordi begge er tekst typer
-- weight_kg er DECIMAL i stedet for INT fordi kilo har ofte komma
-- Ukjent vekt skal registreres som NULL og ikke 0, fordi 0 ville vært verdien/kiloen 0
-- verdiene som må ha NOT NULL er area name, animals name, species og area_id, resten kan være NULL
-- area name må være UNIQUE

-- areas id er PK og animals
-- tabellen animals inneholder fremmednøkkelen area_id og den peker på id i areas
-- vi bør ikke lagre en liste over alle dyrenes ID-er i en kolonne i areas fordi vi lagrer avdelingen hos dyret

-- relasjonen sett fra en avdeling er en avdeling kan være tom, ha ett dyr eller flere
-- relasjonen sett fra et dyr er et dyr må være registrert til kun en avdeling av gangen
-- Kontroller spesielt at modellen tillater en tom avdeling, men ikke et dyr uten avdeling:
   -- Jeg gjør dette ved at relasjonen tillater 0:N dyr per avdeling. Du trenger ikke registrere et dyr for å opprette en avdeling
   -- men et dyr må ha en avdeling pga area_id INT NOT NULL


-- Oppgave 2 Grunnoppgaver
-- ER modell se bilde

-- Oppgave 3 Opprett databasen og tabellene
CREATE DATABASE IF NOT EXISTS animal_center;

USE animal_center;

SELECT DATABASE();

CREATE TABLE areas(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(40) NOT NULL UNIQUE
);

CREATE TABLE animals(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(40) NOT NULL,
    species VARCHAR(20) NOT NULL,
    weight DECIMAL(5,2),
    admitted_on DATE,
    area_id INT NOT NULL,
    FOREIGN KEY (area_id) REFERENCES areas(id)
);

-- Oppgave 3.4 Kontroller strukturen
-- areas må opprettes før animals fordi hvert dyr er koblet til en avdeling
-- begge kolonnene som inngår i fremmednøkkelforholdet må ha kompatible datatyper fordi de skal kunne sammenlignes og kobles sammen.


-- Oppgave 4 Legg inn og kontroller data
-- Oppgave 4.1 Registrer avdelingene
INSERT INTO areas(name)
VALUES ('Cat Wing');

INSERT INTO areas(name)
VALUES ('Dog Wing'),
       ('Small Animals'),
       ('Quiet Zone');

SELECT *
FROM areas;

-- Cat 1
-- Dog 2
-- Small 3
-- Quiet 4

-- Oppgave 4.2 Registrer dyrene
INSERT INTO animals(name, species, weight, admitted_on, area_id)
VALUES ('Luna', 'cat', 3.80, '2026-09-12', 1);

INSERT INTO animals(name, species, weight, admitted_on, area_id)
VALUES ('Milo', 'cat', 4.20, NULL, 1),
('Rex', 'dog', 18.50, '2026-09-15', 2),
('Nala', 'dog', NULL, '2026-09-17', 2),
('Pip', 'rabbit', 1.60, '2026-09-20', 3),
('Luna', 'rabbit', 2.10, NULL, 3);

SELECT *
FROM animals;

-- Oppgave 4.3 Finn bestemte rader
SELECT id, name, species, area_id
FROM animals
ORDER BY species ASC, id ASC;

SELECT id, name
FROM animals
WHERE name = 'Luna';
-- Jeg ser forskjell på dem ved at id'ene er forskjellig og i dette tilfelle en katt og en kanin

SELECT *
FROM animals
WHERE admitted_on IS NULL;

SELECT *
FROM animals
WHERE weight IS NULL;

-- Oppgave 4.4 Kontroller antall og plassering
SELECT COUNT(*) AS animals_count
FROM animals;
-- 6 dyr

SELECT COUNT(*) AS shelter_count
FROM areas;
-- 4 avdelinger

SELECT *
FROM areas
WHERE name = 'Quiet Zone';
-- id 4

SELECT *
FROM animals
WHERE area_id = 4;
-- 0 rows

SELECT *
FROM areas
WHERE name = 'Small animals';
-- id 3

SELECT *
FROM animals
WHERE area_id = 3;
-- 2 dyr, Pip og Luna i Small animals avdelingen


-- Oppgave 5 Prøv reglene i databasen
-- Oppgave 5.1 Et avdelingsnavn som finnes fra før
INSERT INTO areas(name)
VALUES ('Cat Wing');
-- [23000][1062] Duplicate entry 'Cat Wing' for key 'areas.name'

-- Oppgave 5.2 En obligatorisk verdi mangler
INSERT INTO animals(name, species, weight, admitted_on, area_id)
VALUES (NULL, 'dog', 3.0, '2026-10-15', '2');
-- [23000][1048] Column 'name' cannot be null
-- jeg kan ikke levere NULL i name fordi jeg har valgt NOT NULL når jeg laget tabellen

INSERT INTO animals(name, species, weight, admitted_on, area_id)
VALUES ('Kira', 'cat', 3.4, '2026-10-15', NULL);
-- [23000][1048] Column 'area_id' cannot be null
-- area_id kan ikke være NULL fordi jeg har valgt NOT NULL da jeg laget tabellen

-- Oppgave 5.3 En avdeling som ikke finnes
INSERT INTO animals(name, species, weight, admitted_on, area_id)
VALUES ('Kira', 'cat', 3.4, '2026-10-15', 8);
-- [23000][1452] Cannot add or update a child row: a foreign key constraint fails (`animal_center`.`animals`, CONSTRAINT `animals_ibfk_1` FOREIGN KEY (`area_id`) REFERENCES `areas` (`id`))
-- area_id funker ikke med 8 fordi vi prøver å sammenligne og koble mot en id i areas som ikke finnes

-- Oppgave 5.4 En ID som allerede er brukt
SELECT *
FROM animals;

INSERT INTO animals (id, name, species, weight, admitted_on, area_id)
VALUES (3, 'Molly', 'dog', '4.3', '2026-11-20', '2');
-- [23000][1062] Duplicate entry '3' for key 'animals.PRIMARY'
-- et dyr kan ha samme navn da jeg har valgt å ikke bruke UNIQUE på name under opprettelsen,
-- men et dyr med samme primærnøkkel gå ikke fordi PK'er skal være unike for å kunne avskille dem med samme navn f.eks


