def nytt_brett(liste):
    for i in range(0, 3):
        liste.append([])
        for o in range(0, 3):
            liste[i].append('')
    for i in range(0, 3):
        print(liste[i])
    return liste

#brett = nytt_brett([])

#brett = [['x', '', 'x'], ['', '', ''], ['x', 'o', 'x']]

def vinn_sjekk(brett):
    test = False
    vinn_x = 0
    vinn_o = 0
    for i in range(0, 3):
        for o in range(0, 3):
            #print(1111, i, o)
            if brett[i][o] == 'x' or brett[i][o] == 'X':
                vinn_x = 1
                #print(vinn_x)
                it = 0
                u = o
                #print("Bort")
                while it < 2:
                    if u < 2:
                        if brett[i][u+1] == 'x':
                            #print(20)
                            vinn_x += 1
                        u += 1
                    else:
                        u = 0
                        if brett[i][u] == 'x':
                            #print(21)
                            vinn_x += 1
                    it += 1
                if vinn_x == 3:
                    print("X VINNER")
                    test = True
                    vinn_x = 4
                    break
                else:
                    vinn_x = 1
                it = 0
                u = i
                #print("Ned")
                while it < 2:
                    if u < 2:
                        if brett[u+1][o] == 'x':
                            #print(20)
                            vinn_x += 1
                        u += 1
                    else:
                        u = 0
                        if brett[u][o] == 'x':
                            #print(21)
                            vinn_x += 1
                    it += 1
                if vinn_x == 3:
                    print("X VINNER")
                    test = True
                    vinn_x = 4
                    break
                else:
                    vinn_x = 0
            if brett[i][o] == 'o' or brett[i][o] == 'O':
                vinn_o = 1
                #print(vinn_o)
                it = 0
                u = o
                #print("Bort")
                while it < 2:
                    if u < 2:
                        if brett[i][u+1] == 'o':
                            #print(20)
                            vinn_o += 1
                        u += 1
                    else:
                        u = 0
                        if brett[i][u] == 'o':
                            #print(21)
                            vinn_o += 1
                    it += 1
                if vinn_o == 3:
                    print("O VINNER")
                    test = True
                    vinn_o = 4
                    break
                else:
                    vinn_o = 1
                it = 0
                u = i
                #print("Ned")
                while it < 2:
                    if u < 2:
                        if brett[u+1][o] == 'o':
                            #print(20)
                            vinn_o += 1
                        u += 1
                    else:
                        u = 0
                        if brett[u][o] == 'o':
                            #print(21)
                            vinn_o += 1
                    it += 1
                if vinn_o == 3:
                    print("O VINNER")
                    test = True
                    vinn_o = 4
                    break
                else:
                    vinn_o = 0
        if vinn_x == 4 or vinn_o == 4:
            break
    return test
#vinn_sjekk(brett)

def navn():
    spiller_x = input("Hva heter du, spiller X? :")
    spiller_o = input("Hva heter du, spiller O? :")
    return spiller_x, spiller_o

def trekk(brett, x, y, x_o):
    print(brett[3-y][x-1])
    if brett[3-y][x-1] == '':
        brett[3-y][x-1] = x_o
    else:
        print("Der er det allerede noe")
        
#trekk(brett, 3, 2, 'o')
#print(brett)

def legal_check(brett, x, y, x_o):
    sjekk = 0
    if 0 > y > 4 and 0 > x > 4:
        print("Ikke på brettet")
        sjekk = 1
    if x_o != 'x' and x_o != 'o':
        print("Feil tegn")
        sjekk = 1
    return sjekk

def vis_brett(brett):
    for i in range(0, 3):
        print(brett[i])
        
def main():
    global vinner
    navn1, navn2 = navn()
    brett = nytt_brett([])
    print(f"{navn1} starter")
    vinner = False
    print(brett[0][0])
    while vinner is False:
        x = int(input("Sett en x, x:Koordinat:"))
        y = int(input("Sett en x, y:Koordinat:"))
        if legal_check(brett, x, y, 'x') == 0:
            trekk(brett, x, y, 'x')
            vis_brett(brett)
        test = vinn_sjekk(brett)
        if test:
            vinner = True
        x1 = int(input("Sett en o, x:Koordinat:"))
        y1 = int(input("Sett en o, y:Koordinat:"))
        if legal_check(brett, x1, y1, 'o') == 0:
            trekk(brett, x1, y1, 'o')
            vis_brett(brett)
        test = vinn_sjekk(brett)
        if test:
            vinner = True
    
main()