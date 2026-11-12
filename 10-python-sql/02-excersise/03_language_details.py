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

# Løkken trenger nå tre variabler fordi vi hver tuple inneholdet tre verdier fra SQL-spørringen. Hver variabel får én
   # verdi fra tuplen.
# Rekkefølgen på verdiene i tupelen bestemmes av rekkefølgen på kolonnene i SELECT-spørringen