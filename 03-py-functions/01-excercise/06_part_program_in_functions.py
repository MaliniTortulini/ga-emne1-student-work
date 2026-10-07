# Oppgave 6.1 Tallanalyse
def read_number():
    number = int(input("Gi meg et helttall: "))
    return number

def describe_sign(number):
    if number > 0:
        return "Positivt"
    elif number < 0:
        return "Negativt"
    else:
        return "Null"

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

def show_analysis(number, sign, even):
    if even:
        even_number = "Partall"
        print(f"{number} er {sign} og {even_number}")
    else:
        odd_number = "Oddetall"
        print(f"{number} er {sign} og {odd_number}")



def run_number_analyzer():
    number = read_number()
    describe = describe_sign(number)
    even_odd = is_even(number)
    show_analysis(number, describe, even_odd)

run_number_analyzer()

print("\n---------\n")

# Opggave 6.2 Quiz med tre spørsmål
def ask_question(question_text):
    question = input(question_text)
    return question

def check_answer(answer, correct_answer):
    if answer.lower() == correct_answer.lower():
        return True
    else:
        return False

def show_feedback(is_correct):
    if is_correct:
        print("Korrekt!")
    else:
        print("Feil")

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



