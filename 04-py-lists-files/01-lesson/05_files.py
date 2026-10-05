# Filstien beskriver hvor en fil forventes å være, men åpner ikke filen
# Path.cwd() viser gjeldene arbeidsmappe
# Path er et objekt som representer en filsti
# ".." betyr å gå en mappe utover
# / setter sammen flere mapper og filnavn

from pathlib import Path

print(f"Currect directory is {Path.cwd}")
data_directory = Path("..") / "data"
prices_path = data_directory / "prices.txt"

#Disse under trengs ikke, men skal hjelpe med å forstå/lære
print(data_directory)
print(f"Directory exists: {data_directory.exists()}")
print(prices_path)
print(prices_path.exists())

print("\n--\n")

# r for read
with open(prices_path, "r", encoding="utf-8") as file:
    #Les alt som er i fila
    content = file.read()

print(content)

print("\n--\n")

prices = []
with open(prices_path, "r", encoding="utf-8") as file:
    for line in file:
        price = float(line.strip())
        prices.append(price)

print(prices)

print("\n--\n")

report_path = data_directory / "price_report.txt"

#Existing content is replaced
# w for write
with open(report_path, "w", encoding="utf-8") as file:
    file.write("First line\n")

# Existing content is kept, new content at the end
with open(report_path, "a", encoding="utf-8") as file:
    file.write("Another line\n")
#Hadde jeg skrever file.. her så mister man retten til fila


#Her slettes first og second line, og legges til nytt i price_report.txt i data mappe
report_lines = [
    "Itmes: Epler",
    "Amount: 20",
    "Price: 96,50"]
with open(report_path, "w", encoding="utf-8") as file:
    for line in report_lines:
        file.write(line + "\n")
    #Her lukkes fila og loopen

#Sjekk forskjellen på utf-8. Dette er for at vi kan få med norske tegn
with open(report_path, "a", encoding="utf-8") as file:
    file.write("Kommentar: Husk blåbær og grøt")

with open(report_path, "a") as file:
    file.write("Kommentar: Husk blåbær og grøt")