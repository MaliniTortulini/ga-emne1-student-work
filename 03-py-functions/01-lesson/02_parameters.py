# 1 parameter
def greet(name):
    print(f"Hello, {name}!")

greet("Erna")
greet("Jens")

print("\n-------\n")

# 2 parameter
def show_total(price, quantity):
    total = price * quantity
    print(f"Total: {total:.2f}")

show_total(49.90, 3)

