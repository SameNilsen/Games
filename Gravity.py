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

        self.sprite = arcade.Sprite("Sprite/Stan.png", center_x=100, center_y=100, scale=0.5)
        self.player_x = self.width/2
        self.player_y = self.height
        self.sprite.set_position(self.player_x, self.player_y)

        self.sprite_list.append(self.sprite)

        self.up = False
        self.down = True
        self.right = False
        self.left = False
        self.player_speed = 4

        self.shape_list = None
        self.shape_list = arcade.ShapeElementList()

        shape = arcade.create_rectangle_filled(self.width/2, self.height/2, 100, 50, arcade.color.RED)
        self.shape_list.append(shape)

        self.kollisjon = False

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

        self.shape_list.draw()

    def on_update(self, delta_time):


        if self.right:
            if (self.width / 2 - 76) < (self.player_x + 4) < (self.width / 2) and (self.height / 2 - 60) < self.player_y < (self.height / 2 + 59):
                self.player_x = (self.width / 2 - 76)
            else:
                self.player_x += self.player_speed
        if self.left:
            if (self.width / 2 + 76) > (self.player_x - 4) > (self.width / 2) and (self.height / 2 - 60) < self.player_y < (self.height / 2 + 59):
                self.player_x = (self.width / 2 + 76)
            else:
                self.player_x -= self.player_speed
        if self.up:
            if (self.width / 2 - 75) < self.player_x < (self.width / 2 + 75) and (self.height / 2 - 61) < (self.player_y + 4) < (self.height / 2):
                print(2)
                self.player_y = (self.height / 2 - 61)
            else:
                self.player_y += self.player_speed
        if (self.width/2 - 75) < self.player_x < (self.width/2 + 75) and (self.height/2 - 60) < self.player_y < (self.height/2 + 60):
            #print(1)
            self.down = False
        else:
            self.down = True

        if self.down:
            #print(1)
            #self.player_y -= self.player_speed * delta_time
            self.player_y -= 2
        self.sprite.set_position(self.player_x, self.player_y)

        if self.player_y > self.height:
            self.player_y = self.height
        if self.player_y < 0:
            self.player_y = 0
        if self.player_x > self.width:
            self.player_x = self.width
        if self.player_x < 0:
            self.player_x = 0


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