# if kjører kode bare når testen er sant

# 1. Sammenligningen testes
# 2. Den innrykkede linjen kjøres bare ved True
# 3. Programmet fortsetter etter if-blokken
temperature = 4

if temperature < 5:
    print("Wear a warm jacket.")

print("Ready to go!")


# elif og else gir flere mulige veier, men kun 1 velges
score = 73

if score >= 90:
    print("Excellent")
elif score >= 60:
    print("Passed")
else:
    print("Try again")


# Innrykk viser hvilke linjer som hører sammen

#samme innrykk = samme blokk
#vanlig innrykk er 4 mellomrom
#PyCharm hjelper oss ofte med å få innrykkene korrekt
is_raining = True

if is_raining:
    print("Bring an umbrella.")
    print("Wear good shoes.")

print("Have a good day!")