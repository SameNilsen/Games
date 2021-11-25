brett = [['x', 'x', 'x'], [' ', 'x', ' '], [' ', 'x', ' ']]


def vinn_sjekk(brett):
    vinn_x = 0
    vinn_o = 0
    for i in range(0, 3):
        for o in range(0, 3):
            if brett[i][o] == 'x' or brett[i][o] == 'X':
                vinn_x += 1
                print(vinn_x)
                it = 0
                u = o
                while it < 2:
                    if u < 2:
                        if brett[i][u+1] == 'x':
                            vinn_x += 1
                        u += 1
                    else:
                        if brett[i][u] == 'x':
                            vinn_x += 1
                        u = 0
                    it += 1
                if vinn_x == 3:
                    print("X VINNER")
vinn_sjekk(brett)