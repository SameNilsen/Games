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

        self.up = False
        self.down = True
        self.right = False
        self.left = False

        self.background = None

        self.MAI = arcade.create_rectangle_outline(self.width / 4.1, self.height / 1.75, self.width/10, self.height/10, arcade.color.RED, 1)
        self.shape_list.append(self.MAI)

        self.OKTOBER = arcade.create_rectangle_outline(self.width*3.05 / 4, self.height / 2.2, 100, 50, arcade.color.RED, 1)
        self.shape_list.append(self.OKTOBER)

        self.JANUAR = arcade.create_rectangle_outline(self.width * 3.05 / 4, self.height / 2.2, 100, 50, arcade.color.RED, 1)
        self.shape_list.append(self.JANUAR)

        self.FEBRUAR = arcade.create_rectangle_outline(self.width * 3.05 / 4, self.height / 2.2, 100, 50, arcade.color.RED, 1)
        self.shape_list.append(self.FEBRUAR)

        self.MARS = arcade.create_rectangle_outline(self.width / 2.8, self.height / 4.3, self.width / 10, self.height / 10, arcade.color.RED, 1)
        self.shape_list.append(self.MARS)

        self.APRIL = arcade.create_rectangle_outline(self.width / 3.8, self.height / 2.9, self.width / 10, self.height / 10, arcade.color.RED, 1)
        self.shape_list.append(self.APRIL)

        self.JUNI = arcade.create_rectangle_outline(self.width * 3.05 / 4, self.height / 2.2, 100, 50, arcade.color.RED, 1)
        self.shape_list.append(self.JUNI)


    def on_resize(self, width, height):

        # Call the parent. Failing to do this will mess up the coordinates, and default to 0,0 at the center and the
        # edges being -1 to 1.
        super().on_resize(width, height)

        self.width = width
        self.height = height

        print(self.width, self.height)

    def on_draw(self):
        arcade.start_render()

        self.background = arcade.load_texture("Sprite/KALENDER.png")
        self.background.draw(self.width/2, self.height/2, self.width, self.height)
        arcade.draw_text(f"{self.x}, {self.y}", self.width/2, self.height-30, arcade.color.RED, 20)

        self.sprite_list.draw()

        self.shape_list.draw()



    def on_update(self, delta_time):
        pass

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        print(x, y)

        self.x = x
        self.y = y

        if 194 < x < 294 and 295 < y < 378:
            print("MAI")

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.RIGHT:
            self.right = True
        if symbol == arcade.key.LEFT:
            self.left = True
        if symbol == arcade.key.UP:
            self.up = True
        if symbol == arcade.key.DOWN:
            pass
            #self.down = True

        if symbol == arcade.key.ESCAPE:
            arcade.close_window()

    def on_key_release(self, symbol, modifiers):
            if symbol == arcade.key.RIGHT:
                self.right = False
            if symbol == arcade.key.LEFT:
                self.left = False
            if symbol == arcade.key.UP:
                self.up = False
            if symbol == arcade.key.DOWN:
                pass
                #self.down = False


MyGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT, 'My Game window')
arcade.run()