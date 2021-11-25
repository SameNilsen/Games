import time
print("------tall string sortering-------")
print("             f.eks:             ")
print("        Tall:987654321           ")
print("        ---> 123456789           ")
string = str(input("Tall:"))
list = []
for i in range(0, len(string)):
    list.append(int(string[i]))
print(list)
sortert = 0
while sortert < len(list):
    for i in range(0, len(list)-1):
        if list[i+1] < list[i]:
            time.sleep(0.3)
            a = list[i]
            list[i] = list[i+1]
            list[i+1] = a
            print(list)
    sortert += 1
