import random
import time
import keyboard
import os

hand_liste = []
hand1_liste = []
kastHedda_liste = []
avHver_liste = []
scoreboard_liste_liste = []
current_player = 1


hand = []
hand1 = []
kastHedda = 0
avHver = [1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0]
scoreboard_liste = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
round_counter = 1
round_name = ["enere", "toere", "treere", "firere", "femere", "seksere", "Sum", "Bonus",
              "1 par", "2 par", "3 like", "4 like", "Liten straight", "Stor straight", "Hus", "Sjanse", "Yatzee", "Totalsum"]

global antallSpillere
antallSpillere = int(input("Hvor mange spillere?"))
for i in range(0, antallSpillere):
    hand_liste.append([])
    hand1_liste.append([])
    kastHedda_liste.append(0)
    avHver_liste.append([1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0])
    scoreboard_liste_liste.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
for u in range(1, antallSpillere+1):
    print("Navn", u, end="")
    navn = input(":")
    scoreboard_liste_liste[u-1].append(navn)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def kastTerning(x):
    print("Press SPACE to throw!")
    global kastHedda_liste
    while True:
        if keyboard.is_pressed("SPACE"):
            #rint(888, avHver)
            break
    kastHedda_liste[current_player-1] += 1
    for i in range(0, x):
        hand_liste[current_player-1].append(random.randint(1, 6))
    print("\nKast:", hand_liste[current_player-1])
    if kastHedda_liste[current_player-1] >= 2:
        for i in range(0, len(newHand)):
            hand1_liste[current_player-1].append(newHand[i])
        for u in range(0, len(hand_liste[current_player-1])):
            hand1_liste[current_player-1].append(hand_liste[current_player-1][u])
        print("Nåværende hånd:", hand1_liste[current_player-1])
        antallHver(hand1_liste[current_player-1])
    else:
        antallHver(hand_liste[current_player-1])
    print("Antall kast: ", kastHedda_liste[current_player-1])
    decicions()


def antallHver(rar):
    global avHver_liste
    avHver_liste[current_player-1] = [1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0]
    for u in range(0, len(rar)):
        for o in range(1, 7):
            if rar[u] == o:
                avHver_liste[current_player-1][rar[u]*2 - 1] += 1
    #print("", avHver, "\n")

def scoreboard():
    """
    for i in range(0, 18):
        print("---------------")
        if i == 7:
            if scoreboard_liste[i-1] > 42:
                scoreboard_liste[i] += 50
                print("|", round_name[i], "|", scoreboard_liste[i], "|")
            else:
                print("|", round_name[i], "|", 0, "|")
        else:
            print("|", round_name[i], "|", scoreboard_liste[i], "|")
    """
    for i in range(0, 18):
        print("\n-----------------------")
        print("|", round_name[i], "|", end=" ")
        if i == 7:
            if scoreboard_liste_liste[current_player-1][i - 1] > 42:
                scoreboard_liste_liste[current_player-1][i] += 50
                for u in range(0, antallSpillere):
                    print(scoreboard_liste_liste[u][i], "|", end=" ")
            else:
                for u in range(0, antallSpillere):
                    print(0, "|", end=" ")
        else:
            for u in range(0, antallSpillere):
                print(scoreboard_liste_liste[u][i], "|", end=" ")
    print("\n--------------\n")

def runde1(x):
    global round_counter
    global scoreboard_liste_liste
    if x == 0:
        scoreboard()
        print("\n--- Runde ", round_counter, "! ---")
        print("Spiller:", scoreboard_liste_liste[current_player-1][-1])
        if round_counter <= 6:
            print("Du skal ha", round_name[round_counter-1], ":) ")
        else:
            print("Du skal ha", round_name[round_counter + 1], ":) ")
        kastTerning(5)



    elif x == 1:
        if round_counter <= 6:  # 1-6
            #print(avHver_liste[current_player-1])
            for i in range(0, len(hand1_liste[current_player-1])):
                #print(1, scoreboard_liste_liste)
                if hand1_liste[current_player-1][i] == round_counter:
                    scoreboard_liste_liste[current_player-1][round_counter-1] += round_counter
                    scoreboard_liste_liste[current_player - 1][6] += round_counter
                #print(2, scoreboard_liste_liste)




        elif round_counter == 7:  # 1 par
            for i in range(-1, len(avHver_liste[current_player-1])*-1, -2):
                if avHver_liste[current_player-1][i] >= 2:
                    scoreboard_liste_liste[current_player - 1][round_counter+1] = avHver_liste[current_player-1][i-1]*2
                    break
        elif round_counter == 8:  # 2 par
            for i in range(-1, len(avHver_liste[current_player-1]) * -1, -2):
                if avHver_liste[current_player-1][i] >= 2:
                    #print(avHver_liste[current_player-1][i - 1], avHver_liste[current_player-1][i], i)
                    for u in range(i - 2, len(avHver_liste[current_player-1]) * -1, -2):
                        if avHver_liste[current_player-1][u] >= 2:
                            #print(avHver_liste[current_player-1][u - 1], avHver_liste[current_player-1][u], u)
                            scoreboard_liste_liste[current_player - 1][round_counter+1] += avHver_liste[current_player-1][u-1]*2
                            scoreboard_liste_liste[current_player - 1][round_counter + 1] += avHver_liste[current_player-1][i - 1] * 2
                            break
                    break
        elif round_counter == 9:  # 3 like
            for i in range(-1, len(avHver_liste[current_player-1])*-1, -2):
                if avHver_liste[current_player-1][i] >= 3:
                    scoreboard_liste_liste[current_player - 1][round_counter+1] = avHver_liste[current_player-1][i-1]*3
                    break
        elif round_counter == 10: # 4 like
            for i in range(-1, len(avHver_liste[current_player-1])*-1, -2):
                if avHver_liste[current_player-1][i] >= 4:
                    scoreboard_liste_liste[current_player - 1][round_counter+1] = avHver_liste[current_player-1][i-1]*4
                    break
        elif round_counter == 11:  # Liten straight
            ha = 0
            for i in range(1, 6):
                for u in range(0, len(hand1_liste[current_player-1])):
                    if hand1_liste[current_player-1][u] == i:
                        ha += 1
                        break
            #print(ha)
            if ha >= 5:
                #print("ya")
                scoreboard_liste_liste[current_player - 1][round_counter+1] = 15
        elif round_counter == 12:  # Stor straight
            hb = 0
            for i in range(2, 7):
                for u in range(0, len(hand1_liste[current_player-1])):
                    if hand1_liste[current_player-1][u] == i:
                        hb += 1
                        break
            #print(hb)
            if hb >= 5:
                #print("ya")
                scoreboard_liste_liste[current_player - 1][round_counter + 1] = 20
        elif round_counter == 13:  # Hus
            for i in range(-1, len(avHver_liste[current_player-1]) * -1, -2):
                if 2 <= avHver_liste[current_player-1][i] <= 3:
                    #print(avHver_liste[current_player-1][i - 1], avHver_liste[current_player-1][i], i)
                    for u in range(i - 2, len(avHver_liste[current_player-1]) * -1, -2):
                        if avHver_liste[current_player-1][i] == 2 and avHver_liste[current_player-1][u] == 3:
                            #print(avHver_liste[current_player-1][u - 1], avHver_liste[current_player-1][u], u, "a1")
                            scoreboard_liste_liste[current_player - 1][round_counter+1] += avHver_liste[current_player-1][u-1]*3
                            scoreboard_liste_liste[current_player - 1][round_counter + 1] += avHver_liste[current_player-1][i - 1] * 2
                            break
                        elif avHver_liste[current_player-1][i] == 3 and avHver_liste[current_player-1][u] == 2:
                            #print(avHver_liste[current_player-1][u - 1], avHver_liste[current_player-1][u], u, "a2")
                            scoreboard_liste_liste[current_player - 1][round_counter+1] += avHver_liste[current_player-1][u-1]*2
                            scoreboard_liste_liste[current_player - 1][round_counter + 1] += avHver_liste[current_player-1][i - 1] * 3
                            break
                    break
        elif round_counter == 14:  # Sjanse
            for i in range(0, len(hand1_liste[current_player-1])):
                scoreboard_liste_liste[current_player - 1][round_counter+1] += hand1_liste[current_player-1][i]
        elif round_counter == 15:  # Yatzee
            for i in range(1, len(avHver_liste[current_player-1]), 2):
                if avHver_liste[current_player-1][i] == 5:
                    scoreboard_liste_liste[current_player - 1][round_counter+1] = 50
        scoreboard_liste_liste[current_player - 1][17] = 0
        for i in range(6, len(scoreboard_liste_liste[current_player - 1])-2):  # Totalsum
            scoreboard_liste_liste[current_player - 1][17] += scoreboard_liste_liste[current_player - 1][i]
        #print(scoreboard_liste_liste)
        if round_counter <= 6:
            print("Dritbra, ", scoreboard_liste_liste[current_player - 1][round_counter-1], "poeng!!")
        else:
            print("Dritbra, ", scoreboard_liste_liste[current_player - 1][round_counter+1], "poeng!!")
        if current_player == antallSpillere:
            round_counter += 1

def decicions():
    global kastHedda_liste
    global hand1_liste
    global hand_liste
    global avHver_liste
    global newHand
    global current_player
    if kastHedda_liste[current_player-1] < 3:
        print("--------")
        if kastHedda_liste[current_player-1] == 1:
            spm3 = input("WOW, flott kast!\nVil du ta vare på noe eller kaste pånytt?\n(ra=reroll all / k=keep / a=avslutt runde) :")
        else:
            spm3 = input("WOW, flott kast!\nVil du ta vare på noe eller kaste pånytt?\n(ra=reroll all / rr = reroll rest / k=keep / a=avslutt runde) :")
        if spm3 == "k":
            keepFunction()
        elif spm3 == "ra":
            if kastHedda_liste[current_player-1] < 3:
                hand1_liste[current_player-1] = []
                newHand = []
                hand_liste[current_player-1] = []
                avHver_liste[current_player-1] = [1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0]
                kastTerning(5)
            else:
                print("Du har jo ikke flere kast, så du må nok ta vare på det du har")
        elif spm3 == "rr":
            print(newHand)
            print("Kast igjen!")
            hand_liste[current_player-1] = []
            hand1_liste[current_player-1] = []
            avHver_liste[current_player-1] = [1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0]
            kastTerning(5 - len(newHand))
        elif spm3 == "a":
            if kastHedda_liste[current_player-1] == 1:
                hand1_liste[current_player-1] = hand_liste[current_player-1]
            kastHedda_liste[current_player-1] = 3
            decicions()
    else:
        runde1(1)
        if round_counter > 15:
            time.sleep(2)
            scoreboard()
            winner_list = []
            for i in range(0, antallSpillere):
                winner_list.append(scoreboard_liste_liste[i][17])
            winner_list.sort(reverse=True)
            for u in range(0, len(winner_list)):
                for o in range(0, antallSpillere):
                    if winner_list[u] == scoreboard_liste_liste[o][17]:
                        if u == 0:
                            print("\n SPILL FERDIG \n \nALLE VAR KJEMPE FLINKE! \n \nVinneren er:", scoreboard_liste_liste[o][-1].upper(), "!!!!\n")
                        print(u+1, ".Plass", scoreboard_liste_liste[o][-1], "med: ", winner_list[u], "Poeng !!!")
            #print("\n SPILL FERDIG \n ANTALL POENG:", scoreboard_liste_liste[current_player-1][17], "\n ")
        else:
            print("Fantastisk, klar for ny runde? Press TAB->")
            keyboard.wait("TAB")
            hand_liste[current_player-1] = []
            kastHedda_liste[current_player-1] = 0
            hand1_liste[current_player-1] = []
            avHver_liste[current_player-1] = [1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0]
            if current_player < antallSpillere:
                current_player += 1
            else:
                current_player = 1
            runde1(0)

def keepFunction():
    global hand_liste
    global hand1_liste
    global avHver_liste
    global newHand
    newHand = []
    while True:
        keep = int(input("\nHva vil du ta vare på? :"))
        if avHver_liste[current_player-1][keep*2 - 1] > 0:
            keepNum = int(input("Hvor mange av dem vil du ta vare på? :"))
            if 0 < keepNum <= avHver_liste[current_player-1][keep*2 - 1]:
                for i in range(1, keepNum+1):
                    newHand.append(keep)
                if round_counter < 7:
                    break
            else:
                print("DU HAR IKKE SÅ MANGE", keep, "!!!!")
        else:
            print("DU HAR JO IKKE NOEN", keep, "!!!!")
        spm = input("Vil du ta vare på noe mer/annet? y/n :")
        if spm == "y":
            print("oki")
        else:
            break
    if kastHedda_liste[current_player-1] < 3:
        print(newHand)
        print("Kast igjen!")
        hand_liste[current_player - 1] = []
        hand1_liste[current_player - 1] = []
        avHver_liste[current_player - 1] = [1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0]
        kastTerning(5-len(newHand))
        #decicions()



startspm = int(input("Fritt kast(1), start spill(2), avslutt(3) :"))

#player1name = input("1:")

if startspm == 1:
    kastTerning(5)
elif startspm == 2:
    runde1(0)
elif startspm == 3:
    pass

print("Håper vi sees igjen")
