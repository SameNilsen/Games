liste = []
liste2 = []

for i in range(1, 101):
    if i%3 != 0:
        if i%7 != 0:
            liste.append(i)

print(111, liste, len(liste), "\n")
