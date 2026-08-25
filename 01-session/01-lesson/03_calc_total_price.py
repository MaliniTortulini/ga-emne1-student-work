# Beregn en totalpris

product_name = input("Product name: ")
unit_price = float(input("Unit price: "))
quantity = int(input("Quantity: "))

total = unit_price * quantity

print(f"{product_name}: {total}")

# Her brukes en avansert detalj  :.2f
# Dette skal gjøre at vi ønsker å vise tallet med akkurat 2 desimaler. Den versjonen over får kun 1 når desimal 2 blir 0

product_name = input("Product name: ")
unit_price = float(input("Unit price: "))
quantity = int(input("Quantity: "))

total = unit_price * quantity

print(f"{product_name}: {total:.2f}")
