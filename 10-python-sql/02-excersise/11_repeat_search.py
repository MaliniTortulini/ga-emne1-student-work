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

        def country_code_search(country_code):
            with connection.cursor() as cursor:
                sql = (
                    "SELECT Language, Percentage, IsOfficial "
                    "FROM countrylanguage "
                    "WHERE CountryCode = %s "
                    "ORDER BY Language ASC")

                cursor.execute(sql, (country_code, ))
                rows = cursor.fetchall()

                if not rows:
                    print("No country language found")
                else:
                    for language, percentage, is_official in rows:
                        print(f"{language}: {percentage}%, Official: {is_official} ")

                print(f"Amount of rows: {len(rows)}")

        while True:
            country_code = input("Skriv en landekode: ").strip().upper()
            if country_code == "":
                break

            country_code_search(country_code)
except Error as e:
    print(f"Error using MySQL: {e}")