# Oppgave 2.1 Vis en dagsplan
def show_daily_plan():
    print("Trene")
    print("Handle mat")
    print("Lage mat")

show_daily_plan()
print("---")
show_daily_plan()

print("\n-----------\n")

# Oppgave 2.2 Lag en skillelinje
def show_separator():
    print("-" * 30)

print("Monday")
show_separator()
print("Tuesday")
show_separator()
print("Wednesday")


print("\n-----------\n")


# Oppgave 2.3 Nedtelling
def show_countdown():
    for number in range(5, 0 , -1):
        print(number)
    print("Start!")

show_countdown()