# Oppgave 6.1: Tallundersøkelse
for even_odd in range(1, 21):
    if even_odd % 2 == 0:
        print(f"{even_odd}: Partall")
    else:
        print(f"{even_odd}: Oddetall")

print("----")

# Oppgave 6.2: PIN-kode med begrenset antall forsøk
secret_pin = 2468
is_authenticated = False
attempts_left = 3

answer = int(input("Pin-kode: "))

while not is_authenticated and attempts_left > 1:

    if answer == secret_pin:
        is_authenticated = True
        print("Access granted")
    else:
        attempts_left -= 1
        answer = int(input("Prøv igjen! Pin-kode: "))

    if not is_authenticated:
        print("Access denied")

# Oppgave 6.3: Finn tall som oppfyller flere krav
counter = 0
for req_number in range(1, 101):
    if req_number % 3 == 0 and 20 < req_number < 80:
        print(req_number)
        counter += 1
print(f"Antall tall som oppfyller kravene: {counter}")





