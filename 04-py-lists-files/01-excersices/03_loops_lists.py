# Oppgave 3.1 Velkomsmeldinger
names = ["Fiona", "Ivan", "George", "Alan", "Helge"]

for name in names:
    print(f"Velkommen {name}!")

print(f"Antall deltakere: {len(names)}")

print("\n-----\n")

# Oppgave 3.2 Temperaturmålinger
temperatures = [34, -20, 2, 0, 14, 22, 4]
for temperature in temperatures:
    if temperature < 10:
        print(f"{temperature} degrees. Cold day!")
    else:
        print(f"{temperature} degrees")

print(f"Laveste temp: {min(temperatures)}")
print(f"Høyeste temp: {max(temperatures)}")

average_temp = sum(temperatures) / len(temperatures)
print(f"Gjennomsnitts temp: {average_temp}")

print("\n-----\n")

# Oppgave 3.3 Pris etter rabatt
prices = [20.00, 144.99, 5.50, 5000.89, 550.49]

for price in prices:
    sale = price * 0.8
    print(f"{price} med 20% rabatt er {sale:.2f}")

print(f"Summen av opprinnelige priser: {sum(prices):.2f}")

print("\n-----\n")


# Oppgave 3.4 Finn bestemte verdier
numbers = [3, 50, 90, 44, 72, 10, 66]
how_many_over = 0

for over_fifty_number in numbers:
    if over_fifty_number > 50:
        print(over_fifty_number)
        how_many_over += 1
print(f"Antall tall over 50: {how_many_over}")