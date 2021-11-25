import random
import time
import keyboard
import os


hand = []
hand1 = []
kastHedda = 0
avHver = [1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0]
scoreboard_liste = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
round_counter = 1
round_name = ["enere", "toere", "treere", "firere", "femere", "seksere", "Sum", "Bonus",
              "1 par", "2 par", "3 like", "4 like", "Liten straight", "Stor straight", "Hus", "Sjanse", "Yatzee", "Totalsum"]

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def kastTerning(x):
    print("Press SPACE to throw!")
    global kastHedda
    while True:
        if keyboard.is_pressed("SPACE"):
            #rint(888, avHver)
            break
    kastHedda += 1
    for i in range(0, x):
        hand.append(random.randint(1, 6))
    print("\nKast:", hand)
    if kastHedda >= 2:
        for i in range(0, len(newHand)):
            hand1.append(newHand[i])
        for u in range(0, len(hand)):
            hand1.append(hand[u])
        print("Nåværende hånd:", hand1)
        antallHver(hand1)
    else:
        antallHver(hand)
    print("Antall kast: ", kastHedda)
    decicions()


def antallHver(rar):
    global avHver
    avHver = [1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0]
    for u in range(0, len(rar)):
        for o in range(1, 7):
            if rar[u] == o:
                avHver[rar[u]*2 - 1] += 1
    #print("", avHver, "\n")

def scoreboard():
    sum = 0
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


def runde1(x):
    global round_counter
    global scoreboard_liste
    if x == 0:
        scoreboard()
        print("\n--- Runde ", round_counter, "! ---")
        if round_counter <= 6:
            print("Du skal ha", round_name[round_counter-1], ":) ")
        else:
            print("Du skal ha", round_name[round_counter + 1], ":) ")
        kastTerning(5)
    elif x == 1:
        if round_counter <= 6:  # 1-6
            print(avHver)
            for i in range(0, len(hand1)):
                if hand1[i] == round_counter:
                    scoreboard_liste[round_counter-1] += round_counter
                    scoreboard_liste[6] += round_counter
        elif round_counter == 7:  # 1 par
            for i in range(-1, len(avHver)*-1, -2):
                if avHver[i] >= 2:
                    scoreboard_liste[round_counter+1] = avHver[i-1]*2
                    break
        elif round_counter == 8:  # 2 par
            for i in range(-1, len(avHver) * -1, -2):
                if avHver[i] >= 2:
                    print(avHver[i - 1], avHver[i], i)
                    for u in range(i - 2, len(avHver) * -1, -2):
                        if avHver[u] >= 2:
                            print(avHver[u - 1], avHver[u], u)
                            scoreboard_liste[round_counter+1] += avHver[u-1]*2
                            scoreboard_liste[round_counter + 1] += avHver[i - 1] * 2
                            break
                    break
        elif round_counter == 9:  # 3 like
            for i in range(-1, len(avHver)*-1, -2):
                if avHver[i] >= 3:
                    scoreboard_liste[round_counter+1] = avHver[i-1]*3
                    break
        elif round_counter == 10: # 4 like
            for i in range(-1, len(avHver)*-1, -2):
                if avHver[i] >= 4:
                    scoreboard_liste[round_counter+1] = avHver[i-1]*4
                    break
        elif round_counter == 11:  # Liten straight
            ha = 0
            for i in range(1, 6):
                for u in range(0, len(hand1)):
                    if hand1[u] == i:
                        ha += 1
                        break
            print(ha)
            if ha >= 5:
                print("ya")
                scoreboard_liste[round_counter+1] = 15
        elif round_counter == 12:  # Stor straight
            hb = 0
            for i in range(2, 7):
                for u in range(0, len(hand1)):
                    if hand1[u] == i:
                        hb += 1
                        break
            print(hb)
            if hb >= 5:
                print("ya")
                scoreboard_liste[round_counter + 1] = 20
        elif round_counter == 13:  # Hus
            for i in range(-1, len(avHver) * -1, -2):
                if 2 <= avHver[i] <= 3:
                    print(avHver[i - 1], avHver[i], i)
                    for u in range(i - 2, len(avHver) * -1, -2):
                        if avHver[i] == 2 and avHver[u] == 3:
                            print(avHver[u - 1], avHver[u], u, "a1")
                            scoreboard_liste[round_counter+1] += avHver[u-1]*3
                            scoreboard_liste[round_counter + 1] += avHver[i - 1] * 2
                            break
                        elif avHver[i] == 3 and avHver[u] == 2:
                            print(avHver[u - 1], avHver[u], u, "a2")
                            scoreboard_liste[round_counter+1] += avHver[u-1]*2
                            scoreboard_liste[round_counter + 1] += avHver[i - 1] * 3
                            break
                    break
        elif round_counter == 14:  # Sjanse
            for i in range(0, len(hand1)):
                scoreboard_liste[round_counter+1] += hand1[i]
        elif round_counter == 15:  # Yatzee
            for i in range(1, len(avHver), 2):
                if avHver[i] == 5:
                    scoreboard_liste[round_counter+1] = 50
        scoreboard_liste[17] = 0
        for i in range(6, len(scoreboard_liste)-1):
            scoreboard_liste[17] += scoreboard_liste[i]

        if round_counter <= 6:
            print("Dritbra, ", scoreboard_liste[round_counter-1], "poeng!!")
        else:
            print("Dritbra, ", scoreboard_liste[round_counter+1], "poeng!!")
        round_counter += 1


def runde2():
    print("--- Runde 2! ---")
    print("Du skal ha toere")
    u = input("VENT:")

def decicions():
    global kastHedda
    global hand1
    global hand
    global avHver
    global newHand
    if kastHedda < 3:
        print("--------")
        if kastHedda == 1:
            spm3 = input("WOW, flott kast!\nVil du ta vare på noe eller kaste pånytt?\n(ra=reroll all / k=keep / a=avslutt runde) :")
        else:
            spm3 = input("WOW, flott kast!\nVil du ta vare på noe eller kaste pånytt?\n(ra=reroll all / rr = reroll rest / k=keep / a=avslutt runde) :")
        if spm3 == "k":
            keepFunction()
        elif spm3 == "ra":
            if kastHedda < 3:
                hand1 = []
                newHand = []
                hand = []
                avHver = [1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0]
                kastTerning(5)
            else:
                print("Du har jo ikke flere kast, så du må nok ta vare på det du har")
        elif spm3 == "rr":
            print(newHand)
            print("Kast igjen!")
            hand = []
            hand1 = []
            avHver = [1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0]
            kastTerning(5 - len(newHand))
        elif spm3 == "a":
            if kastHedda == 1:
                hand1 = hand
            kastHedda = 3
            decicions()
    else:
        runde1(1)
        if round_counter > 15:
            time.sleep(2)
            scoreboard()
            print("\n SPILL FERDIG \n ANTALL POENG:", scoreboard_liste[17], "\n ")
        else:
            print("Fantastisk, klar for ny runde? Press TAB->")
            keyboard.wait("TAB")
            hand = []
            kastHedda = 0
            hand1 = []
            avHver = [1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0]
            #lear()
            runde1(0)

def keepFunction():
    global hand
    global hand1
    global avHver
    global newHand
    newHand = []
    while True:
        keep = int(input("\nHva vil du ta vare på? :"))
        if avHver[keep*2 - 1] > 0:
            keepNum = int(input("Hvor mange av dem vil du ta vare på? :"))
            if 0 < keepNum <= avHver[keep*2 - 1]:
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
    if kastHedda < 3:
        print(newHand)
        print("Kast igjen!")
        hand = []
        hand1 = []
        avHver = [1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0]
        kastTerning(5-len(newHand))
        #decicions()



startspm = int(input("Fritt kast(1), start spill(2), avslutt(3) :"))
if startspm == 1:
    kastTerning(5)
elif startspm == 2:
    runde1(0)
elif startspm == 3:
    pass

print("Håper vi sees igjen")
