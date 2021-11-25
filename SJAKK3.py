hvit = ['♜', '♝', '♞', '♛', '♚', '♟']
svart = ['♖', '♗', '♘', '♕', '♔', '♙']
begge = ['♜', '♝', '♞', '♛', '♚', '♟', '♖', '♗', '♘', '♕', '♔', '♙']
abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
hvit_x = 5
hvit_y = 1
svart_x = 5
svart_y = 8

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
    #  Legger til tårn ♜ hvit
    matrise[7][0] = '♜'
    matrise[7][7] = '♜'
    #  Legger til hest ♘ svart
    matrise[0][1] = '♘'
    matrise[0][6] = '♘'
    #  Legger til hest ♞ hvit
    matrise[7][1] = '♞'
    matrise[7][6] = '♞'
    #  Legger til løper ♗ svart
    matrise[0][2] = '♗'
    matrise[0][5] = '♗'
    #  Legger til løper ♝ hvit
    matrise[7][2] = '♝'
    matrise[7][5] = '♝'
    #  Legger til konge ♔ og dronning ♕ svart
    matrise[0][4] = '♔'
    matrise[0][3] = '♕'
    #  Legger til konge ♚ og dronning ♛ svart
    matrise[7][4] = '♚'
    matrise[7][3] = '♛'

    return matrise

def print_board(brett):

    for i in range(0, 8):
        print(8-i, end="")
        for o in range(0, 7):
            print(f"|{brett[i][o]}", end='')
        print(f"|{brett[i][7]}|")
    print(" ", end="")
    for i in range(0, len(abc)):
        print(abc[i], end="  ")
    print("\n")


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


def hvit_bonde_skifte(brett, x, y):
    print("Hva vil du skifte til?")
    print("d = dronning, l = løper, t = tårn, h = hest, b = bonde")
    valg = input("::")
    if valg == 'd':
        brett[-y][x - 1] = '♛'
    if valg == 'l':
        brett[-y][x - 1] = '♝'
    if valg == 't':
        brett[-y][x - 1] = '♜'
    if valg == 'h':
        brett[-y][x - 1] = '♞'
    if valg == 'b':
        brett[-y][x - 1] = '♟'


def svart_bonde_skifte(brett, x, y):
    print("Hva vil du skifte til?")
    print("d = dronning, l = løper, t = tårn, h = hest, b = bonde")
    valg = input("::")
    if valg == 'd':
        brett[-y][x - 1] = '♕'
    if valg == 'l':
        brett[-y][x - 1] = '♗'
    if valg == 't':
        brett[-y][x - 1] = '♖'
    if valg == 'h':
        brett[-y][x - 1] = '♘'
    if valg == 'b':
        brett[-y][x - 1] = '♙'


def move_piece(brett, x, y, x1, y1, brikke, brikke1):
    #  Flytter løper
    x2 = x
    y2 = y
    if brikke == '♝' or brikke == '♗':
        #print(111)
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
        #print(222)
        if (x == x1) or (y == y1):
            flytt = 1
            while (x != x1) or (y != y1):
                #print(x, y, x1, y1)
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
        #print(333, x+1, y+2, x1, y1)
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
        #print(444)
        if (x == x1) or (y == y1):
            flytt = 1
            while (x != x1) or (y != y1):
                #print(x, y, x1, y1)
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
            #print(212121)
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
        #print(555)
        if (abs(x-x1) <= 1) and (abs(y-y1) <= 1):
            flytt = 1
            while (x != x1) or (y != y1):
                #print(x, y, x1, y1)
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
        #print(676)
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
                if y1 == 8:
                    hvit_bonde_skifte(brett, x1, y1)
        elif x == x1 and (y1-y == 1):
            if brett[-y1][x1 - 1] != '⟤':
                flytt = 0
                print("NOE I VEIEN:", brett[-y1][x1 - 1])
            else:
                brett[-y1][x1 - 1] = '♟'
                brett[-y2][x2 - 1] = '⟤'
                if y1 == 8:
                    hvit_bonde_skifte(brett, x1, y1)
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
                    if y1 == 8:
                        hvit_bonde_skifte(brett, x1, y1)
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
                    if y1 == 8:
                        hvit_bonde_skifte(brett, x1, y1)
                    break
        else:
            print("Ugyldig trekk")
    #  Flytter bonde svart
    if brikke == '♙':
        #print(767)
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
                if y1 == 1:
                    svart_bonde_skifte(brett, x1, y1)
        elif x == x1 and (y-y1 == 1):
            if brett[-y1][x1 - 1] != '⟤':
                flytt = 0
                print("NOE I VEIEN:", brett[-y1][x1 - 1])
            else:
                brett[-y1][x1 - 1] = '♙'
                brett[-y2][x2 - 1] = '⟤'
                if y1 == 1:
                    svart_bonde_skifte(brett, x1, y1)
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
                    if y1 == 1:
                        svart_bonde_skifte(brett, x1, y1)
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
                    if y1 == 1:
                        svart_bonde_skifte(brett, x1, y1)
                    break
        else:
            print("Ugyldig trekk")


def finn_hvit_konge(brett):
    for i in range(0, len(brett)):
        for o in range(0, 8):
            if brett[i][o] == '♚':
                hvit_x = o+1
                hvit_y = 8-i
                #print(i, o, f"x={hvit_x}, y={hvit_y}", '♚')
    return hvit_x, hvit_y


def finn_svart_konge(brett):
    for i in range(0, len(brett)):
        for o in range(0, 8):
            if brett[i][o] == '♔':
                svart_x = o+1
                svart_y = 8-i
                #print(i, o, f"x={svart_x}, y={svart_y}", '♔')
    return svart_x, svart_y


def sjakk_sjekk_hvit(brett, x_sjekk, y_sjekk):
    hvit_x = x_sjekk
    hvit_y = y_sjekk
    #  sjekker for dronning og tårn
    fare = 1
    sjakk = 0
    for y in range(hvit_y-1, 0, -1):
        if brett[-y][hvit_x - 1] == '♕' or brett[-y][hvit_x - 1] == '♖':
            print(brett[-y][hvit_x - 1], "SJAKK")
            return True
        for i in range(0, len(begge)):
            if brett[-y][hvit_x - 1] == begge[i]:
                fare = 0
                break
        if fare == 0:
            break
    fare = 1
    for y in range(hvit_y+1, 9):
        if brett[-y][hvit_x - 1] == '♕' or brett[-y][hvit_x - 1] == '♖':
            print(brett[-y][hvit_x - 1], "SJAKK")
            return True
        for i in range(0, len(begge)):
            if brett[-y][hvit_x - 1] == begge[i]:
                fare = 0
                break
        if fare == 0:
            break
    fare = 1
    for x in range(hvit_x-1, 0, -1):
        if brett[-hvit_y][x - 1] == '♕' or brett[-hvit_y][x - 1] == '♖':
            print(brett[-hvit_y][x - 1], "SJAKK")
            return True
        for i in range(0, len(begge)):
            if brett[-hvit_y][x - 1] == begge[i]:
                fare = 0
                break
        if fare == 0:
            break
    fare = 1
    for x in range(hvit_x+1, 9):
        if brett[-hvit_y][x - 1] == '♕' or brett[-hvit_y][x - 1] == '♖':
            print(brett[-hvit_y][x - 1], "SJAKK")
            return True
        for i in range(0, len(begge)):
            if brett[-hvit_y][x - 1] == begge[i]:
                fare = 0
                break
        if fare == 0:
            break
    #  Sjekker for dronning og løper
    fare = 1
    for x in range(hvit_x + 1, 9):
        if (x < 1 or x > 8) or (hvit_y+x-hvit_x < 1 or hvit_y+x-hvit_x > 8):
            break
        if brett[-(hvit_y+x-hvit_x)][x - 1] == '♕' or brett[-(hvit_y+x-hvit_x)][x - 1] == '♗':
            print(brett[-(hvit_y+x-hvit_x)][x - 1], "SJAKK")
            return True
        for i in range(0, len(begge)):
            if brett[-(hvit_y+x-hvit_x)][x - 1] == begge[i]:
                fare = 0
                break
        if fare == 0:
            break
    fare = 1
    for x in range(hvit_x-1, 0, -1):
        if (x < 1 or x > 8) or (hvit_y+hvit_x-x < 1 or hvit_y+hvit_x-x > 8):
            break
        if brett[-(hvit_y+hvit_x-x)][x - 1] == '♕' or brett[-(hvit_y+hvit_x-x)][x - 1] == '♗':
            print(brett[-(hvit_y+hvit_x-x)][x - 1], "SJAKK")
            return True
        for i in range(0, len(begge)):
            if brett[-(hvit_y+hvit_x-x)][x - 1] == begge[i]:
                fare = 0
                break
        if fare == 0:
            break
    fare = 1
    for x in range(hvit_x - 1, 0, -1):
        if (x < 1 or x > 8) or (hvit_y-hvit_x+x < 1 or hvit_y-hvit_x+x > 8):
            break
        if brett[-(hvit_y-hvit_x+x)][x - 1] == '♕' or brett[-(hvit_y-hvit_x+x)][x - 1] == '♗':
            print(brett[-(hvit_y-hvit_x+x)][x - 1], "SJAKK")
            return True
        for i in range(0, len(begge)):
            if brett[-(hvit_y-hvit_x+x)][x - 1] == begge[i]:
                fare = 0
                break
        if fare == 0:
            break
    fare = 1
    for x in range(hvit_x + 1, 9):
        if (x < 1 or x > 8) or (hvit_y-x+hvit_x < 1 or hvit_y-x+hvit_x > 8):
            break
        if brett[-(hvit_y-x+hvit_x)][x - 1] == '♕' or brett[-(hvit_y-x+hvit_x)][x - 1] == '♗':
            print(brett[-(hvit_y-x+hvit_x)][x - 1], "SJAKK")
            return True
        for i in range(0, len(begge)):
            if brett[-(hvit_y-x+hvit_x)][x - 1] == begge[i]:
                fare = 0
                break
        if fare == 0:
            break
    #  Sjekker for hest
    if (hvit_x+1 < 9) and (hvit_y+2 < 9):
        if brett[-(hvit_y+2)][hvit_x+1 - 1] == '♘':
            print(brett[-(hvit_y+2)][hvit_x+1 - 1], "SJAKK")
            return True
    if (hvit_x-1 > 0) and (hvit_y+2 < 9):
        if brett[-(hvit_y+2)][hvit_x-1 - 1] == '♘':
            print(brett[-(hvit_y+2)][hvit_x-1 - 1], "SJAKK")
            return True
    if (hvit_x-1 > 0) and (hvit_y-2 > 0):
        if brett[-(hvit_y-2)][hvit_x-1 - 1] == '♘':
            print(brett[-(hvit_y-2)][hvit_x-1 - 1], "SJAKK")
            return True
    if (hvit_x+1 < 9) and (hvit_y-2 > 0):
        if brett[-(hvit_y-2)][hvit_x+1 - 1] == '♘':
            print(brett[-(hvit_y-2)][hvit_x+1 - 1], "SJAKK")
            return True

    if (hvit_x+2 < 9) and (hvit_y+1 < 9):
        if brett[-(hvit_y+1)][hvit_x+2 - 1] == '♘':
            print(brett[-(hvit_y+1)][hvit_x+2 - 1], "SJAKK")
            return True
    if (hvit_x-2 > 0) and (hvit_y+1 < 9):
        if brett[-(hvit_y+1)][hvit_x-2 - 1] == '♘':
            print(brett[-(hvit_y+1)][hvit_x-2 - 1], "SJAKK")
            return True
    if (hvit_x-2 > 0) and (hvit_y-1 > 0):
        if brett[-(hvit_y-1)][hvit_x-2 - 1] == '♘':
            print(brett[-(hvit_y-1)][hvit_x-2 - 1], "SJAKK")
            return True
    if (hvit_x+2 < 9) and (hvit_y-1 > 0):
        if brett[-(hvit_y-1)][hvit_x+2 - 1] == '♘':
            print(brett[-(hvit_y-1)][hvit_x+2 - 1], "SJAKK")
            return True
    #  Sjekker for bønder
    if (hvit_x+1 < 9) and (hvit_y+1 < 9):
        if brett[-(hvit_y+1)][hvit_x+1 - 1] == '♙':
            print(brett[-(hvit_y+1)][hvit_x+1 - 1], "SJAKK")
            return True
    if (hvit_x-1 < 9) and (hvit_y+1 < 9):
        if brett[-(hvit_y+1)][hvit_x-1 - 1] == '♙':
            print(brett[-(hvit_y+1)][hvit_x-1 - 1], "SJAKK")
            return True
    #  Legg inn for konge også


def sjakk_sjekk_svart(brett, x_sjekk, y_sjekk):
    svart_x = x_sjekk
    svart_y = y_sjekk
    #  sjekker for dronning og tårn
    fare = 1
    sjakk = 0
    for y in range(svart_y -1, 0, -1):
        if brett[-y][svart_x - 1] == '♛' or brett[-y][svart_x - 1] == '♜':
            print(brett[-y][svart_x - 1], "SJAKK")
            return True
        for i in range(0, len(begge)):
            if brett[-y][svart_x - 1] == begge[i]:
                fare = 0
                break
        if fare == 0:
            break
    fare = 1
    for y in range(svart_y+1, 9):
        if brett[-y][svart_x - 1] == '♛' or brett[-y][svart_x - 1] == '♜':
            print(brett[-y][svart_x - 1], "SJAKK")
            return True
        for i in range(0, len(begge)):
            if brett[-y][svart_x - 1] == begge[i]:
                fare = 0
                break
        if fare == 0:
            break
    fare = 1
    for x in range(svart_x-1, 0, -1):
        if brett[-svart_y][x - 1] == '♛' or brett[-svart_y][x - 1] == '♜':
            print(brett[-svart_y][x - 1], "SJAKK")
            return True
        for i in range(0, len(begge)):
            if brett[-svart_y][x - 1] == begge[i]:
                fare = 0
                break
        if fare == 0:
            break
    fare = 1
    for x in range(svart_x+1, 9):
        if brett[-svart_y][x - 1] == '♛' or brett[-svart_y][x - 1] == '♜':
            print(brett[-svart_y][x - 1], "SJAKK")
            return True
        for i in range(0, len(begge)):
            if brett[-svart_y][x - 1] == begge[i]:
                fare = 0
                break
        if fare == 0:
            break
    #  Sjekker for dronning og løper
    fare = 1
    for x in range(svart_x + 1, 9):
        if (x < 1 or x > 8) or (svart_y+x-svart_x < 1 or svart_y+x-svart_x > 8):
            break
        if brett[-(svart_y+x-svart_x)][x - 1] == '♛' or brett[-(svart_y+x-svart_x)][x - 1] == '♝':
            print(brett[-(svart_y+x-svart_x)][x - 1], "SJAKK")
            return True
        for i in range(0, len(begge)):
            if brett[-(svart_y+x-svart_x)][x - 1] == begge[i]:
                fare = 0
                break
        if fare == 0:
            break
    fare = 1
    for x in range(svart_x-1, 0, -1):
        if (x < 1 or x > 8) or (svart_y+svart_x-x < 1 or svart_y+svart_x-x > 8):
            break
        if brett[-(svart_y+svart_x-x)][x - 1] == '♛' or brett[-(svart_y+svart_x-x)][x - 1] == '♝':
            print(brett[-(svart_y+svart_x-x)][x - 1], "SJAKK")
            return True
        for i in range(0, len(begge)):
            if brett[-(svart_y+svart_x-x)][x - 1] == begge[i]:
                fare = 0
                break
        if fare == 0:
            break
    fare = 1
    for x in range(svart_x - 1, 0, -1):
        if (x < 1 or x > 8) or (svart_y-svart_x+x < 1 or svart_y-svart_x+x > 8):
            break
        if brett[-(svart_y-svart_x+x)][x - 1] == '♛' or brett[-(svart_y-svart_x+x)][x - 1] == '♝':
            print(brett[-(svart_y-svart_x+x)][x - 1], "SJAKK")
            return True
        for i in range(0, len(begge)):
            if brett[-(svart_y-svart_x+x)][x - 1] == begge[i]:
                fare = 0
                break
        if fare == 0:
            break
    fare = 1
    for x in range(svart_x + 1, 9):
        if (x < 1 or x > 8) or (svart_y-x+svart_x < 1 or svart_y-x+svart_x > 8):
            break
        if brett[-(svart_y-x+svart_x)][x - 1] == '♛' or brett[-(svart_y-x+svart_x)][x - 1] == '♝':
            print(brett[-(svart_y-x+svart_x)][x - 1], "SJAKK")
            return True
        for i in range(0, len(begge)):
            if brett[-(svart_y-x+svart_x)][x - 1] == begge[i]:
                fare = 0
                break
        if fare == 0:
            break
    #  Sjekker for hest
    if (svart_x+1 < 9) and (svart_y+2 < 9):
        if brett[-(svart_y+2)][svart_x+1 - 1] == '♞':
            print(brett[-(svart_y+2)][svart_x+1 - 1], "SJAKK")
            return True
    if (svart_x-1 > 0) and (svart_y+2 < 9):
        if brett[-(svart_y+2)][svart_x-1 - 1] == '♞':
            print(brett[-(svart_y+2)][svart_x-1 - 1], "SJAKK")
            return True
    if (svart_x-1 > 0) and (svart_y-2 > 0):
        if brett[-(svart_y-2)][svart_x-1 - 1] == '♞':
            print(brett[-(svart_y-2)][svart_x-1 - 1], "SJAKK")
            return True
    if (svart_x+1 < 9) and (svart_y-2 > 0):
        if brett[-(svart_y-2)][svart_x+1 - 1] == '♞':
            print(brett[-(svart_y-2)][svart_x+1 - 1], "SJAKK")
            return True

    if (svart_x+2 < 9) and (svart_y+1 < 9):
        if brett[-(svart_y+1)][svart_x+2 - 1] == '♞':
            print(brett[-(svart_y+1)][svart_x+2 - 1], "SJAKK")
            return True
    if (svart_x-2 > 0) and (svart_y+1 < 9):
        if brett[-(svart_y+1)][svart_x-2 - 1] == '♞':
            print(brett[-(svart_y+1)][svart_x-2 - 1], "SJAKK")
            return True
    if (svart_x-2 > 0) and (svart_y-1 > 0):
        if brett[-(svart_y-1)][svart_x-2 - 1] == '♞':
            print(brett[-(svart_y-1)][svart_x-2 - 1], "SJAKK")
            return True
    if (svart_x+2 < 9) and (svart_y-1 > 0):
        if brett[-(svart_y-1)][svart_x+2 - 1] == '♞':
            print(brett[-(svart_y-1)][svart_x+2 - 1], "SJAKK")
            return True
    #  Sjekker for bønder
    if (svart_x+1 < 9) and (svart_y-1 < 9):
        if brett[-(svart_y-1)][svart_x+1 - 1] == '♟':
            print(brett[-(svart_y-1)][svart_x+1 - 1], "SJAKK")
            return True
    if (svart_x-1 < 9) and (svart_y-1 < 9):
        if brett[-(svart_y-1)][svart_x-1 - 1] == '♟':
            print(brett[-(svart_y-1)][svart_x-1 - 1], "SJAKK")
            return True
    #  Legg inn for konge også


def hvit_konge_sjekk(brett, x, y):
    if x > 8 or x < 1 or y > 8 or y < 1:
        return False
    elif sjakk_sjekk_hvit(brett, x, y):
        return False
    for i in range(0, len(hvit)):
        if brett[-y][x-1] == hvit[i]:
            return False
    return True


def svart_konge_sjekk(brett, x, y):
    if x > 8 or x < 1 or y > 8 or y < 1:
        return False
    elif sjakk_sjekk_svart(brett, x, y):
        return False
    for i in range(0, len(svart)):
        if brett[-y][x-1] == svart[i]:
            return False
    return True



def sjakk_matt_hvit(brett, hvit_x, hvit_y):
    matt = 8
    if hvit_konge_sjekk(brett, hvit_x, hvit_y+1):
        matt -= 1
    if hvit_konge_sjekk(brett, hvit_x+1, hvit_y + 1):
        matt -= 1
    if hvit_konge_sjekk(brett, hvit_x+1, hvit_y):
        matt -= 1
    if hvit_konge_sjekk(brett, hvit_x+1, hvit_y-1):
        matt -= 1
    if hvit_konge_sjekk(brett, hvit_x, hvit_y-1):
        matt -= 1
    if hvit_konge_sjekk(brett, hvit_x-1, hvit_y-1):
        matt -= 1
    if hvit_konge_sjekk(brett, hvit_x-1, hvit_y):
        matt -= 1
    if hvit_konge_sjekk(brett, hvit_x-1, hvit_y+1):
        matt -= 1
    if matt == 8:
        return True
    else:
        return False


def sjakk_matt_svart(brett, svart_x, svart_y):
    matt = 8
    if svart_konge_sjekk(brett, svart_x, svart_y+1):
        matt -= 1
    if svart_konge_sjekk(brett, svart_x+1, svart_y + 1):
        matt -= 1
    if svart_konge_sjekk(brett, svart_x+1, svart_y):
        matt -= 1
    if svart_konge_sjekk(brett, svart_x+1, svart_y-1):
        matt -= 1
    if svart_konge_sjekk(brett, svart_x, svart_y-1):
        matt -= 1
    if svart_konge_sjekk(brett, svart_x-1, svart_y-1):
        matt -= 1
    if svart_konge_sjekk(brett, svart_x-1, svart_y):
        matt -= 1
    if svart_konge_sjekk(brett, svart_x-1, svart_y+1):
        matt -= 1
    if matt == 8:
        return True
    else:
        return False


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
        for i in range(0, len(abc)):
            if x == abc[i]:
                x = i+1
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
                for i in range(0, len(abc)):
                    if x1 == abc[i]:
                        x1 = i + 1
                x1 = int(x1)
                y1 = int(y1)
                if turn == 'hvit':
                    turn = 'svart'
                else:
                    turn = 'hvit'
                if check_move_legal(brett, x1, y1, turn) == 2:
                    brikke1 = get_piece(brett, x1, y1)
                    print(brikke1)
                    if brikke == '♚':
                        brett[-y][x - 1] = '⟤'
                        if hvit_konge_sjekk(brett, x1, y1):
                            move_piece(brett, x, y, x1, y1, brikke, brikke1)
                        else:
                            print("Ikke sett deg selv i sjakk mann")
                            brett[-y][x - 1] = '♚'
                    elif brikke == '♔':
                        brett[-y][x - 1] = '⟤'
                        if svart_konge_sjekk(brett, x1, y1):
                            move_piece(brett, x, y, x1, y1, brikke, brikke1)
                        else:
                            print("Ikke sett deg selv i sjakk mann")
                            brett[-y][x - 1] = '♔'
                    else:
                        move_piece(brett, x, y, x1, y1, brikke, brikke1)
                    print_board(brett)
        else:
            if turn == 'hvit':
                turn = 'svart'
            else:
                turn = 'hvit'
        hvit_x, hvit_y = finn_hvit_konge(brett)
        if sjakk_sjekk_hvit(brett, hvit_x, hvit_y):
            print("SJAKK MOT HVIT")
            brett[-hvit_y][hvit_x-1] = '⟤'
            if sjakk_matt_hvit(brett, hvit_x, hvit_y):
                print("SJAKK MATT MOT HVIT")
            brett[-hvit_y][hvit_x - 1] = '♚'
        svart_x, svart_y = finn_svart_konge(brett)
        if sjakk_sjekk_svart(brett, svart_x, svart_y):
            print("SJAKK MOT SVART")
            brett[-svart_y][svart_x - 1] = '⟤'
            if sjakk_matt_svart(brett, svart_x, svart_y):
                print("SJAKK MATT MOT SVART")
            brett[-svart_y][svart_x - 1] = '♔'

#brett = make_board()
#print_board(brett)
main()