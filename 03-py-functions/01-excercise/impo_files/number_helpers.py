# Oppgave 4.4 Finn det største tallet
def find_largest_new(first_number, second_number):
    if first_number > second_number:
        return first_number
    elif second_number > first_number:
        return second_number
    else:
        return first_number



# Oppgave 4.5 Returner en boolsk verdi
def is_even_new(number):
    if number % 2 == 0:
        return True
    else:
        return False

for check_number in range(1, 11):
    print(check_number, is_even_new(check_number))