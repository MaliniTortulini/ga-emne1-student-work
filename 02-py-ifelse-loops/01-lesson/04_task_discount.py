# Beregn rabatt med betingelser
total_purchase = float(input("Purchase amount: "))

if total_purchase >= 1000:
    discount = 0.20
elif total_purchase >= 500:
    discount = 0.10
else:
    discount = 0

discounted_amount = total_purchase * (1 - discount)
print(f"Final amount: {discounted_amount:.2f}")
