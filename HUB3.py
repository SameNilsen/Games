from tkinter import *
from PIL import Image, ImageTk
import time

#im = Image.open("Sprite/Wolverine_ani/Ja/Wolverine30.jpg")
#im.show()

brozone = Tk()
brozone.geometry("1000x600")
brozone.configure(bg='midnight blue')
dwnd = PhotoImage(file='Sprite/Circle.png')
current_topbar_list = []
current_topbar = None


class Modes():
    def __init__(self, columns, rows):
        global current_topbar
        if current_topbar != 1:
            current_topbar_list[current_topbar].reset_frame()
            current_topbar = 1
            topbar.topbar_modes_button.configure(bg='#568')
            topbar.topbar_main_screen_button.configure(bg='#567')
            topbar.topbar_apps_button.configure(bg='#567')
            topbar.topbar_colors_button.configure(bg='#567')
            self.frame_modes = Frame(brozone, bg='midnight blue')
            self.frame_modes.pack(expand=True, fill='both')
            self.columns = columns
            self.rows = rows
            for columns in range(0, self.columns):
                self.frame_modes.grid_columnconfigure(columns, weight=1)
            for rows in range(0, self.rows):
                self.frame_modes.grid_rowconfigure(rows, weight=1)
            #label1 = Label(self.frame_modes, bg='#567').grid(row=2, column=0, sticky=W + E + N + S)
            self.show_grid()
            self.types()
            print(brozone.winfo_width())
            print(brozone.winfo_height())

    def show_grid(self):
        for x in range(0, self.columns):
            for y in range(0, self.columns):
                la = Label(self.frame_modes, bg='red', text=f'{x, y}')
                la.grid(row=y, column=x)
                #lab = Label(self.frame_modes, bg='blue', text=f'{x+1, y+1}')
                #lab.grid(row=y+1, column=x+1)

    def types(self):
        # dwnd.zoom(1000, 1000)
        self.a1 = Button(self.frame_modes, image=dwnd, command=self.new_window, borderwidth=0, bg='midnight blue', activebackground='midnight blue')
        self.a1.grid(row=2, column=2)
        #self.a1.pack(side=LEFT)

    def new_window(self):
        broland = Toplevel()
        print(99)

    def reset_frame(self):
        self.frame_modes.destroy()

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


class Main_Screen():
    def __init__(self, columns, rows):
        global current_topbar
        if current_topbar != 0:
            current_topbar = 0
            topbar.topbar_modes_button.configure(bg='#567')
            topbar.topbar_main_screen_button.configure(bg='#568')
            topbar.topbar_apps_button.configure(bg='#567')
            topbar.topbar_colors_button.configure(bg='#567')
            self.frame_main_screen = Frame(brozone, bg='midnight blue')
            self.frame_main_screen.pack(expand=True, fill='both')


    def show_grid(self):
        self.columns = 10
        self.rows = 10
        for columns in range(0, self.columns):
            self.frame_main_screen.grid_columnconfigure(columns, weight=1)
        for rows in range(0, self.rows):
            self.frame_main_screen.grid_rowconfigure(rows, weight=1)
        for x in range(0, self.columns):
            for y in range(0, self.columns):
                la = Label(self.frame_main_screen, bg='red', text=f'{x, y}')
                la.grid(row=y, column=x)
                # lab = Label(self.frame_modes, bg='blue', text=f'{x+1, y+1}')
                # lab.grid(row=y+1, column=x+1)

    def types(self):
        # dwnd.zoom(1000, 1000)
        self.a1 = Button(self.frame_main_screen, image=dwnd, command=self.new_window, borderwidth=0, bg='midnight blue', activebackground='midnight blue')
        self.a1.grid(row=2, column=2)
        # self.a1.pack(side=LEFT)

    def new_window(self):
        broland = Toplevel()
        print(99)

    def reset_frame(self):
        self.frame_main_screen.destroy()


class TopBar:
    def __init__(self):
        self.top_frame = Frame(brozone, bg='#567')
        self.top_frame.pack(side=TOP, anchor=W, fill='x')

        self.topbar_main_screen()
        self.topbar_modes()
        self.topbar_apps()
        self.topbar_colors()

        label = Label(self.top_frame, bg='#567', bd=3)
        label.pack(side=LEFT, anchor=N, expand=True, fill='x')

    def topbar_main_screen(self):
        self.topbar_main_screen_button = Button(self.top_frame, text="Mainscreen", command=Main_Screen, bg='#568', borderwidth=1, width=20, activebackground='#567')
        #self.a2.grid(row=0, column=3, sticky=W+E+N+S)
        self.topbar_main_screen_button.pack(side=LEFT, anchor=N)

    def topbar_modes(self):
        self.topbar_modes_button = Button(self.top_frame, text="Modes", command=Modes(10, 10), bg='#567', borderwidth=1, width=20, activebackground='#567')
        #self.a2.grid(row=0, column=0, sticky=W+E+N+S)
        self.topbar_modes_button.pack(side=LEFT, anchor=N)

    def topbar_apps(self):
        self.topbar_apps_button = Button(self.top_frame, text="Apps", command=Apps, bg='#567', borderwidth=1, width=20, activebackground='#567')
        #self.a2.grid(row=0, column=1, sticky=W+E+N+S)
        self.topbar_apps_button.pack(side=LEFT, anchor=N)

    def topbar_colors(self):
        self.topbar_colors_button = Button(self.top_frame, text="Colors", command=Colors, bg='#567', borderwidth=1, width=20, activebackground='#567')
        #self.a2.grid(row=0, column=2, sticky=W+E+N+S)
        self.topbar_colors_button.pack(side=LEFT, anchor=N)

    def new_window(self):
        broland = Toplevel()
        print(99)


main_screen = Main_Screen
current_topbar_list.append(main_screen)
modes = Modes
current_topbar_list.append(modes)
apps = Apps
current_topbar_list.append(apps)
colors = Colors
current_topbar_list.append(colors)
topbar = TopBar()
Main_Screen(10, 10)

#Button(brozone, text="Colors", command=new_window).pack()
#Button(brozone, text="Boller", command=Modes.setup()).pack()


#Button(brozone, text="ANIMASJON", command=animasjon).pack()
#a = Toplevel()

brozone.title("Brozone")
brozone.mainloop()
