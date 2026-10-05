# Oppgave 3.1: Sammenlign med 10
comparison_number = int(input("Skriv inn et helt tall: "))

if comparison_number > 10:
    print("The number is greater than 10")
elif comparison_number == 10:
    print("The number is equal to 10")
else:
    print("The number is less than 10")

# Oppgave 3.2: Sammenlign to tall
first_number = int(input("Skriv inn et nummer: "))
second_number = int(input("Skriv inn ENDA et nummer: "))

if first_number == second_number:
    print("Tallene er like!")
elif first_number > second_number:
    print("Det første tallet er større enn det andre!")
else:
    print("Det andre tallet er størst!")


# 0ppgave 3.3: Positivt, negativt eller null
check_number = int(input("Skriv inn et nummer, kan også være minus tall: "))

even_or_odd = check_number % 2

if check_number == 0:
    print("Tallet er null")
elif check_number > 0 and even_or_odd == 0:
    print("Tallet er positivt og er et partall")
elif check_number > 0 and even_or_odd == 1:
    print("Tallet er positivt og er et oddetall")
elif check_number < 0 and even_or_odd == 0:
    print("Tallet er negativt og et partall")
else:
    print("Tallet er negativt og et oddetall")


# Oppgave 3.4 Beregn fraktkostnad
package_weight = float(input("Pakkevekt: "))

if package_weight <= 2:
    print("Frakten koster: 79kr")
elif package_weight <= 5:
    print("Frakten koster: 129 kr")
elif package_weight <= 10:
    print("Frakten koster: 199 kr")
else:
    print("Pakken er for tung og kan ikke sendes med denne tjenesten")

# Oppgave 3.5 Tilgang til et spill
has_username = False
accepted_rules = True
is_blocked = False

if has_username and accepted_rules and not is_blocked:
    print("Du har tilgang")
else:
    print("Du har ikke tilgang")

# Oppgave 3.6 Gratis levering
order_amount = 650
is_member = True

if order_amount >= 800 or is_member == True:
    print("Du får gratis levering!")
else:
    print("Du må betale frakt")