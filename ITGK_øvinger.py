def kjopmannavrunding():
    tall = float(input("Gi inn et desimaltall:"))
    antall_ønskede_decimaler = int(input("Antall desimaler i avrunding:"))
    decimal = tall%1
    
    if antall_ønskede_decimaler > 0:
        ny_decimal = (decimal//(10**(-antall_ønskede_decimaler)) + 1) * 10**(-antall_ønskede_decimaler)
        ny_tall = tall//1 + ny_decimal
        print(ny_tall)
    elif antall_ønskede_decimaler == 0:
        if decimal > 0:
            ny_tall = tall//1 + 1
            print(ny_tall)
        else:
            print(tall)
    else:
        ny_tall = (tall//10**((antall_ønskede_decimaler*-1))+1) * 10**(antall_ønskede_decimaler*-1)
        print(ny_tall)


def avrunding():
    tall = float(input("Gi inn et desimaltall:"))
    antall_ønskede_decimaler = int(input("Antall desimaler i avrunding:"))
    decimal = tall%1
    
    string_dec = str(tall)
    string_tall = string_dec.split(".")[0]
    string_dec = string_dec.split(".")[1]
    
    while len(string_dec) >= antall_ønskede_decimaler+1:
        if antall_ønskede_decimaler == 0 and len(string_dec) == 1:
            if int(string_dec) < 5:
                string_dec = "0"
            elif int(string_dec) > 5:
                string_tall = str(int(string_tall)+1)
            elif int(string_dec) == 5:
                if int(string_tall[-1])%2 == 1:
                    string_tall = str(int(string_tall)+1)
            string_dec = "0"
            break
        a = int(string_dec[-1])
        b = int(string_dec[-2])
        if a < 5:
            a = 0
        elif a > 5:
            a = 10
        elif a == 5:
            if b%2 == 1:
                a = 10
            else:
                a = 0
        if a == 10:
            if b == 9:
                string_dec = string_dec[0:-2] + str(b)
            else:
                string_dec = string_dec[0:-2] + str(b+1)
        elif a == 0:
            string_dec = string_dec[0:-2] + str(b)
    
    
    ny_tall = string_tall + "." + string_dec
    print(ny_tall)
    

def årstider():
    month = input("Måned:").lower()
    day = int(input("Dag:"))
    
    årstider = []
    årstider2 = ["vår", "sommer", "høst", "vinter"]
    vår = ["april", "mai", "juni", 20]
    sommer = ["juli", "august", "september", 21]
    høst = ["oktober", "november", "desember", 20]
    vinter = ["januar", "februar", "mars", 19]
    årstider.append(vår)
    årstider.append(sommer)
    årstider.append(høst)
    årstider.append(vinter)
    
    for i in range(0, len(årstider)):
        for o in range(0, len(årstider[i])):
            if month == årstider[i][o]:
                if type(årstider[i][o+1]) is not int:
                    print(årstider2[i])
                    break
                else:
                    if day > årstider[i][o+1]:
                        if i < 3:
                            print(årstider2[i+1])
                        else:
                            print(årstider2[0])
                    else:
                        print(årstider2[i])
                    break
        else:
            continue
        break


def primtallsfaktorisering():
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


def matriseaddisjon():
    import random

    def random_matrise(bredde, høyde):
        matrise = []
        for i in range(0, høyde):
            matrise.append([])
            for o in range(0, bredde):
                matrise[i].append(random.randint(0, 10))
        #print(matrise)
        return matrise
    
    def print_matrise(matrise, navn):
        print(navn + "=[")
        for i in range(0, len(matrise)):
            print(matrise[i])
        print("]")
        
    def matrise_addisjon(a, b):
        if (len(a) != len(b)) or (len(a[0]) != len(b[0])):
            print("Matrisene er ikke av samme dimensjon")
        else:
            matrise = []
            for i in range(0, len(a)):
                matrise.append([])
                for o in range(0, len(a[0])):
                    matrise[i].append(a[i][o] + b[i][o])
            #print(111, matrise)
            return matrise
    
    def main():
        A = random_matrise(4,3)
        print_matrise(A, 'A')
        B = random_matrise(3,4)
        print_matrise(B, 'B')
        C = random_matrise(3,4)
        print_matrise(C, 'C')
        D = matrise_addisjon(A,B)
        E = matrise_addisjon(B,C)
        print_matrise(E, 'B+C' )
        
    main()


def tannfeen():
    teeth = [95,103,71,99,114,64,95,53,97,114,109,11,2,21,45,2,26,81,54,14,118,108,117,27,115,43,70,58,107]
    matrise = []
    
    for i in range(0, len(teeth)):
        matrise.append([0, 0, 0, 0])
        tall = teeth[i]
        while tall > 0:
            if tall >= 20:
                matrise[i][0] += 1
                tall -= 20
            elif tall >= 10:
                matrise[i][1] += 1
                tall -= 10
            elif tall >= 5:
                matrise[i][2] += 1
                tall -= 5
            elif tall >= 1:
                matrise[i][3] += 1
                tall -= 1
    print(matrise, "\n")
    
    for i in range(0, len(matrise)):
        print(f"20: {matrise[i][0]}, 10: {matrise[i][1]}, 5: {matrise[i][2]}, 1: {matrise[i][3]}")


def lotto():
    import random

    numbers = []
    for i in range(1, 35):
        numbers.append(i)
    
    myGuess = [1, 2, 3, 4, 5, 6, 7]
    print(myGuess, len(myGuess))
    
    def drawNumbers(n, N):
        random.shuffle(n)
        liste = []
        for i in range(0, N):
            liste.append(n[i])
        return liste
    
    def compList(a, b):
        like_tall = 0
        tilleggs_tall = 0
        for i in range(0, 7):
            for o in range(0, 7):
                if a[i] == b[o]:
                    like_tall += 1
        for i in range(7, 10):
            for o in range(0, 7):
                if a[i] == b[o]:
                    tilleggs_tall += 1
        return like_tall, tilleggs_tall
    
    def Winnings(a, b):
        premie = 0
        if a == 7:
            premie += 2749455
        elif a == 6 and b == 1:
            premie += 102110
        elif a == 6:
            premie += 3385
        elif a == 5:
            premie += 95
        elif a == 4 and b == 1:
            premie += 45
        return premie-5
    
    def main():
        vinner_tall = drawNumbers(numbers, 10)
        antall_like, tillegg = compList(vinner_tall, myGuess)
        premie = Winnings(antall_like, tillegg)
        print(vinner_tall)
        print(antall_like, tillegg)
        print(premie)
        
    main()




               
