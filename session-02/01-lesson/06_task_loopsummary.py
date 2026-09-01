# Skriv ut partall og finn summen

#Beskrivelse
# 1. Brik range() med steg 2
# 2. Skriv ut partallene fra 2 til 20
# 3. Legg hvert tall til total
# 4. Skriv ut summen til slutt

total = 0

for even_number_loop in range (2, 21, 2): #21 fordi du vil telle med 20 i slutt-summen
    print(even_number_loop)
    total += even_number_loop # adderer nummer som dukker opp sammen med neste og neste, med navn kunne du hatt Tomas += sandnes of du ender opp med Tomas Sandnes

print(f"Total: {total}")
#2, 4, 6, 8, 10, 12, 14, 16, 18, 20
# Total: 110