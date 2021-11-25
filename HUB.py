from tkinter import *
from PIL import Image, ImageTk
import time

#im = Image.open("Sprite/Wolverine_ani/Ja/Wolverine30.jpg")
#im.show()

brozone = Tk()
brozone.geometry("1000x600")
brozone.configure(bg='midnight blue')
dwnd = PhotoImage(file='Sprite/Circle.png')
for column in range(0, 5):
    brozone.grid_columnconfigure(column, weight=1)


class Modes():
    def __init__(self):
        self.frame_modes = Frame(brozone)
        self.frame_modes.grid(columnspan=5, sticky=W)
        self.frame_modes.grid_rowconfigure(1, weight=1)
        #label1 = Label(brozone, bg='#567').grid(row=2, column=4, sticky=W + E + N + S)
        self.show_grid()
        #self.types()
        print(brozone.winfo_width())
        print(brozone.winfo_height())

    def show_grid(self):
        for i in range(0, 4, 2):
            la = Label(self.frame_modes, bg='red', text=f'{i}')
            la.grid(row=0, column=i)
            lab = Label(self.frame_modes, bg='blue', text=f'{i+1}')
            lab.grid(row=1, column=i+1)
        color1 = 'red'
        color2 = 'blue'
        """
        for i in range(0, 10):
            for o in range(0, 10):
                if i%2 == 0:
                    la = Label(self.frame_modes, bg=f'{color1}', height=2, bd=10)
                else:
                    la = Label(self.frame_modes, bg=f'{color2}', height=2, bd=10)
                la.grid(row=i, column=o, sticky=W + E + N + S)
        """


    def types(self):
        # dwnd.zoom(1000, 1000)
        self.a1 = Button(self.frame_modes, image=dwnd, command=self.new_window, borderwidth=0, bg='midnight blue', activebackground='midnight blue')
        self.a1.grid(row=1, column=5, sticky=E)
        #self.a1.pack()

    def new_window(self):
        broland = Toplevel()
        print(99)

class Apps():
    def __init__(self):
        self.types()

    def types(self):
        # dwnd.zoom(1000, 1000)
        self.a1 = Button(brozone, image=dwnd, command=self.new_window, borderwidth=0, bg='midnight blue', activebackground='midnight blue')
        self.a1.grid(row=0, column=0, sticky=W + E + N + S)
        #self.a1.pack(pady=20)

    def new_window(self):
        broland = Toplevel()
        print(99)

class Colors():
    def __init__(self):
        self.types()

    def types(self):
        # dwnd.zoom(1000, 1000)
        self.a1 = Button(brozone, image=dwnd, command=self.new_window, borderwidth=0, bg='midnight blue', activebackground='midnight blue')
        self.a1.grid(row=5, column=2, sticky=W + E + N + S)
        #self.a1.pack(pady=20)

    def new_window(self):
        broland = Toplevel()
        print(99)

class Main_screen():
    def __init__(self):
        self.types()

    def types(self):
        # dwnd.zoom(1000, 1000)
        self.a1 = Button(brozone, image=dwnd, command=self.new_window, borderwidth=0, bg='midnight blue', activebackground='midnight blue')
        self.a1.grid(row=5, column=2, sticky=W + E + N + S)
        #self.a1.pack(pady=20)

    def new_window(self):
        broland = Toplevel()
        print(99)

class Hub:
    def __init__(self):
        self.topbar_modes()
        self.topbar_apps()
        self.topbar_colors()
        self.topbar_main_screen()

        label = Label(brozone, bg='#567').grid(row=0, column=4, sticky=W+E+N+S)

    def topbar_modes(self):
        self.a2 = Button(brozone, text="Modes", command=Modes, bg='#567', borderwidth=1, width=20, activebackground='#567')
        self.a2.grid(row=0, column=0, sticky=W+E+N+S)
        #self.a2.pack()

    def topbar_apps(self):
        self.a2 = Button(brozone, text="apps", command=Apps, bg='#567', borderwidth=1, width=20, activebackground='#567')
        self.a2.grid(row=0, column=1, sticky=W+E+N+S)
        #self.a2.pack()

    def topbar_colors(self):
        self.a2 = Button(brozone, text="colors", command=Colors, bg='#567', borderwidth=1, width=20, activebackground='#567')
        self.a2.grid(row=0, column=2, sticky=W+E+N+S)
        #self.a2.pack()

    def topbar_main_screen(self):
        self.a2 = Button(brozone, text="mainscreen", command=Main_screen, bg='#567', borderwidth=1, width=20, activebackground='#567')
        self.a2.grid(row=0, column=3, sticky=W+E+N+S)
        #self.a2.pack()

    def new_window(self):
        broland = Toplevel()
        print(99)



hub = Hub()

#Button(brozone, text="Colors", command=new_window).pack()
#Button(brozone, text="Boller", command=Modes.setup()).pack()


#Button(brozone, text="ANIMASJON", command=animasjon).pack()
#a = Toplevel()

brozone.title("Brozone")
brozone.mainloop()
