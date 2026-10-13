CREATE DATABASE IF NOT EXISTS music_school;

USE music_school;

CREATE TABLE rooms(
    id INT AUTO_INCREMENT,
    name VARCHAR(40) NOT NULL,
    PRIMARY KEY (id),
    UNIQUE(name)
);

CREATE TABLE instruments (
    id INT AUTO_INCREMENT,
    name VARCHAR(80) NOT NULL,
    purchase_price DECIMAL(8,2),
    acquired_on DATE,
    room_id INT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (room_id) REFERENCES rooms(id)
);


ALTER TABLE rooms
ADD COLUMN capacity INT NOT NULL DEFAULT 1;

ALTER TABLE rooms
MODIFY COLUMN capacity INT NOT NULL DEFAULT 10;

-- lager en test tabell for å slette
CREATE TABLE test (
    note VARCHAR(100)
);
-- Slett test tabellen
DROP TABLE test;
