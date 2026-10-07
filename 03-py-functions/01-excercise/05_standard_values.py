# Oppgave 5.1 Valgfri valuta
def show_price(price, currency = "NOK"):
    print(f"Pris: {price}, valuta: {currency}")

show_price(230)
show_price(190, "EUR")

print("\n---------\n")

# Oppgave 5.2 Tips med standardprosent
def calculate_tip(amount, tip_percent = 0):
    tips = (amount * tip_percent) / 100
    return tips

without_tips = calculate_tip(200)
with_tips = calculate_tip(200, 20)

print(f"Tipsbeløp med standardprosent: {without_tips:.2f}kr")
print(f"Tipsbeløp med 20%: {with_tips:.2f}kr")

print("\n---------\n")

# Oppgave 5.3 Gjenta en melding
def repeat_message(message, repetitions = 3):
    for i in range(repetitions):
        print(message)

repeat_message("Hei")
repeat_message("Halloween", 5)

