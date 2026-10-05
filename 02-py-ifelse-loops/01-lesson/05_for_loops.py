# for passer når antall gjentakelser er kjent

#Ta verdier fra 0 opp til range(), lagre verdien i loop_counter
#Kjør den innrykkede blokken
#Stopp når du kommer til 6 (før 6 utføres, altså vi ser kun 5, 6 blir Finished)
#1 blir med, men 6 syntes ikke
for loop_counter in range(1, 6):
    print(f"Round {loop_counter}")

print("Finished!")

# range() bestemmer start, stopp og steg

#Noen vanlige former
range(5) # 0, 1, 2, 3, 4
range(2, 6) # 2, 4, 5
range(2, 11, 2) # 2, 4, 6, 8, 10
range(9, 0, -1) # 9, 8, 7, 6, , 4, 3, 2, 1

# Related topic: slicing
name = 'Tomas Sandnes'
print(name[:5]) # Tomas
print(name[6:13]) # Sandnes, mellomrom telles som et tall
