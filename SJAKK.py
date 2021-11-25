hvit = ['♜', '♝', '♞', '♛', '♚', '♟']
svart = ['♖', '♗', '♘', '♕', '♔', '♙']
begge = ['♜', '♝', '♞', '♛', '♚', '♟', '♖', '♗', '♘', '♕', '♔', '♙']

def make_board():
    matrise = []
    #  Tomt brett
    for i in range(0, 8):
        matrise.append([])
        for o in range(0, 8):
            matrise[i].append('⟤')
    # Legger til bønder ♙ svart
    for i in range(0, 8):
        matrise[1][i] = '♙'
    # Legger til bønder ♟ hvit
    for i in range(0, 8):
        matrise[6][i] = '♟'
    #  Legger til tårn ♖ svart
    matrise[0][0] = '♖'
    matrise[0][7] = '♖'
    matrise[1][0] = '♖'
    #  Legger til tårn ♜ hvit
    matrise[7][0] = '♚'
    matrise[7][7] = '♜'
    matrise[6][0] = '♜'
    #  Legger til hest ♘ svart
    matrise[0][1] = '♘'
    matrise[0][6] = '♘'
    #  Legger til hest ♞ hvit
    matrise[7][1] = '♞'
    matrise[7][6] = '♞'
    #  Legger til løper ♗ svart
    matrise[0][2] = '♗'
    matrise[0][5] = '♗'
    matrise[1][6] = '♗'
    #  Legger til løper ♝ hvit
    matrise[7][2] = '♝'
    matrise[7][5] = '♝'
    #  Legger til konge ♔ og dronning ♕ svart
    matrise[0][4] = '♔'
    matrise[0][3] = '♕'
    #  Legger til konge ♚ og dronning ♛ svart
    matrise[7][4] = '⟤'
    matrise[7][3] = '♛'

    return matrise

def print_board(brett):

    for i in range(0, 8):
        for o in range(0, 7):
            print(f"|{brett[i][o]}", end='')
        print(f"|{brett[i][7]}|")
        #print('\n')
    """
    for i in range(0, 8):
        print(f"|{brett[i]}|")
    """


def get_piece(board, x, y):
    brikke = board[-y][x - 1]
    return brikke


def check_move_legal(brett, x, y, turn):
    sjekk = 0
    if x < 1 or x > 8:
        print("Ikkke gyldig koordinat")
    elif y < 1 or y > 8:
        print("Ikkkkke gyldig koordinat")
    else:
        sjekk = 1

    if turn == 'hvit':
        for i in range(0, len(hvit)):
            if brett[-y][x - 1] == hvit[i]:
                sjekk += 1
                break
            elif brett[-y][x-1] == '⟤':
                sjekk += 1
                break
        if sjekk == 1:
            print("Feil brikke bro")
    else:
        for i in range(0, len(svart)):
            if brett[-y][x - 1] == svart[i]:
                sjekk += 1
                break
            elif brett[-y][x-1] == '⟤':
                sjekk += 1
                break
        if sjekk == 1:
            print("Feil brikke bro")
    return sjekk


def move_piece(brett, x, y, x1, y1, brikke, brikke1):
    #  Flytter løper
    x2 = x
    y2 = y
    if brikke == '♝' or brikke == '♗':
        print(111)
        if abs(x-x1) == abs(y-y1):
            flytt = 1
            while x != x1:
                if x < x1:
                    x += 1
                else:
                    x -= 1
                if y < y1:
                    y += 1
                else:
                    y -= 1
                if brett[-y][x-1] != '⟤':
                    for i in range(0, len(hvit)):
                        if brett[-y][x - 1] == hvit[i] and brikke == '♝':
                            flytt = 0
                            print("NOE I VEIEN:", brett[-y][x-1])
                            break
                        elif brett[-y][x - 1] == svart[i] and brikke == '♗':
                            flytt = 0
                            print("NOE I VEIEN:", brett[-y][x-1])
                            break
                        if brett[-y][x - 1] == hvit[i] and brikke == '♗':
                            brett[-y][x - 1] = '♗'
                            flytt = 0
                            x1 = x
                            y1 = y
                            brett[-y2][x2 - 1] = '⟤'
                            break
                        if brett[-y][x - 1] == svart[i] and brikke == '♝':
                            brett[-y][x - 1] = '♝'
                            flytt = 0
                            x1 = x
                            y1 = y
                            brett[-y2][x2 - 1] = '⟤'
                            break
            if flytt == 1:
                if brikke == '♗':
                    brett[-y1][x1 - 1] = '♗'
                elif brikke == '♝':
                    brett[-y1][x1-1] = '♝'
                brett[-y2][x2 - 1] = '⟤'
        else:
            print("Ugyldig trekk")
    #  Flyyter tårn
    if brikke == '♜' or brikke == '♖':
        print(222)
        if (x == x1) or (y == y1):
            flytt = 1
            while (x != x1) or (y != y1):
                print(x, y, x1, y1)
                if x < x1:
                    x += 1
                elif x > x1:
                    x -= 1
                if y < y1:
                    y += 1
                elif y > y1:
                    y -= 1
                if brett[-y][x-1] != '⟤':
                    for i in range(0, len(hvit)):
                        if brett[-y][x - 1] == hvit[i] and brikke == '♜':
                            flytt = 0
                            print("NOE I VEIEN:", brett[-y][x-1])
                            break
                        elif brett[-y][x - 1] == svart[i] and brikke == '♖':
                            flytt = 0
                            print("NOE I VEIEN:", brett[-y][x-1])
                            break
                        if brett[-y][x - 1] == hvit[i] and brikke == '♖':
                            brett[-y][x - 1] = '♖'
                            flytt = 0
                            x1 = x
                            y1 = y
                            brett[-y2][x2 - 1] = '⟤'
                            break
                        if brett[-y][x - 1] == svart[i] and brikke == '♜':
                            brett[-y][x - 1] = '♜'
                            flytt = 0
                            x1 = x
                            y1 = y
                            brett[-y2][x2 - 1] = '⟤'
                            break
            if flytt == 1:
                if brikke == '♖':
                    brett[-y1][x1 - 1] = '♖'
                elif brikke == '♜':
                    brett[-y1][x1-1] = '♜'
                brett[-y2][x2 - 1] = '⟤'
        else:
            print("Ugyldig trekk")
    #  Flytter hest
    if brikke == '♞' or brikke == '♘':
        print(333, x+1, y+2, x1, y1)
        horse_move = False
        if (x+1 == x1) and (y+2 == y1):
            horse_move = True
        if (x-1 == x1) and (y+2 == y1):
            horse_move = True
        if (x+1 == x1) and (y-2 == y1):
            horse_move = True
        if (x-1 == x1) and (y-2 == y1):
            horse_move = True
        if (x+2 == x1) and (y+1 == y1):
            horse_move = True
        if (x+2 == x1) and (y-1 == y1):
            horse_move = True
        if (x-2 == x1) and (y+1 == y1):
            horse_move = True
        if (x-2 == x1) and (y-1 == y1):
            horse_move = True
        if horse_move:
            flytt = 1
            while (x != x1) or (y != y1):
                x = x1
                y = y1
                if brett[-y][x-1] != '⟤':
                    for i in range(0, len(hvit)):
                        if brett[-y][x - 1] == hvit[i] and brikke == '♞':
                            flytt = 0
                            print("NOE I VEIEN:", brett[-y][x-1])
                            break
                        elif brett[-y][x - 1] == svart[i] and brikke == '♘':
                            flytt = 0
                            print("NOE I VEIEN:", brett[-y][x-1])
                            break
            if flytt == 1:
                if brikke == '♘':
                    brett[-y1][x1 - 1] = '♘'
                elif brikke == '♞':
                    brett[-y1][x1-1] = '♞'
                brett[-y2][x2 - 1] = '⟤'
        else:
            print("Ugyldig trekk")
    #  Flytter dronning
    if brikke == '♛' or brikke == '♕':
        print(444)
        if (x == x1) or (y == y1):
            flytt = 1
            while (x != x1) or (y != y1):
                print(x, y, x1, y1)
                if x < x1:
                    x += 1
                elif x > x1:
                    x -= 1
                if y < y1:
                    y += 1
                elif y > y1:
                    y -= 1
                if brett[-y][x-1] != '⟤':
                    for i in range(0, len(hvit)):
                        if brett[-y][x - 1] == hvit[i] and brikke == '♛':
                            flytt = 0
                            print("NOE I VEIEN:", brett[-y][x-1])
                            break
                        elif brett[-y][x - 1] == svart[i] and brikke == '♕':
                            flytt = 0
                            print("NOE I VEIEN:", brett[-y][x-1])
                            break
                        if brett[-y][x - 1] == hvit[i] and brikke == '♕':
                            brett[-y][x - 1] = '♕'
                            flytt = 0
                            x1 = x
                            y1 = y
                            brett[-y2][x2 - 1] = '⟤'
                            break
                        if brett[-y][x - 1] == svart[i] and brikke == '♛':
                            brett[-y][x - 1] = '♛'
                            flytt = 0
                            x1 = x
                            y1 = y
                            brett[-y2][x2 - 1] = '⟤'
                            break
            if flytt == 1:
                if brikke == '♕':
                    brett[-y1][x1 - 1] = '♕'
                elif brikke == '♛':
                    brett[-y1][x1-1] = '♛'
                brett[-y2][x2 - 1] = '⟤'
        elif abs(x-x1) == abs(y-y1):
            print(212121)
            flytt = 1
            while x != x1:
                if x < x1:
                    x += 1
                else:
                    x -= 1
                if y < y1:
                    y += 1
                else:
                    y -= 1
                if brett[-y][x-1] != '⟤':
                    for i in range(0, len(hvit)):
                        if brett[-y][x - 1] == hvit[i] and brikke == '♛':
                            flytt = 0
                            print("NOE I VEIEN:", brett[-y][x-1])
                            break
                        elif brett[-y][x - 1] == svart[i] and brikke == '♕':
                            flytt = 0
                            print("NOE I VEIEN:", brett[-y][x-1])
                            break
                        if brett[-y][x - 1] == hvit[i] and brikke == '♕':
                            brett[-y][x - 1] = '♕'
                            flytt = 0
                            x1 = x
                            y1 = y
                            brett[-y2][x2 - 1] = '⟤'
                            break
                        if brett[-y][x - 1] == svart[i] and brikke == '♛':
                            brett[-y][x - 1] = '♛'
                            flytt = 0
                            x1 = x
                            y1 = y
                            brett[-y2][x2 - 1] = '⟤'
                            break
            if flytt == 1:
                if brikke == '♕':
                    brett[-y1][x1 - 1] = '♕'
                elif brikke == '♛':
                    brett[-y1][x1-1] = '♛'
                brett[-y2][x2 - 1] = '⟤'
        else:
            print("Ugyldig trekk")
    #  Flytter konge
    if brikke == '♚' or brikke == '♔':
        print(555)
        if (abs(x-x1) <= 1) and (abs(y-y1) <= 1):
            flytt = 1
            while (x != x1) or (y != y1):
                print(x, y, x1, y1)
                if x < x1:
                    x += 1
                elif x > x1:
                    x -= 1
                if y < y1:
                    y += 1
                elif y > y1:
                    y -= 1
                if brett[-y][x-1] != '⟤':
                    for i in range(0, len(hvit)):
                        if brett[-y][x - 1] == hvit[i] and brikke == '♚':
                            flytt = 0
                            print("NOE I VEIEN:", brett[-y][x-1])
                            break
                        elif brett[-y][x - 1] == svart[i] and brikke == '♔':
                            flytt = 0
                            print("NOE I VEIEN:", brett[-y][x-1])
                            break
                        if brett[-y][x - 1] == hvit[i] and brikke == '♔':
                            brett[-y][x - 1] = '♔'
                            flytt = 0
                            x1 = x
                            y1 = y
                            brett[-y2][x2 - 1] = '⟤'
                            break
                        if brett[-y][x - 1] == svart[i] and brikke == '♚':
                            brett[-y][x - 1] = '♚'
                            flytt = 0
                            x1 = x
                            y1 = y
                            brett[-y2][x2 - 1] = '⟤'
                            break
            if flytt == 1:
                if brikke == '♔':
                    brett[-y1][x1 - 1] = '♔'
                elif brikke == '♚':
                    brett[-y1][x1-1] = '♚'
                brett[-y2][x2 - 1] = '⟤'
        else:
            print("Ugyldig trekk")
    #  Flytter bonde hvit
    if brikke == '♟':
        print(676)
        flytt = 1
        if y == 2 and y1 == 4 and x == x1:
            if brett[-y1][x1 - 1] != '⟤':
                flytt = 0
                print("NOE I VEIEN:", brett[-y1][x1 - 1])
            elif brett[-y1+1][x1 - 1] != '⟤':
                flytt = 0
                print("NOE I VEIEN:", brett[-y1+1][x1 - 1])
            else:
                brett[-y1][x1 - 1] = '♟'
                brett[-y2][x2 - 1] = '⟤'
        elif x == x1 and (y1-y == 1):
            if brett[-y1][x1 - 1] != '⟤':
                flytt = 0
                print("NOE I VEIEN:", brett[-y1][x1 - 1])
            else:
                brett[-y1][x1 - 1] = '♟'
                brett[-y2][x2 - 1] = '⟤'
        elif (x+1 == x1) and (y1-y == 1):
            for i in range(0, len(hvit)):
                if brett[-y1][x1 - 1] == hvit[i]:
                    flytt = 0
                    print("NOE I VEIEN:", brett[-y1][x1 - 1])
                    break
            for i in range(0, len(svart)):
                if brett[-y1][x1 - 1] == svart[i]:
                    brett[-y1][x1 - 1] = '♟'
                    brett[-y2][x2 - 1] = '⟤'
                    break
        elif (x-1 == x1) and (y1-y == 1):
            for i in range(0, len(hvit)):
                if brett[-y1][x1 - 1] == hvit[i]:
                    flytt = 0
                    print("NOE I VEIEN:", brett[-y1][x1 - 1])
                    break
            for i in range(0, len(svart)):
                if brett[-y1][x1 - 1] == svart[i]:
                    brett[-y1][x1 - 1] = '♟'
                    brett[-y2][x2 - 1] = '⟤'
                    break
        else:
            print("Ugyldig trekk")
    #  Flytter bonde svart
    if brikke == '♙':
        print(676)
        flytt = 1
        if y == 7 and y1 == 5 and x == x1:
            if brett[-y1][x1 - 1] != '⟤':
                flytt = 0
                print("NOE I VEIEN:", brett[-y1][x1 - 1])
            elif brett[-y1-1][x1 - 1] != '⟤':
                flytt = 0
                print("NOE I VEIEN:", brett[-y1+1][x1 - 1])
            else:
                brett[-y1][x1 - 1] = '♙'
                brett[-y2][x2 - 1] = '⟤'
        elif x == x1 and (y-y1 == 1):
            if brett[-y1][x1 - 1] != '⟤':
                flytt = 0
                print("NOE I VEIEN:", brett[-y1][x1 - 1])
            else:
                brett[-y1][x1 - 1] = '♙'
                brett[-y2][x2 - 1] = '⟤'
        elif (x+1 == x1) and (y-y1 == 1):
            for i in range(0, len(svart)):
                if brett[-y1][x1 - 1] == svart[i]:
                    flytt = 0
                    print("NOE I VEIEN:", brett[-y1][x1 - 1])
                    break
            for i in range(0, len(hvit)):
                if brett[-y1][x1 - 1] == hvit[i]:
                    brett[-y1][x1 - 1] = '♙'
                    brett[-y2][x2 - 1] = '⟤'
                    break
        elif (x-1 == x1) and (y-y1 == 1):
            for i in range(0, len(svart)):
                if brett[-y1][x1 - 1] == svart[i]:
                    flytt = 0
                    print("NOE I VEIEN:", brett[-y1][x1 - 1])
                    break
            for i in range(0, len(svart)):
                if brett[-y1][x1 - 1] == svart[i]:
                    brett[-y1][x1 - 1] = '♙'
                    brett[-y2][x2 - 1] = '⟤'
                    break
        else:
            print("Ugyldig trekk")

def sjakk_sjekk(brett):
    for i in range(0, len(brett)):
        for o in range(0, 8):
            if brett[i][o] == '♚':
                hvit_x = o+1
                hvit_y = 8-i
                print(i, o, f"x={hvit_x}, y={hvit_y}")
    #  sjekker for løper og dronning
    sjakk = False
    x1 = hvit_x
    y1 = hvit_y
    while True:
        x1 += 1
        y1 += 1
        if (x1 < 1 or x1 > 8) or (y1 < 1 or y1 > 8):
            break
        for i in range(0, len(hvit)):
            if brett[-y1][x1 - 1] == hvit[i]:
                print(89898)
                sjakk = False
                break
        else:
            if brett[-y1][x1 - 1] == '♕' or brett[-y1][x1 - 1] == '♗':
                print(brett[-y1][x1 - 1])
                sjakk = True
            continue
        break
    x1 = hvit_x
    y1 = hvit_y
    while True:
        x1 -= 1
        y1 += 1
        if (x1 < 1 or x1 > 8) or (y1 < 1 or y1 > 8):
            break
        if brett[-y1][x1 - 1] == '♕' or brett[-y1][x1 - 1] == '♗':
            print(brett[-y1][x1 - 1])
            sjakk = True
    x1 = hvit_x
    y1 = hvit_y
    while True:
        x1 += 1
        y1 -= 1
        if (x1 < 1 or x1 > 8) or (y1 < 1 or y1 > 8):
            break
        if brett[-y1][x1 - 1] == '♕' or brett[-y1][x1 - 1] == '♗':
            print(brett[-y1][x1 - 1])
            sjakk = True
    x1 = hvit_x
    y1 = hvit_y
    while True:
        x1 -= 1
        y1 -= 1
        if (x1 < 1 or x1 > 8) or (y1 < 1 or y1 > 8):
            break
        if brett[-y1][x1 - 1] == '♕' or brett[-y1][x1 - 1] == '♗':
            print(brett[-y1][x1 - 1])
            sjakk = True
    #  Sjekker for tårn og dronning
    x1 = hvit_x
    y1 = hvit_y
    while True:
        x1 += 1
        if (x1 < 1 or x1 > 8) or (y1 < 1 or y1 > 8):
            break
        if brett[-y1][x1 - 1] == '♕' or brett[-y1][x1 - 1] == '♖':
            print(brett[-y1][x1 - 1])
            sjakk = True
    x1 = hvit_x
    y1 = hvit_y
    while True:
        x1 -= 1
        if (x1 < 1 or x1 > 8) or (y1 < 1 or y1 > 8):
            break
        if brett[-y1][x1 - 1] == '♕' or brett[-y1][x1 - 1] == '♖':
            print(brett[-y1][x1 - 1])
            sjakk = True
    x1 = hvit_x
    y1 = hvit_y
    while True:
        y1 += 1
        if (x1 < 1 or x1 > 8) or (y1 < 1 or y1 > 8):
            break
        if brett[-y1][x1 - 1] == '♕' or brett[-y1][x1 - 1] == '♖':
            print(brett[-y1][x1 - 1])
            sjakk = True
    x1 = hvit_x
    y1 = hvit_y
    while True:
        y1 -= 1
        if (x1 < 1 or x1 > 8) or (y1 < 1 or y1 > 8):
            break
        if brett[-y1][x1 - 1] == '♕' or brett[-y1][x1 - 1] == '♖':
            print(brett[-y1][x1 - 1])
            sjakk = True
    #  Sjekker for hest
    x1 = hvit_x
    y1 = hvit_y


    return sjakk





def main():
    brett = make_board()
    print_board(brett)
    #print(get_piece(brett, 5, 8))
    turn = 'hvit'
    while True:
        print(f"{turn} sin tur. Velg brikke")
        x = input("x:")
        y = input("y:")
        if x == "":
            break
        x = int(x)
        y = int(y)
        if check_move_legal(brett, x, y, turn) == 2:
            brikke = get_piece(brett, x, y)
            if brikke == '⟤':
                print("Der er det ingenting")
            else:
                print(brikke)
                print(f"Hvor vil du flytte {brikke}?")
                x1 = input("x:")
                y1 = input("y:")
                if x == "":
                    break
                x1 = int(x1)
                y1 = int(y1)
                if turn == 'hvit':
                    turn = 'svart'
                else:
                    turn = 'hvit'
                if check_move_legal(brett, x1, y1, turn) == 2:
                    brikke1 = get_piece(brett, x1, y1)
                    print(brikke1)
                    move_piece(brett, x, y, x1, y1, brikke, brikke1)
                    print_board(brett)
        else:
            if turn == 'hvit':
                turn = 'svart'
            else:
                turn = 'hvit'
        if sjakk_sjekk(brett):
            print("SJAKK")

#brett = make_board()
#print_board(brett)
main()