# Oppgave 5.1: Tell oppover
up = 1

while up <= 10:
    print(up)
    up += 1

print("----")

# Oppgave 5.2: Tell nedover
down = 30

while down >= 10:
    print(down)
    down -= 1

print("----")

# Oppgave 5.3 Kvadrattall
upper_limit = int(input("Skriv inn et tall: "))
number = 1

while number ** 2 <=  upper_limit:
    square = number ** 2
    print(square)
    number += 1

print("----")

# Oppgave 5.4 Be om et gyldig tall
positive_number = int(input("Skriv inn et positivt heltall: "))

while positive_number <= 0:
    print("Du må skrive et positivt helttall")
    positive_number = int(input("Prøv igjen: "))
print("Tallet er større enn null!")



