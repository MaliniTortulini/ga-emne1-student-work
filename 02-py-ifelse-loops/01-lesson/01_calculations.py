number_of_tickets = int(input("How many tickets? "))
ticket_price = 180
service_fee = 35

subtotal = ticket_price * number_of_tickets
total = subtotal + service_fee
price_per_person = total / number_of_tickets

print(total)
print(price_per_person)


#oppgave 1: regn ut kostnaden per person
total_cost = 1023
number_of_people = 5

cost_per_person = total_cost / number_of_people
print(f"It costs {cost_per_person:.2f} per person")
