#Sammenligninger gir True eller False

age = 20
minimum_age = 18

print(age >= minimum_age)
print(age == 20)
print(age != 20)
print(age <= 10)

# = tilordner, == sammenligner
score = 10

print(score == 10)

# and, or og not kombinerer sammenligninger

#Begge må være sanne: and
age = 20
has_tickets = True

can_enter = age >= 18 and has_tickets
print(can_enter)

#Minst 1 MÅ være sant: or
is_weekend = True
is_holiday = False

can_sleep_in_late = is_weekend or is_holiday
print(can_sleep_in_late)

#Gir omvendt resultat: not
must_get_up = not can_sleep_in_late
print(must_get_up)