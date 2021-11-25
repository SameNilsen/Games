import arcade
import math
import random

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

        self.bilde = None
        self.bilde = arcade.SpriteList()
        self.timer = 0.0
        self.element = 0
        self.dot_liste = []
        self.start = False

        for i in range(0, 1000, 10):
            for o in range(0, 600, 10):
                #dot = arcade.Sprite("Sprite/ShrekIMG5.png", center_x=i, center_y=o, scale=0.01)
                #self.dot_liste.append(dot)
                #print(i,o)
                pass



        self.total_time = 0.0


    def on_resize(self, width, height):

        # Call the parent. Failing to do this will mess up the coordinates, and default to 0,0 at the center and the
        # edges being -1 to 1.
        super().on_resize(width, height)

        self.width = width
        self.height = height

        print(self.width, self.height)

    def on_draw(self):
        arcade.start_render()

        self.sprite_list.draw()

        #arcade.draw_text(f"{self.target_x}, {self.target_y}", 50, self.height - 100, arcade.color.DARK_RED, 20)

        self.shape_list.draw()

        if self.start:
            As = 350
            Ass = 450
            Bs = 550
            Bss = 650
            Cs = 290
            Css = 710
            for i in range(500, 440, -10):
                if Ass != 510:
                    for a in range(As, Ass, 10):
                        dot = arcade.Sprite("Sprite/ShrekIMG5.png", center_x=a, center_y=i, scale=0.01)
                        self.dot_liste.append(dot)
                    As -= 10
                    Ass += 10
                    for b in range(Bs, Bss, 10):
                        dot = arcade.Sprite("Sprite/ShrekIMG5.png", center_x=b, center_y=i, scale=0.01)
                        self.dot_liste.append(dot)
                    Bs -= 10
                    Bss += 10
            for i in range(440, 200, -10):
                for c in range(Cs, Css, 10):
                    dot = arcade.Sprite("Sprite/ShrekIMG5.png", center_x=c, center_y=i, scale=0.01)
                    self.dot_liste.append(dot)
                Cs += 10
                Css -= 10


            self.start = False

        self.bilde.draw()

    def on_update(self, delta_time):

        if self.right:
            self.player2_x += self.player2_speed * delta_time
        if self.left:
            self.player2_x -= self.player2_speed * delta_time
        if self.up:
            self.player2_y += self.player2_speed * delta_time
        if self.down:
            self.player2_y -= self.player2_speed * delta_time

        self.sprite2.set_position(self.player2_x, self.player2_y)

        self.timer += 1
        if self.timer == 2:
            self.timer = 0

        if self.timer == 1:
            if len(self.dot_liste) > self.element:
                self.bilde.append(self.dot_liste[self.element])
                self.element += 1

    def on_mouse_motion(self, x, y, dx, dy):
        self.target_x = x
        self.target_y = y
        # print(x, y)

        self.x = x
        self.y = y


    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):

        self.x = x
        self.y = y

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.RIGHT:
            self.right = True
        if symbol == arcade.key.LEFT:
            self.left = True
        if symbol == arcade.key.UP:
            self.up = True
        if symbol == arcade.key.DOWN:
            self.down = True

        if symbol == arcade.key.ENTER:
            self.start = True

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
