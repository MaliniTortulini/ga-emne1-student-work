# Oppgave 4.1 Fast åpningstid
opening_hours = ("Mandag", "08:00", "18:00"),

print(opening_hours[0][0])
print(opening_hours[0][1])
print(opening_hours[0][2])


# opening_hours[1] = "10:00"
# TypeError: 'tuple' object does not support item assignment

print(opening_hours)

# Tuple er bra for åpningstider fordi de ofte ikke skal endres

print("\n----\n")

# Oppgave 4.2 Fargekode
colors = (255, 192, 203)

print(f"Rød: {colors[0]}, Grønn: {colors[1]} og Blå: {colors[2]}")

color_list = [
    (255, 192, 203),
    (255, 255, 0),
    (0, 0, 255)
]

for color in color_list:
    print(color)


print("\n----\n")

# Oppgave 4.3 Velg mellom liste og tuple
# Endres hele tiden
to_do = ["Vaske bad", "Lage mat", "Handle mat"]
# Endres aldri da du kun er født en gang
birthday = ("20.09.2018", "03.02.2009")

