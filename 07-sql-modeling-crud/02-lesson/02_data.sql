INSERT INTO rooms (name)
VALUES ('Studio A');

INSERT INTO rooms (name)
VALUES ('Studio B'),
       ('Practice Room');

INSERT INTO instruments (name, purchase_price, acquired_on, room_id)
VALUES ('Piano', 18000.00, '2026-09-01', 1);

UPDATE instruments
SET purchase_price = purchase_price * 1.1, name = 'Grand Piano'
WHERE id = 1;
-- WHERE name = 'Piano'

SELECT *
FROM instruments
WHERE name = 'Piano';

-- Alle radene slettes!
-- DELETE FROM instruments;

DELETE FROM instruments
WHERE id = 1;

SELECT *
FROM instruments;