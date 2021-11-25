liste=[]                #Lager en tom liste hvor phi(n)-verdiene vil havne
liste.append(1)              #Legger til phi(1), fordi en vil regnes som en primtall i programmet, og dermed gi oss en verdi 0, som er feil

n = int(input("Til hvilket tall ønsker du å sjekke, fra 1\n"))
for i in range(2,n+1):
    m=0
    for g in range(2,i):          #Sjekker alle tall mellom 2 og tallet i
        if i%g == 0:              #Hvis i er delelig med noe tall settes en variabel til m, og det er da ikke et primtall
                m=1
    if not m==1:                #Hvis m=1 aldri blir aktivert, da er 'i' et primtall, og vi bruker Hypotese 1, og legger til 'i'-1
        liste.append(i-1)       
    elif m==1:
        for dele in range(2,i):    #Lager en variabel 'dele' som er alle tallene mellom 2 og 'i'
            dele2 = i/dele          #Lager så en variabel 'dele2', slik at 'dele'*'dele2' = i
            if dele2%1 == 0:       #Ettersom 'dele2' alltid blir et flyttall, legger vi til en linje som gjør at hvis 'dele2' er et heltall, vil det bli skrevet som et int-tall
                dele2=int(dele2) 
                if i%dele == 0:
                    if not dele2%dele == 0:    #Hvis dele2 og dele er delelige med hverandre, vil vi måtte bruke den 3. hypotesen
                        liste.append(liste[dele-1]*liste[dele2-1])
                        break        #Slutter løkken, da vi ellers vil treffe flere tall, da 6 = 2*3 og 3*2
                    else:
                        liste.append(dele*liste[dele2-1])    #Hvis dele og dele2 er delelige med hverandre, bruker vi hypotese 4. 
                        break

def a():
    print("\n")
    for l in range(1,len(liste)+1):      
        print(l, liste[l-1])      

def b():
    b = int(input("Hva ønsker du at n skal være\n"))
    print("\n")
    print(b,liste[b-1])
    
def c():
    fra = int(input("Hvilket tall ønsker du å se fra?\n"))
    til = int(input("Til og med hviket tall?\n"))
    print("\n")
    for p in range(fra,til+1):
        print(p,liste[p-1])                        
                        
valg = int(input("Hva ønsker du å se, av tallene du har sjekket?\n1.En liste med alle verdiene\n2.En enkel verdi\n3.Fra en verdi til en annen\n"))
if valg == 1:
    a()
elif valg == 2:
    b()
elif valg == 3:
    c()

