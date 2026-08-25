# Testing user input

# 1 name
name = input("What is your name? ")

print(name)

# 2 f-string
course = "Emne 1"

print(f"Hello, {name}!")
print(f"Welcome to {course}. ")

# f-string alternative
# Printing comma-separated items
print("Print", "these", 4, 'values')

# 3 Casting: konvertere en verdi fra en datatype til en annen
age = int(input("How old are you? "))
next_year = age + 1

print(f"Next year you'll be {next_year}.")
