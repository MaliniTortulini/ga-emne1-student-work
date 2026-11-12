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
        region = input("Skriv en region: ").strip()
        with connection.cursor() as cursor:
            sql = ("SELECT Name, Population "
                   "FROM country "
                   #Gjør om både sql resultatene og input svar til små bokstaver
                   "WHERE LOWER(Region) = LOWER(%s) "
                   "ORDER BY Name ASC")
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