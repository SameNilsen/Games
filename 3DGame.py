import arcade
import math
import random


SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
VIEWPORT_MARGIN = 40

class MyGameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title, resizable=True)
        self.set_mouse_visible(False)

        self.sprite_list = None
        self.sprite_list = arcade.SpriteList()

        self.shape_list = None
        self.shape_list = arcade.ShapeElementList()

        self.sprite = arcade.Sprite("Sprite/ShrekIMG5.png", center_x=100, center_y=100, scale=0.07)
        self.player_x = 700
        self.player_y = 300
        self.player_resize = False
        self.sprite.set_position(self.player_x, self.player_y)

        self.sprite_list.append(self.sprite)

        self.sprite2 = arcade.Sprite("Sprite/Høne.png", center_x=100, center_y=100, scale=0.1)
        self.player2_x = 200
        self.player2_y = 100
        self.player2_speed = 100
        self.sprite2.set_position(self.player2_x, self.player2_y)

        self.shadow = arcade.Sprite("Sprite/shadow.png", center_x=100, center_y=100, scale=0.1)
        self.shadow_x = 200
        self.shadow_y = 65
        self.shadow.set_position(self.shadow_x, self.shadow_y)

        self.sprite_list.append(self.shadow)

        self.sprite_list.append(self.sprite2)

        self.up = False
        self.down = False
        self.right = False
        self.left = False

        self.forward = False
        self.backward = False

        self.view_bottom = 0
        self.view_left = 0

        self.total_time = 0.0

        #self.shadow_x = 25
        #self.shadow = arcade.create_ellipse_filled(self.player2_x, self.player2_y-35, self.shadow_x, 10, arcade.color.BLACK)
        #self.shape_list.append(self.shadow)


    def on_resize(self, width, height):

        # Call the parent. Failing to do this will mess up the coordinates, and default to 0,0 at the center and the
        # edges being -1 to 1.
        super().on_resize(width, height)

        self.width = width
        self.height = height

        print(self.width, self.height)

    def on_draw(self):
        arcade.start_render()

        self.background = arcade.load_texture("Sprite/3dgrid.jpg")
        arcade.draw_texture_rectangle(self.width/2, self.height/2, self.width, self.height, self.background)

        self.shape_list.draw()
        self.sprite_list.draw()

        #arcade.draw_text(f"{self.target_x}, {self.target_y}", 50, self.height - 100, arcade.color.DARK_RED, 20)

        arcade.draw_point(self.width/2, self.height/2, arcade.color.RED, 5)

        #arcade.draw_text(f"{self.player2_x//1, self.player2_y//1}", 0, self.height-50, arcade.color.DARK_RED)
        arcade.draw_text(f"{self.x, self.y}", 0, self.height - 100, arcade.color.DARK_RED)
        arcade.draw_text(f"view_bottom:{self.view_bottom}", 0, self.height - 150, arcade.color.DARK_RED)
        arcade.draw_text(f"top_bndry{self.top_bndry}", 0, self.height - 200, arcade.color.DARK_RED)

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


        self.shadow_x = self.player_x
        self.shadow_y = 75
        self.shadow.set_position(self.shadow_x, self.shadow_y)

        changed = False

        # Scroll left
        left_bndry = self.view_left + VIEWPORT_MARGIN
        if self.sprite2.left < left_bndry:
            self.view_left -= left_bndry - self.sprite2.left
            changed = True

        # Scroll right
        right_bndry = self.view_left + self.width - VIEWPORT_MARGIN
        if self.sprite2.right > right_bndry:
            self.view_left += self.sprite2.right - right_bndry
            changed = True
        # print(self.view_bottom)

        # Scroll up
        self.top_bndry = self.view_bottom + self.height - VIEWPORT_MARGIN
        if self.sprite2.top > self.top_bndry:
            self.view_bottom += self.sprite2.top - self.top_bndry
            changed = True

        # Scroll down
        bottom_bndry = self.view_bottom + VIEWPORT_MARGIN
        if self.sprite2.bottom < bottom_bndry:
            self.view_bottom -= bottom_bndry - self.sprite2.bottom
            changed = True

        if changed:
            arcade.set_viewport(self.view_left,
                                self.width + self.view_left,
                                self.view_bottom,
                                self.height + self.view_bottom)


    def on_mouse_motion(self, x, y, dx, dy):
        self.target_x = x
        self.target_y = y
        # print(x, y)

        self.x = x
        self.y = y

        self.player_x = self.x
        self.player_y = self.y

        #if self.x > 14286 * self.sprite.scale:
        #    self.player_x = 14286 * self.sprite.scale
        #if self.x < 1000 - (14286*self.sprite.scale):
        #    self.player_x = 1000 - (14286*self.sprite.scale)

        self.sprite.set_position(self.player_x, self.player_y)

        if self.forward:
            if self.sprite.scale > 0.03:
                self.sprite.scale -= 0.005
        if self.backward:
            if self.sprite.scale < 0.3:
                self.sprite.scale += 0.005
        print(self.sprite.scale)
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

        if symbol == arcade.key.W:
            self.forward = True
        if symbol == arcade.key.S:
            self.backward = True



    def on_key_release(self, symbol, modifiers):
            if symbol == arcade.key.RIGHT:
                self.right = False
            if symbol == arcade.key.LEFT:
                self.left = False
            if symbol == arcade.key.UP:
                self.up = False
            if symbol == arcade.key.DOWN:
                self.down = False

            if symbol == arcade.key.W:
                self.forward = False
            if symbol == arcade.key.S:
                self.backward = False


MyGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT, 'My Game window')
arcade.run()
