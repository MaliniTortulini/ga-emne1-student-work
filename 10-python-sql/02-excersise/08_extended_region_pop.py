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
        try:
            min_population = int(input("Skriv inn minste befolkningstall: "))
        except ValueError as v:
            print(f"Value error: {v}")
        else:
            if min_population < 0:
                print("The number must be 0 or higher")
            else:
                with connection.cursor() as cursor:
                    sql = ("SELECT Name, Population "
                           "FROM country "
                           # Gjør om både sql resultatene og input svar til små bokstaver
                           "WHERE LOWER(Region) = LOWER(%s) "
                           "AND Population >= %s "
                           "ORDER BY Name ASC")
                    cursor.execute(sql, (region, min_population,))
                    rows = cursor.fetchall()
                    if not rows:
                        print("No countries found matching your criteria")
                    else:
                        for name, population in rows:
                            # :, formaterer befolkningstallet med tusenskilletegn
                            print(f"{name}: {population:,}")
                    print(f"Amount of rows: {len(rows)}")
except Error as e:
    print(f"Error using MySQL: {e}")

# Vi trenger fortsatt parametisering selv om folketallet er validert fordi vi må beskytte oss mot sql injections.
# Vi må sørge for at brukerens input behandles som data og ikke som SQL-kode