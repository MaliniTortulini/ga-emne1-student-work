# Oppgave 4.1 Doble et tall
def double_number(number):
    total = number * 2
    return total


result1 = double_number(2)
result2 = double_number(-5)

print(result1)
print(result2)

print("\n---------\n")

# Oppgave 4.2 Minutter til sekunder
def convert_minutes_to_seconds(minutes):
    seconds = minutes * 60
    return seconds

one_min = convert_minutes_to_seconds(1)
two_half_min = convert_minutes_to_seconds(2.5)
ten_min = convert_minutes_to_seconds(10)

print(one_min)
print(two_half_min)
print(ten_min)

print("\n---------\n")

# Oppgave 4.3 Pris etter rabatt
# price: float er type hints
# -> float er til return, den skal returnere en float også
def calculate_discounted_price(price: float, discount_percent: float) -> float:
   discount_amount = (price * discount_percent) / 100
   new_price = price - discount_amount
   return new_price

twenty_percent = calculate_discounted_price(200, 20)
seventy_five_percent = calculate_discounted_price(200, 75)

print(f"Pris etter 20% rabatt er: {twenty_percent:.2f}")
print(f"Pris etter 75% rabatt er: {seventy_five_percent:.2f}")

# Type hints tvinger ikke programmet til å faktisk være en float, den er til informasjon ikke aotomatisk validering
# Gjør det enklere å finne feil

print("\n---------\n")

# Oppgave 4.4 Finn det største tallet
def find_largest(first_number, second_number):
    if first_number > second_number:
        return first_number
    elif second_number > first_number:
        return second_number
    else:
        return first_number

first = find_largest(9, 2)
second = find_largest(3, 4)
even = find_largest(5, 5)

print(f"Det første tallet var størst: {first}")
print(f"Det andre tallet var størst: {second}")
print(f"Uavgjort! {even} - {even}")

# Oppgave 4.5 Returner en boolsk verdi
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

for check_number in range(1, 11):
    print(check_number, is_even(check_number))