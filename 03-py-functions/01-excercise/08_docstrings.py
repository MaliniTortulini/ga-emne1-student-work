# Oppgave 8.1 Dokumenter hjelpemodulen
# Oppgave 4.4 Finn det største tallet
def find_largest_new(first_number, second_number):
    """Finds lagrest number or equal"""
    if first_number > second_number:
        return first_number
    elif second_number > first_number:
        return second_number
    else:
        return first_number



# Oppgave 4.5 Returner en boolsk verdi
def is_even_new(number):
    """Checks if number is even or odd"""
    if number % 2 == 0:
        return True
    else:
        return False

for check_number in range(1, 11):
    print(check_number, is_even_new(check_number))

# Oppgave 8.2 Dokumenter quiz-funksjonene
def ask_question(question_text):
    """Returns user anwser to question"""
    question = input(question_text)
    return question

def check_answer(answer, correct_answer):
    """Checks users answer with question"""
    if answer.lower() == correct_answer.lower():
        return True
    else:
        return False

def show_feedback(is_correct):
    """Gives a feedback depending on right or wrong answer from user"""
    if is_correct:
        print("Korrekt!")
    else:
        print("Feil")