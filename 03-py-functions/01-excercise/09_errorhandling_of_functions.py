# Oppgave 9-1 Fuksjonen kalles for tidlig

#show_message()

#def show_message():
#  print("Hello")

def show_message():
    print("Hello")
show_message()
#første kjøring:NameError: name 'show_message' is not defined
# Flyttet kallet til under funskjonen
# Oppgave løst
# Programmet leser ovenfor og ned, derfor skjøner ikke programmet
# hva den skal gjøre når funskjonen er etter kallet


# Oppgave 9.2 print i stedet for return
#def square_number(number):
 #   print(number ** 2)

#result = square_number(5)
#doubled_result = result * 2

def square_number(number):
    return number ** 2

result = square_number(5)
doubled_result = result * 2
#første kjøring:    doubled_result = result * 2
                     #"~~~~~~~^~~
#TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'
#Function square_number doesn't return anything
# Byttet return med print
#Remove redundant parentheses
# oppgave løst
# print viser outputen, mens return sender daten til videre bruk



#Opggave 9.3 Feil antall argumenter
#def testing(a, b):
 #   return a + b

#testing(34)

def testing(a, b):
    return a + b

print(testing(34, 34))
print(testing(2, 6))
print(testing(90,10))
#første kjøring: TypeError: testing() missing 1 required positional argument: 'b'
# la til argument b, 34
# andre kjøring med tre argumenter:
#TypeError: testing() missing 2 required positional arguments: 'a' and 'b'
# Feilen oppstår fordi funksjonen har to parametere
# oppgave løst

