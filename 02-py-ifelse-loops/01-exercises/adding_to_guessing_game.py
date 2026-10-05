# Mini prosjekt: Et enkelt gjettelek spill!

# Programmet skal
# 1. Ha et hemmelig tall
# 2. Gi spilleren 5 forsøk
# 3. Si om svaret er korrekt, lavt eller høyt
# 4. Stoppe når svaret er riktig eller forsøkene er brukt opp

# Vi trenger
# secret_number
# attemps_left
# if / elif / else logikk
# en while-løkke rundt gjette-logikken

# Egne ideer lagt til
#Prosjekt 1:
# random number

#Prosjekt 2:
#jeg velger et tall og maskinen skal gjette


secret_number = 25
attempts_left = 5
guessed_correctly = False

while attempts_left > 0 and not guessed_correctly: # når attemps er større enn null gjør-->
    guess = int(input("Guess a number between 1 - 30 "))

    if guess == secret_number:
        print("Correct! The number was 25!")
        guessed_correctly = True
    elif guess > secret_number:
        print("You guessed too high!")
    else:
        print("You guessed too low!")

    attempts_left -= 1

if not guessed_correctly:  #Her er det viktig at if ikke har innrykk, da viste den seg etter hver gjetting
        print(f"The number was {secret_number}")
