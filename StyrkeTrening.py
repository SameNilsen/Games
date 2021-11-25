from tkinter import *
import time
import arcade
import math
import random
"""

trening = Tk()

canvas = Canvas(trening, width=800, height=500)
canvas.configure(bg="black")
canvas.pack(fill="both", expand=True)


def timer():
    global current_time
    current_time = time.process_time()
    timerLabel = Label(trening, text=f"Gjennværende tid:{current_time}").pack()
    trening.after(1000, timer)


def okt1():
    o1.destroy()
    o2.destroy()
    timer()


def okt2():
    pass


o1 = Button(trening, text="Økt 1", command=okt1)
o2 = Button(trening, text="Økt 2", command=okt2)

a = canvas.create_window(300, 200, window=o1)
canvas.create_window(500, 200, window=o2)

trening.title("Træning")
trening.mainloop()
"""

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

class MyGameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title, resizable=True)

        self.sprite_list = None
        self.sprite_list = arcade.SpriteList()

        self.shape_list = None
        self.shape_list = arcade.ShapeElementList()

        #self.sprite = arcade.Sprite("Sprite/ShrekIMG5.png", center_x=100, center_y=100, scale=0.1)
        #self.x = 0
        #self.y = 0
        #self.sprite.set_position(self.x, self.y)

        #self.sprite_list.append(self.sprite)

        self.sprite2 = arcade.Sprite("Sprite/Høne.png", center_x=100, center_y=100, scale=0.1)
        self.player2_x = 200
        self.player2_y = 100
        self.player2_speed = 100
        self.sprite2.set_position(self.player2_x, self.player2_y)

        self.sprite_list.append(self.sprite2)

        self.up = False
        self.down = False
        self.right = False
        self.left = False


        self.total_time = 0.0
        self.seconds = 0.0
        self.timer = 6.0

        self.start_screen = True
        self.okt1 = False
        self.start1 = False
        self.start2 = False
        self.start0 = False
        self.okt2 = False

        self.current_ovelse = 0
        self.av_tre = 1
        self.okt = 0
        self.pause = False
        self.done = False
        self.runde = 1

        self.okt1_ovelser = [["Brystpress", 3, "8rep", "7v"], ["Pullupsgreie", 3, "8rep", "6v"], ["Push ups", 3, "6rep", "Egenvekt"],
                             ["tricepspress", 3, "8rep", "3v"], ["brystklem", 3, "6rep", "2v"], ["Svømmer", 2, "1min", "Egenvekt"],
                             ["Dips", 1, "50sek", "Egenvekt"], ["Roer", 3, "10rep", "8v"]]
        self.okt2_ovelser = [["Øvelse1", 3, "8rep", "7v"], ["Dips", 1, "50sek", "Egenvekt"], ["Svømmer", 2, "1min", "Egenvekt"], ["Øvelse4", 3, "6rep", "2v"]]  # Navn, sett, reps, vekt

        self.okter = []
        self.okter.append(self.okt1_ovelser)
        self.okter.append(self.okt2_ovelser)

        self.animasjon = False
        self.list = []

        #for i in range(1, 31):
        #    shape = arcade.draw_xywh_rectangle_filled(self.width/2 - 150, 100, i*10, 10, arcade.color.GREEN)
        #    self.list.append(shape)


    def on_resize(self, width, height):

        # Call the parent. Failing to do this will mess up the coordinates, and default to 0,0 at the center and the
        # edges being -1 to 1.
        super().on_resize(width, height)

        self.width = width
        self.height = height

        print(self.width, self.height)

    def on_draw(self):
        arcade.start_render()

        #self.background = arcade.load_texture("Sprite/GYM.jpg")
        # self.background.draw(0, 0, self.width, self.height)
        #arcade.draw_texture_rectangle(self.width // 2, self.height // 2, self.width, self.height, self.background)

        #self.sprite_list.draw()

        #arcade.draw_text(f"{self.target_x}, {self.target_y}", 50, self.height - 100, arcade.color.DARK_RED, 20)
        #arcade.draw_text(f"Total_time:{self.total_time}", 100, self.height - 100, arcade.color.GREEN, 15)
        #arcade.draw_text(f"Seconds:{self.seconds}", 100, self.height - 200, arcade.color.GREEN, 15)


        if self.start_screen:
            arcade.draw_line(self.width/2, self.height, self.width/2, 0, arcade.color.ELECTRIC_CYAN, 5)
            arcade.draw_text("Økt 1", self.width/4, self.height/2, arcade.color.ELECTRIC_CYAN, 40)
            arcade.draw_text("Økt 2", self.width*2.7/4, self.height/2, arcade.color.ELECTRIC_CYAN, 40)

        if self.start0:
            arcade.draw_text("Ready when you are!", self.width/4, self.height/2, arcade.color.ELECTRIC_CYAN, 40)
            arcade.draw_text(f"Første øvelse er: {self.okter[self.okt-1][0][0]}", self.width/4, self.height/2 + 100, arcade.color.ELECTRIC_CYAN, 40)
            arcade.draw_text("Trykk SPACE for å starte", self.width/4, self.height/2-100, arcade.color.ELECTRIC_CYAN, 40)

        if self.start_screen == False:
            if self.start0 == False:
                arcade.draw_text(f"Runde: {self.runde}", 50, self.height-100, arcade.color.ELECTRIC_CYAN, 40)

        if self.start1:
            self.timer -= self.delta_time
            if self.timer//1 > 0:
                arcade.draw_text(f"Starter om:{self.timer//1}", self.width/2, self.height/2 - 200, arcade.color.GREEN, 15)
            elif self.timer//1 > -2:
                arcade.draw_text(f"START!!!", self.width/2, self.height/2 - 200, arcade.color.GREEN, 15)
            else:
                self.timer = 0.0
                self.start2 = True
                self.start1 = False

        if self.start2:
            self.timer += self.delta_time
            arcade.draw_text(f"{self.okter[self.okt-1][self.current_ovelse][2]}", self.width / 2 - 50, self.height-150, arcade.color.ELECTRIC_CYAN, 40)
            arcade.draw_text(f"{self.okter[self.okt-1][self.current_ovelse][3]}", self.width / 2 - 50, self.height-200, arcade.color.ELECTRIC_CYAN, 40)
            arcade.draw_text(f"Sett:{self.av_tre}", self.width / 2 - 50, self.height-250, arcade.color.ELECTRIC_CYAN, 40)
            arcade.draw_text(f"{self.okter[self.okt-1][self.current_ovelse][0]}", self.width / 2 - 50, 200, arcade.color.ELECTRIC_CYAN, 40)
            arcade.draw_text(f"Timer:{self.timer//1}", self.width / 2 - 50, 100, arcade.color.ELECTRIC_CYAN, 40)

        if self.pause:
            self.timer -= self.delta_time
            #self.list[int(self.timer//1)-1].draw()
            arcade.draw_xywh_rectangle_filled(self.width / 2 - 150, 120, int(self.timer//1)*10, 30, arcade.color.ELECTRIC_CYAN)
            arcade.draw_xywh_rectangle_outline(self.width/2-150, 120, 300, 30, arcade.color.ELECTRIC_CYAN)
            arcade.draw_text(f"Pause{self.timer//1}", self.width / 2 - 100, 220, arcade.color.ELECTRIC_CYAN, 40)
            if self.av_tre >= self.okter[self.okt-1][self.current_ovelse][1]:
                arcade.draw_text(f"{self.okter[self.okt-1][self.current_ovelse+1][2]}", self.width / 2 - 50, self.height - 150, arcade.color.ELECTRIC_CYAN, 40)
                arcade.draw_text(f"{self.okter[self.okt-1][self.current_ovelse+1][3]}", self.width / 2 - 50, self.height - 200, arcade.color.ELECTRIC_CYAN, 40)
                arcade.draw_text(f"Sett:{self.av_tre}", self.width / 2 - 50, self.height - 250, arcade.color.ELECTRIC_CYAN, 40)
                arcade.draw_text(f"Neste øvelse:{self.okter[self.okt-1][self.current_ovelse+1][0]}", self.width / 2 - 150, 20, arcade.color.ELECTRIC_CYAN, 40)
            else:
                arcade.draw_text(f"{self.okter[self.okt-1][self.current_ovelse][2]}", self.width / 2 - 50, self.height - 150, arcade.color.ELECTRIC_CYAN, 40)
                arcade.draw_text(f"{self.okter[self.okt-1][self.current_ovelse][3]}", self.width / 2 - 50, self.height - 200, arcade.color.ELECTRIC_CYAN, 40)
                arcade.draw_text(f"Sett:{self.av_tre}", self.width / 2 - 50, self.height - 250, arcade.color.ELECTRIC_CYAN, 40)
                arcade.draw_text(f"Neste øvelse:{self.okter[self.okt-1][self.current_ovelse][0]}", self.width / 2 - 150, 20, arcade.color.ELECTRIC_CYAN, 40)
            if self.timer//1 == 0:
                self.start2 = True
                self.timer = 0.0
                self.pause = False

                if self.av_tre >= self.okter[self.okt-1][self.current_ovelse][1]:
                    self.current_ovelse += 1
                    self.av_tre = 1
                else:
                    self.av_tre += 1


        if self.done:
            self.timer -= self.delta_time
            if self.timer//1 > 0:
                arcade.draw_text(f"Workout complete, nice job", self.width / 2 - 150, 120, arcade.color.ELECTRIC_CYAN, 40)
            else:
                self.start_screen = True
                self.timer = 6.0
                self.current_ovelse = 0
                self.done = False

    def on_update(self, delta_time):

        #self.total_time += delta_time
        #self.seconds = self.seconds
        self.delta_time = delta_time
        if self.right:
            self.player2_x += self.player2_speed * delta_time
        if self.left:
            self.player2_x -= self.player2_speed * delta_time
        if self.up:
            self.player2_y += self.player2_speed * delta_time
        if self.down:
            self.player2_y -= self.player2_speed * delta_time

        self.sprite2.set_position(self.player2_x, self.player2_y)


    def on_mouse_motion(self, x, y, dx, dy):
        self.target_x = x
        self.target_y = y
        # print(x, y)

        self.x = x
        self.y = y


    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):

        self.x = x
        self.y = y

        if self.x < self.width/2:
            self.start_screen = False
            self.okt = 1
            self.start0 = True
        elif self.x > self.width/2:
            self.start_screen = False
            self.okt = 2
            self.start0 = True

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.RIGHT:
            self.right = True
        if symbol == arcade.key.LEFT:
            self.left = True
        if symbol == arcade.key.UP:
            self.up = True
        if symbol == arcade.key.DOWN:
            self.down = True

        if self.start0 == True:
            if symbol == arcade.key.SPACE:
                self.start0 = False
                self.start1 = True

        if self.start2:
            if symbol == arcade.key.SPACE:
                #print("current øvelse", self.current_ovelse, "lengde", len(self.okter[self.okt-1]))
                if self.av_tre >= self.okter[self.okt - 1][self.current_ovelse][1]:
                    if self.current_ovelse+1 < len(self.okter[self.okt-1]):
                        self.start2 = False
                        self.pause = True
                        print(self.av_tre)
                        self.timer = 61.0
                    else:
                        if self.runde == 1:
                            self.runde += 1
                            self.current_ovelse = 0
                            self.av_tre = 0
                            self.start2 = False
                            self.pause = True
                            self.timer = 121.0
                        else:
                            self.start2 = False
                            self.pause = False
                            self.done = True
                            self.timer = 5.0
                else:
                    self.start2 = False
                    self.pause = True
                    self.timer = 31.0


    def on_key_release(self, symbol, modifiers):
            if symbol == arcade.key.RIGHT:
                self.right = False
            if symbol == arcade.key.LEFT:
                self.left = False
            if symbol == arcade.key.UP:
                self.up = False
            if symbol == arcade.key.DOWN:
                self.down = False

MyGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT, 'My Game window')
arcade.run()
