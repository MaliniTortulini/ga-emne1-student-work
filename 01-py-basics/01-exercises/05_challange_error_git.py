# Del 5. Utfordring, feilretting og Git

# 17. Sekunder til timer, minutter og sekunder
seconds_input = int(input("Skriv inn antall sekunder: "))

hours = seconds_input // 3600
minutes = seconds_input % 60
seconds = seconds_input % 60

print(f"{seconds_input} sekunder tilsvarer: {hours} timer, {minutes} minutter og {seconds} sekunder")

# 18. Feillesing

# text = hallo"
# numb = 23
# text_again = "hvordan går det?"
# print(text + numb + text_again)

# Rettet på etter feillesing
text = "hallo" #SyntaxError: unterminated string literal (detected at line 19)
numb = "23"
text_again = "hvordan går det?"

print(text + " " + numb + "," + " " + text_again)
#          ~~~~~^~~~~~
#TypeError: can only concatenate str (not "int") to str
