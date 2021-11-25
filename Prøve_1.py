
#Oppgave 3

u = 0
for i in range(1, 1000):
    u += 1/i**2 
print(u)
#rekken divergerer

#Oppgave 4
liste1 = []
for i in range(0, 100):
    p = i/7
    if p == type(int):
        liste1.append(p)
print(len(liste1))


#Oppgave 5
m = int(input("Skriv inn masse:"))
v_0 = int(input("Skriv inn startfart:"))
v = int(input("Skriv inn sluttfart:"))
h_0 = int(input("Skriv inn starthøyde:")) 
h = int(input("Skriv inn slutthøyde:")) 

g = 9.81

def e_m_0(m, v_0, h_0):
    return m*g*h_0 + (1/2)*m*v_0**2

def e_m(m, v, h):
    return m*g*h + (1/2)*m*v**2

print("vi har så mye energi i starten:", e_m_0(m, v_0, h_0))
print("Og så mye energi til slutt:", e_m(m, v, h))

c = e_m_0(m, _0, h_0) - e_m(m, v, h)


if e_m_0(m, v_0, h_0) == e_m(m, v, h):
    print("Ingen energi er tapt")
else:
    print("Energien er ikke bevart, det ble:", c, "Joule som gikk tapt")

          