# Del 4. Sammensatte programmer

# 13. Bygg en setning
adjective_1 = input("Skriv et adjektiv: ")
adjective_2 = input("Skriv et adjektiv: ")
noun = input("Skriv et subjektiv: ")
verb = input("Skriv et verb: ")

print(f"Et {adjective_1} {noun} er {adjective_2} og liker å {verb} til butikken.")


# 14. Enkel valutaomregning
amount = float(input("Beløp: "))
currency_rate = float(input("Kurs: "))

converted_currency = amount * currency_rate
print(converted_currency)


# 15. Mini-prosjekt: totalpris
product_name = input("Produktnavn: ")
unit_price = float(input("Enhetspris: "))
amount = int(input("Antall produkter: "))

total_price = unit_price * amount

print(product_name)
print(f"Total pris: {total_price}")


# 16. Pris med rabatt
product_price = float(input("Produkt pris: "))
discount = int(input("Rabatt: "))

discount_price = product_price * (discount / 100)
price_with_discount = product_price - discount_price

print(f"Ny pris med rabatt er: {price_with_discount:.2f}")
