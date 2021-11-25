from tkinter import *
from PIL import Image, ImageTk
import time

#im = Image.open("Sprite/Wolverine_ani/Ja/Wolverine30.jpg")
#im.show()

brozone = Tk()
#brozone.geometry("500x300")


def new_window():
    broland = Toplevel()


#Button(brozone, text="CLICK", command=new_window).pack()

canvas = Canvas(brozone, width=800, height=500)
canvas.configure(bg="black")
canvas.pack(fill="both", expand=True)
"""
bilde = Image.open(f'Sprite/Wolverine_ani/Ja/Wolverine{30}.jpg')
bilde = bilde.resize((800, 500), Image.ANTIALIAS)
img = ImageTk.PhotoImage(bilde)

print(img.width(), img.height())
"""

current_bilde = 31
liste = []
for i in range(-1, 31):
    bilde = Image.open(f'Sprite/Wolverine_ani/Ja/Wolverine{i}.jpg')
    bilde = bilde.resize((800, 500), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(bilde)
    liste.append(img)
canvas.create_image(-40, -30, anchor=NW, image=liste[31])


def animasjon():
    global canvas, current_bilde
    #liste[current_bilde].__del__()
    canvas.create_image(-40, -30, anchor=NW, image=liste[current_bilde - 1])
    current_bilde -= 1
    if current_bilde >= 1:
        brozone.after(30, animasjon)
    else:
        #current_bilde = 31
        animasjonReverse()


def animasjonReverse():
    global canvas, current_bilde
    print(current_bilde)
    time.sleep(2)
    #liste[current_bilde].__del__()
    canvas.create_image(-40, -30, anchor=NW, image=liste[current_bilde + 1])
    current_bilde += 1
    if current_bilde <= 30:
        brozone.after(30, animasjonReverse)
    else:
        current_bilde = 31


Button(brozone, text="START", command=animasjon).pack()

brozone.title("Brozone")
brozone.resizable(0, 0)
brozone.mainloop()
