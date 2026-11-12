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
        with connection.cursor() as cursor:
            sql = ("SELECT Language, Percentage, IsOfficial "
                   "FROM countrylanguage "
                   "WHERE CountryCode = 'ZZZ' "
                   "ORDER BY Language ASC")
            cursor.execute(sql)
            rows = cursor.fetchall()
            if not rows:
                print("No country language found")
            else:
                for language, percentage, is_official in rows:
                    print(f"{language}: {percentage}%, Official: {is_official} ")
            print(f"Amount of rows: {len(rows)}")
except Error as e:
    print(f"Error using MySQL: {e}")

print("\n--------\n")

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
        with connection.cursor() as cursor:
            sql = ("SELECT Language, Percentage, IsOfficial "
                   "FROM countrylanguage "
                   "WHERE CountryCode = 'SWE' "
                   "ORDER BY Language ASC")
            cursor.execute(sql)
            rows = cursor.fetchall()
            if not rows:
                print("No country language found")
            else:
                for language, percentage, is_official in rows:
                    print(f"{language}: {percentage}%, Official: {is_official} ")
            print(f"Amount of rows: {len(rows)}")
except Error as e:
    print(f"Error using MySQL: {e}")

# En tom resultatliste er ikke det samme som databasefeil. En tom liste betyr at SQL-spørringen ble gjennomført uten feil,
# men at databasen ikke fant noen rader som oppfylte betingelsene. En databasefeil betyr at noe gikk galt under tilkoblingen
# eller utførelsen av spørringen
