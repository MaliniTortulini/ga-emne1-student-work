-- Oppgave 7: Testsøk med LIKE
-- Oppgave 7.1 Landnavn med en bestemt start
SELECT Name
FROM country
WHERE Name LIKE 'B%'
ORDER BY Name ASC;

SELECT Name
FROM country
WHERE Name LIKE 'Br%'
ORDER BY Name ASC;
-- Når jeg endrer B% til Br% så blir søket mer spesifikt
-- Jeg får færre land fordi navnene må begynne med Br og ikke bare B

-- Oppgave 7.2 Slutten eller midten av navnet
SELECT Name
FROM country
WHERE Name LIKE '%stan'
ORDER BY Name ASC;

SELECT Name
FROM country
WHERE Name LIKE '%is%'
ORDER BY Name ASC;
-- % betyr null eller flere tegn
-- Hvis du da skriver % først betyr dette samma hva som står først, men dette spesifikt bak
-- %ord% betyr samma hva forran og bak, men ordet inneholder f.eks is

-- Oppgave 7.3 Nøyaktig ett tegn
SELECT Name
FROM country
WHERE Name Like '_a%';
-- I den første spørringen bruker jeg _ for å representere den første bokstaven,
-- a som den andre og % fordi resten kan ha ulik lengde og bokstaver.

SELECT Name
FROM country
WHERE Name Like '____';
-- I den andre bruker jeg kun fire _ fordi jeg vil ha navn som kun består av
-- nøyaktig fire tegn. Jeg bruker ikke % fordi jeg vil ikke ha noe forran eller bak