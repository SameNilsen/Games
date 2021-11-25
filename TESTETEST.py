import math
import random
import webbrowser
import os
"""
b = math.radians(60)
a = math.cos(b)
print(a)

t = 1730.7831380000005/(140*math.cos(b))
print(t)

# t = 24.7

y = (140*math.sin(b)*t) - (1/2 * 9.81 * t**2)
print(y)

print(str(chr(32)))

print(int(chr(55)) + 2)

print(ord("2"))

print(int("2") *8)

print((1000*600)/0.05)

print(round(5.9))

a = [0, 1, 2, 3, 4, 5]

a[2:2] = [6]

a[0:0] = [11]
print(a)

for i in range(0, 100):
    #print(random.randint(1, 1))
    pass

print(random.choice(a))
a.remove(11)
print(a)

aa = 1
bb = 2
cc = 4
if aa == 1 and bb == 3 or cc == 4:
    print(aa, bb, cc)

gh = [1, 2]
print(gh)
gh.append(4)
print(gh)

for i in range(-16, 17, 8):
    print(i)

ae = []
ae.append([2, 2])
ae.append([3452, 256])
ae.append([7672, 56562])
print(ae)
print(ae[1][0])
if ae[0] == [2, 2]:
    print(ae[2])

aw = [[2, 3], [1, 4]]
aq = [1, 4]
if aw[1] == aq:
    print(aw, aq, "hh")
for i in range(0, 50):
    print(random.randrange(-1, 100, 2))

ere = [[1, 1], [2, 2], [1,1]]
for i in range(0, len(ere)):
    if [1,1] == ere[i]:
        print("ererere")



test = []
AI_x = 200
x = AI_x
while x <= AI_x+16:
    test.append(x)
    x += 0.1
x = AI_x + 16
while x >= AI_x:
    test.append(x)
    x -= 0.1
x = AI_x
while x >= AI_x-16:
    test.append(x)
    x -= 0.1
x = AI_x - 16
while x <= AI_x:
    test.append(x)
    x += 0.1

print(test)


horisontal_liste = []
for i in range(1, 10):
    horisontal_liste.append([(i*10)+1])
    for o in range(2, 10):
        horisontal_liste[i-1].append((10*i)+o)
print(horisontal_liste)
print(horisontal_liste[4][5])

a = 7
print("Hello world", 8)
print(888)

print(a)
if a == 7:
    a = 6
elif a == 6:
    a = 7

print(a)

liste = [2, 1]

liste.append(3)
print(liste)

for i in range(0, 5):
    print(i)

liste[2] = None
print(liste)
for i in range(len(liste)):
    if liste[i] != None:
        print(liste[i])

a = [3, 5,1, 9, 6,8 ,4, 2, 7]
if len(a) == 9:
    feil = 0
    for b in range(0, len(a)):
        if a[b] == None:
            feil = 10
    for i in range(0, len(a)):
        for o in range(0, len(a)):
            if i != o:
                if a[i] == a[o]:
                    feil += 1
    if feil >= 1:
        print("feil", a)
    else:
        print("ye", a)

print(math.degrees(math.atan(-10/10)))

print(math.sin(math.radians(60)))

aa = 19

if aa >= 21:
    print("du kan kjøpe hva du vil")
elif 18 <= aa < 21:
    print("du kan få noe")
else:
    print("STIKK")

def kode():
    print("-----")
    spm = input("Hei:")
    if spm == "ja":
        print("aight")
    else:
        print("hmm")

def start1():
    print("1----")
    while True:
        print("halla")
        break
    kode()
    spm2 = input("spm 2:")
    if spm2 == "ja":
        print("strålede")
    else:
        print("uffasa")
#start1()
print("------")

gg = [1, 2, 2, 0, 3, 0, 4, 0, 5, 0, 6, 2]
print("gg", gg[-2])
for i in range(-1, len(gg)*-1, -2):
    if 2 <= gg[i] <= 3:
        print(gg[i-1], gg[i], i)
        for u in range(i-2, len(gg)*-1, -2):
            if gg[i] - gg[u] == 1:
                print(gg[u-1], gg[u], u, "a1")
                break
            elif gg[i] - gg[u] == -1:
                print(gg[u - 1], gg[u], u, "a2")
                break
        break
print("-------")

ff = [5, 2, 1, 4, 3]
for a in range(0, len(ff)):
    if ff[a] == 1:
        for b in range(0, len(ff)):
            if ff[b] == 2:
                for c in range(0, len(ff)):
                    if ff[c] == 3:
                        for d in range(0, len(ff)):
                            if ff[d] == 4:
                                for e in range(0, len(ff)):
                                    if ff[e] == 5:
                                        print("ålø")

ha = 0
for i in range(1, 6):
    for u in range(0, len(ff)):
        if ff[u] == i:
            ha += 1
            break
print(ha)
if ha >= 5:
    print("ya")
print("------")
ui = [1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 5]
for i in range(1, len(ui), 2):
    print(i)
    if ui[i] == 5:
        print("yahaahahtzee")
print("----------")
scores = []
score1 = [2, 3, 4, 53, 5,34, 345, 345]
score2 = [1, 2, 3, 4, 5, 6]
scores.append(score1)
scores.append(score2)
print("|", 22, "|", end=" ")
for i in range(0, len(scores)):
    print(scores[i][0], "|", end=" ")
print("---------")
yy = [1,2,3,4,5,6, "heo"]
uu = [1,2,3,4,5,8, "iua"]
ii = []
ii.append(yy[5])
ii.append(uu[5])
ii.sort(reverse=True)
print(ii)
for u in range(0, len(ii)):
    if ii[u] == yy[5]:
        print()
"""
class enemy():
    "This is the enemy of Norway"
    health = 100
    liste = [0]
    def __init__(self, attack_power, defense_power):
        self.attack_power = attack_power
        self.defense_power = defense_power

        print(222)
    def attack(self):
        print("u suk potato")
        print(-1*self.attack_power)
        print(self.defense_power)
        print(self.liste)
    def stats(self):
        print(self.attack_power, self.defense_power, "ee")


print(enemy.__doc__)
print(enemy.health)
enemy.health += 1
print(enemy.health)

sweden = enemy(1, 2)
sweden.attack()

denmark = enemy(2, 3)
denmark.stats()
denmark.attack()

denmark.shout = "POTÆT"
sweden.shout = "BULLAR"

print(denmark.shout, sweden.shout)

enemy.liste.append(2)
print(enemy.liste)
denmark.attack()
print("-------------")
a = "hei"
print(a, f"hei{1}")

for i in range(30, -1, -1):
    print(i)
print("---------------")
a = [[1, 2, 3, 4, 5], [11, 22, [111, 222, 333], 44, 55]]
print(a[1][2][1])




