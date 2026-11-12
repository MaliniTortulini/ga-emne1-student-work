#region = input("Enter region: ")
   # Unsafe: input becomes part of the SQL
# sql = (
# "SELECT Name, Population FROM country "
# f"WHERE Region = '{region}'"
# )
# cursor.execute(sql)

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
        region = input("Enter region: ")
        with connection.cursor() as cursor:
            sql = ("SELECT Name, Population "
                   "FROM country "
                   #Gjør om både sql resultatene og input svar til små bokstaver
                   "WHERE Region = %s "
                   )
            cursor.execute(sql, (region, ))
            rows = cursor.fetchall()
            if not rows:
                print("No region found")
            else:
                for name, population in rows:
                    # :, formaterer befolkningstallet med tusenskilletegn
                    print(f"{name}: {population:,}")
            print(f"Amount of rows: {len(rows)}")
except Error as e:
    print(f"Error using MySQL: {e}")

# i den usikre versjonen kunne brukerens input endret SQL-spørringens betingelser, slik at den returnere informasjon
   # som brukeren egentlig ikke skulle få gjennom søket. SQL-injeksjon kan også være farlig i andre spørringer som endrer
   # eller sletter data.
# Parametrisering sørger for at brukerens input blir behandlet som data og ikke som en del av SQL-koden
# ja det er trygt å bruke f-streng til å formatere teksten du skriver ut med print(). Det er trygt fordi f-strengen brukes
   # til å formatere teskt som skal skrives ut, ikke til å bygge SQL-spørringen