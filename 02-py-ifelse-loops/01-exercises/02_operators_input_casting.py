# Oppgave 2.1: Beregn kostnaden for en kjøretur

distance = float(input("Kjørelengde: "))
fuel_per_100_km = float(input("Drivstoff per 100km brukt: "))
fuel_price = float(input("Drivstoffpris: "))

fuel_quantity = distance / 100 * fuel_per_100_km
fuel_per_liter = fuel_quantity * fuel_price

print(f"Drivstoffmengde: {fuel_quantity} liter")
print(f"Kostnad: {fuel_per_liter} kr.")


# Oppgave 2.2 Regning med to tall
first_number = int(input("Første nummer: "))
second_number = int(input("Andre nummer: "))

addition = first_number + second_number
minus = first_number - second_number
multiplication = first_number * second_number
division = first_number / second_number
integer_division = first_number // second_number
rest_after_division = first_number % second_number

print(f"Sum: {addition}")
print(f"Differanse: {minus}")
print(f"Produkt: {multiplication}")
#Når second_number er 0, får programmet ZeroDivisionError: division by zero. Dette er fordi det ikke er mulig p dele et tall på 0. Programmet stopper ved vanlig divisjon.
print(f"Vanlig divisjon: {division}")
print(f"Heltallsdivisjon: {integer_division}")
print(f"Rest etter divisjon: {rest_after_division}")


#Oppgave 2.3: Potens og partall
whole_number = int(input("Skriv inn et helt tall: "))

squared = whole_number ** 2
cubed = whole_number ** 3
rest_after_2 = whole_number % 2

print(f"I andre: {squared}")
print(f"I tredje: {cubed}")

if rest_after_2 == 0:
    print("Tallet er et partall")
else:
    print("Tallet er et oddetall")



