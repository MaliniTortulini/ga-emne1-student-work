# Oppgave 3.1 Personlig hilsen
def greet_student(name):
    print(f"Velkommen, {name}!")

greet_student("Else")
greet_student("Anna")
greet_student("Jon")

print("\n---------\n")

# Oppgave 3.2 Temperaturmelding
def show_temperature(city, temperature):
    print(f"It is {temperature} in {city}")

show_temperature("Oslo", 18)
show_temperature("Gouda", 23)
show_temperature("Trondheim", 13)

print("\n---------\n")

# Oppgave 3.3 Kampresultat
def show_match_result(home_team, away_team, home_score, away_score):
    if home_score > away_score:
        print(f"{home_team} {home_score} - {away_team} {away_score}")
        print(f"Vinneren er: Hjemmelaget {home_team}!")
    elif away_score > home_score:
        print(f"{home_team} {home_score} - {away_team} {away_score}")
        print(f"Vinneren er: Bortelaget {away_team}")
    else:
        print(f"{home_team} {home_score} - {away_team} {away_score}")
        print("Uavgjort!")

show_match_result("Andebu", "Heistad", 2, 4)
print("----")
show_match_result("Pors", "Turn", 3, 3)
print("----")
show_match_result("Tønsberg", "Notodden", 1, 0)

print("\n---------\n")

# Oppgave 3.4 Rekkefølgen på argumentene
def show_profile(name, age, city):
    print(f"Navn: {name}, alder: {age}, by: {city}")

show_profile("Malin", 23, "Gouda")
# Feil rekkefølge, 24 er ikke navnet til Sivert
show_profile(24, "Skien", "Sivert")
# Fiks name = Sivert, age = 24, city = Skien
show_profile("Sivert", 24, "Skien")



