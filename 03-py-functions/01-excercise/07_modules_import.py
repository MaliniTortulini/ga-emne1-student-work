# Oppgave 7.1: Kast en terning
import random

def roll_die(sides=6):
    dice = random.randint(1, sides)
    return dice

# Bestemmer hvor mange ganger terningen ruller
for _ in range(10):
    print(roll_die())

print("\n----\n")

# D20 terning
print(roll_die(20))


print("\n---------------\n")

# Oppgave 7.2 Bruk math-modulen
# Finn hypotenus, den legste siden i en rettvinklet trekant
import math

def calculate_hypotenuse(side_a, side_b):
     a = side_a ** 2
     b = side_b ** 2
     add = a + b
     hypotenuse = math.sqrt(add)
     return hypotenuse

print(calculate_hypotenuse(3,4))

print("\n---------------\n")

# Oppgave 7.3: Lag din egen hjelpemodul
from impo_files.number_helpers import is_even_new, find_largest_new

first = find_largest_new(9, 2)
second = find_largest_new(3, 4)
even = find_largest_new(5, 5)

print(f"Det første tallet var størst: {first}")
print(f"Det andre tallet var størst: {second}")
print(f"Uavgjort! {even} - {even}")

print("\n----\n")

print(f"Dette tallet er: {is_even_new(5)}")
print(f"Dette tallet er: {is_even_new(8)}")


print("\n---------------\n")


# Oppgave 7.4: Del quiz-programmet i to filer
from impo_files.quiz_helpers import ask_question, check_answer, show_feedback

def run_quiz():
    points = 0

    first_question = "Hvor mange øyne har mennesker: "
    first_correct_answer = "2"
    first_answer = ask_question(first_question)

    second_question = "Hvilken planet er nærmest solen: "
    second_correct_answer = "Merkur"
    second_answer = ask_question(second_question)

    third_question = "Hva er verdens største øy: "
    third_correct_answer = "Grønland"
    third_answer = ask_question(third_question)

    check_first_answer = check_answer(first_answer, first_correct_answer)
    check_second_answer = check_answer(second_answer, second_correct_answer)
    check_third_answer = check_answer(third_answer, third_correct_answer)

    show_feedback(check_first_answer)
    show_feedback(check_second_answer)
    show_feedback(check_third_answer)

    if check_first_answer:
        points += 1

    if check_second_answer:
        points += 1

    if check_third_answer:
        points += 1

    print(f"Du fikk: {points} poeng")

run_quiz()



