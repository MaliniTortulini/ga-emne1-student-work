# Oppgave 4.1 Tell oppover
for first_for in range (0, 10):
    print(first_for)
print("Første oppgave ferdig!")

for second_for in range(5, 16):
    print(second_for)
print("Andre oppgave er ferdig!")

for third_for in range(1, 21):
    print(third_for)
print("Tredje oppgave er ferdig!")


# Oppgave 4.2: Partall og oddetall
for even_numbers in range(2, 21, 2):
    print(even_numbers)
print("Partall ferdig")

for odd_numbers in range(1, 20, 2):
    print(odd_numbers)
print("Oddetall ferdig")


# Oppgave 4.3 Tell nedover
for count_down in range(30, 9, -1):
    print(count_down)
print("Alle tall fra 30 til 10 er ferdig")

for down_odd_numbers in range(29, 10, -2):
    print(down_odd_numbers)
print("Alle oddetall er ferdig ")

# Oppgave 4.4 Summer tall
sum = 0
for numbers in range(1, 11):
    sum += numbers
    print(f"tall: {numbers} => foreløpig sum: {sum}")
print(f"Endelig sum {sum}")

# 4.5 Summer tall med bestemte steg
third = 0
for third_multi_table in range (3, 31, 3):
    third += third_multi_table
    print(third_multi_table)
print(f"Sum av 3-gangetabellen: {third}")

fifth = 0
for five_multi_table in range(5, 51, 5):
    fifth += five_multi_table
    print(five_multi_table)
print(f"Sum av 5-gangetabellen: {fifth}")

# 4.6 Gangetabell
table_input = int(input("Velg et tall fra gangetabellen: "))

for multiplication in range(1, 11):
    var = table_input * multiplication
    print(f"{table_input} x {multiplication} = {var}")

