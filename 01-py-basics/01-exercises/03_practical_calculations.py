# 9. Minutter til timer og minutter
# Ekstra som ikke oppgaven inkluderer, jeg vil ha 1 time og 2+ timer, samme med minutter

minutes = int(input("Skriv antall minutter: "))

hours = minutes // 60

rest_minutes = minutes % 60

if hours == 1 and rest_minutes == 1:
    print(f"{hours} time og {rest_minutes} minutt")
elif hours == 1:
    print(f"{hours} time og {rest_minutes} minutter")
elif rest_minutes == 1:
    print(f"{hours} timer og {rest_minutes} minutt")
else:
    print(f"{hours} timer og {rest_minutes} minutter")

# 10. Tips og totalpris
product_price = float(input("Total pris på varer: "))

percentage_off = 15

price_with_percentage = (percentage_off / 100) * product_price
print(f"Tips: {price_with_percentage}")

total = product_price + price_with_percentage
print(f"Total pris med tips: {total}")

# 11. Centimeter til fot
centimeter = float(input("Centimeter: "))

convert_to_feet = centimeter / 30.48

print(f"{centimeter} cm = {convert_to_feet:.2f} fot")


# 12. Beregn ukelønn
paid_by_hour = float(input("Timelønn: "))
hours_worked = float(input("Timer jobbet: "))

earned = paid_by_hour * hours_worked

print(f"Tjent denne uken: {earned:.2f}")

