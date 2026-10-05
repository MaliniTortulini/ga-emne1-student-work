# return sender total tilbake
# kallet bli til returverdien
# verdien lagres i order_total

def calculate_total(price, quantity):
    total = price * quantity
    return total

order_total = calculate_total(149.50, 3)
print(f"Total: {order_total:.2f}")