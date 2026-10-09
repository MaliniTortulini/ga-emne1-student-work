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