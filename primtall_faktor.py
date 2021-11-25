print("------Primtalls faktorisering-------")
print("             f.eks:             ")
print("        Tall:24           ")
print("        ---> [2, 2, 3, 2]           ")
tall = int(input("Skriv inn et positivt heltall:"))
primtall = 0
primtalls_liste = [tall]
while primtall <= len(primtalls_liste):
    for o in range(0, len(primtalls_liste)):
        for i in range(primtalls_liste[o]-1, 0, -1):
            if primtalls_liste[o]%i == 0:
                print(i)
                if i == 1:
                    primtall += 1
                    print(primtall)
                else:
                    primtalls_liste.append(i)
                    primtalls_liste.append(int(primtalls_liste[o]/i))
                    primtalls_liste.pop(o)
                break
        print(primtalls_liste)

