-- This root user changes and city_reader kan read them
SELECT city.Name, city.Population
FROM world.city
WHERE CountryCode = 'NOR'
   AND Name IN ('Oslo', 'Bergen')
ORDER BY Name;

START TRANSACTION;

UPDATE world.city
SET Population = Population + 100000
WHERE CountryCode = 'NOR'
AND Name = 'Oslo';

UPDATE world.city
SET Population = Population - 100000
WHERE CountryCode = 'NOR'
  AND Name = 'Bergen';

COMMIT;


-- city_reader user
SELECT CURRENT_USER(), CONNECTION_ID();


-- Dette skal være tilatt: JA
SELECT city.Name, city.Population
FROM city
WHERE CountryCode = 'NOR';

-- Dette skal bli avvist: JA og JA
SELECT * FROM world.country;
-- [42000][1142] SELECT command denied to user 'city_reader'@'172.17.0.1' for table 'country'


UPDATE world.city
SET Population = Population
WHERE CountryCode = 'NOR'
   AND Name = 'Oslo';
-- [42000][1142] UPDATE command denied to user 'city_reader'@'172.17.0.1' for table 'city'

-- This user changes and city_reader kan read them
SELECT city.Name, city.Population
FROM world.city
WHERE CountryCode = 'NOR'
  AND Name IN ('Oslo', 'Bergen')
ORDER BY Name;