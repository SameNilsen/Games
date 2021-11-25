from tkinter import *

ws = Tk()
ws.title('PythonGuides')
ws.geometry('300x200')

dwnd = PhotoImage(file='Sprite/Circle.png')
Button(ws, image=dwnd, command=None, borderwidth=0).pack(pady=10)

ws.mainloop()