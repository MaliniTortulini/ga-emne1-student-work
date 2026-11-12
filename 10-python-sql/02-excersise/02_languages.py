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
            sql = ("SELECT Language, Percentage "
                   "FROM countrylanguage "
                   "WHERE CountryCode = 'SWE' "
                   "ORDER BY Language ASC")
            cursor.execute(sql)
            rows = cursor.fetchall()
            if not rows:
                print("No country language found")
            else:
                for language, perc in rows:
                    print(f"{language}: {perc}%")
except Error as e:
    print(f"Error using MySQL: {e}")