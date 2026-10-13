# Oppgave 2.1 Filmkveld
movies = ["Black Widow", "Jumanji", "Clueless", "High School Musical", "Big Hero 6"]

print(movies[0])
print(movies[2])
print(movies[-1])

movies[1] = "Harry Potter"
print(movies)

print("\n----\n")

# Oppgave 2.2 En liste i endring
packing_list = ["Bikini", "Swiming shorts", "Sunscreen", "Sunglasses"]

packing_list.remove("Sunglasses")
packing_list.append("Book")

print(len(packing_list))

print("\n----\n")


# Oppgave 2.3 Hvem står i kø?
line = ["Karina", "Line", "Magnus", "Adam"]
print(line[0])
print(line[-1])

line.remove(line[0])
line.append("Daisy")
print(line)

print("\n----\n")


# Oppgave 2.4 Poengsummer
scores = [90, 1, 45, 22, 6, 3]

print(f"Antall poengsummer: {len(scores)}")
print(f"Summen av poengene: {sum(scores)}")
print(f"Den laveste poengsummen: {min(scores)}")
print(f"Den høyeste poengsummen: {max(scores)}")

average = sum(scores) / len(scores)
print(f"Gjennomsnittet av poengsummene: {average:.2f}")

