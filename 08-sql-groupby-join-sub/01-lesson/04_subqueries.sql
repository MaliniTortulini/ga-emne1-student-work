-- Den indre spørringen beregner en verdi: gjennomsnittsbefolkningen for lagrede byer
-- Den ytre spørringen sammenligner hver by med denne verdien
-- Vi setter subspørringen i parantes. For denne gir AVG en rad med en kolonne i svaret
SELECT city.Name, city.Population
FROM city
WHERE Population > (
    SELECT AVG(Population)
    FROM city
    )
ORDER BY Population DESC;

-- Subspørring med flere verdier
-- Sunspørringen kan gi flere landekoder. IN sjekker om lander finnes blandt dem.
-- Gjentatte landkoder i subspørringen gir ikke gjentatte land i resultatet
-- Land med registrerte millionbyer
SELECT Code, Name
FROM country
WHERE Code IN (
    SELECT CountryCode
    FROM city
    WHERE Population >= 1000000
    )
ORDER BY Name;

-- Forskjell på bruksområdet, JOIN og subspørring:
  -- Bruk JOIN når du vil se kolonner fra flere tabeller
  -- Bruk en sunspørring når du trenger svaret på noe før du kan fullføre den egentlige spørringen din
  -- Av og til passer begge deler, da kan du velge