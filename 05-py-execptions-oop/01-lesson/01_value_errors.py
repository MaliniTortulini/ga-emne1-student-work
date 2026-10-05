inputok = False
age = 0

while not inputok:
    try:
        age = int(input("Age: "))
    except ValueError:
        print("Error: Only intergers are valid!")
    else:
        inputok = True

print(f"Next year: {age + 1}")

print("Done")

