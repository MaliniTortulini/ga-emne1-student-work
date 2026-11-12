import mysql.connector
from mysql.connector import Error

# with sørger for at forbindelsen automatisk lukkes etter at connect-blokken går ut av scope
# connect() åpner forbindelsen til MySQL

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
    # connection.cursor() gir oss en cursor for SQL-kommandoen vår. Dvs. et Python-objekt som kan holde på vår SQL statement
    # execute() kjører SQL-kommandoen mpt databasen
    # fetchall() returnerer resultatet av en spørring til en variabel i Python
        with connection.cursor() as cursor:
            # Hver rad fra denne spørringen er en tuple. SELECT bestemmer kolonne og rekkefølgen
            sql = ("SELECT Name, Population "
                   "FROM city "
                   "WHERE CountryCode = 'NOR' ")
            cursor.execute(sql)
            rows = cursor.fetchall()
            # Løkken pakker ut hver rad i variablene name og population
            if not rows:
                print("No cities found.")
            else:
                for name, population in rows:
                    print(f"{name}: {population}")
except Error as e:
    print(f"Error using MySQL: {e}")

# Resultatets struktur
# En tuple er en ordnet samling verdier. Elementene kan ikke byttes  ut etter at tupelen er opprettet

# fetchall() gir en tom liste når ingen rader returneres.
# Programmet bør håndtere dette: En mulighet er å fortelle brukeren at søket ikke ga noen treff (if/else)
