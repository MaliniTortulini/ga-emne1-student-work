import mysql.connector
from mysql.connector import Error

try:
    print("Connecting to the database...")
    with mysql.connector.connect(
        host='localhost',
        port=3306,
        user="root",
        password="gokstad",
        database="world_missing"
    ) as connection:
        print("Connected to MySQL!")
except Error as e:
    print(f"Error using MySQL: {e}")

print("\n--------------\n")

import mysql.connector
from mysql.connector import Error

try:
    print("Connecting to the database...")
    with mysql.connector.connect(
        host='localhost',
        port=3306,
        user="root",
        password="gokstad",
        database="world"
    ) as connection:
        print("Connected to MySQL!")
except Error as e:
    print(f"Error using MySQL: {e}")

# Forskjellen er at oppgave 10 handler om en database feil, fordi programmet prøver å koble til en database som ikke finnes.
# I oppgave 8 får vi en ValueError hvis brukeren skriver inn tekst i stedet for et hetall.
# I oppgave 4 fungerer både databasetilkoblingen og SQL-spørringen, men spørringen finner ingen rader som passer med søket.