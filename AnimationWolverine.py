import arcade
import math
import random


SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

#  FAIL  for store bilder(?)

class MyGameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title, resizable=True)

        self.sprite_list = None
        self.sprite_list = arcade.SpriteList()

        self.shape_list = None
        self.shape_list = arcade.ShapeElementList()

        self.wolverine = None
        self.wolverine = arcade.AnimatedTimeSprite()
        self.wolverine.textures = []
        self.wolverine.textures.append(arcade.load_texture("Sprite/Wolverine_ani/Ja/Wolverine30.jpg", scale=0.7))
        self.wolverine.textures.append(arcade.load_texture("Sprite/Wolverine_ani/Ja/Wolverine29.jpg", scale=0.7))
        self.wolverine.textures.append(arcade.load_texture("Sprite/Wolverine_ani/Ja/Wolverine28.jpg", scale=0.7))
        self.wolverine.textures.append(arcade.load_texture("Sprite/Wolverine_ani/Ja/Wolverine27.jpg", scale=0.7))
        self.wolverine.textures.append(arcade.load_texture("Sprite/Wolverine_ani/Ja/Wolverine26.jpg", scale=0.7))

        self.wolverine.textures.append(arcade.load_texture("Sprite/Wolverine_ani/Ja/Wolverine25.jpg", scale=0.7))
        self.wolverine.textures.append(arcade.load_texture("Sprite/Wolverine_ani/Ja/Wolverine24.jpg", scale=0.7))

        self.wolverine.textures.append(arcade.load_texture("Sprite/Wolverine_ani/Ja/Wolverine23.jpg", scale=0.7))
        self.wolverine.textures.append(arcade.load_texture("Sprite/Wolverine_ani/Ja/Wolverine22.jpg", scale=0.7))

        self.wolverine.textures.append(arcade.load_texture("Sprite/Wolverine_ani/Ja/Wolverine21.jpg", scale=0.7))

        self.wolverine.textures.append(arcade.load_texture("Sprite/Wolverine_ani/Ja/Wolverine20.jpg", scale=0.7))
        """
        
        self.wolverine.textures.append(arcade.load_texture("Sprite/Wolverine_ani/Ja/Wolverine19.jpg", scale=0.7))
        self.wolverine.textures.append(arcade.load_texture("Sprite/Wolverine_ani/Ja/Wolverine18.jpg", scale=0.7))
        self.wolverine.textures.append(arcade.load_texture("Sprite/Wolverine_ani/Ja/Wolverine17.jpg", scale=0.7))
        self.wolverine.textures.append(arcade.load_texture("Sprite/Wolverine_ani/Ja/Wolverine16.jpg", scale=0.7))
        self.wolverine.textures.append(arcade.load_texture("Sprite/Wolverine_ani/Ja/Wolverine15.jpg", scale=0.7))
        self.wolverine.textures.append(arcade.load_texture("Sprite/Wolverine_ani/Ja/Wolverine14.jpg", scale=0.7))
        self.wolverine.textures.append(arcade.load_texture("Sprite/Wolverine_ani/Ja/Wolverine13.jpg", scale=0.7))
        self.wolverine.textures.append(arcade.load_texture("Sprite/Wolverine_ani/Ja/Wolverine12.jpg", scale=0.7))
        self.wolverine.textures.append(arcade.load_texture("Sprite/Wolverine_ani/Ja/Wolverine11.jpg", scale=0.7))
        self.wolverine.textures.append(arcade.load_texture("Sprite/Wolverine_ani/Ja/Wolverine10.jpg", scale=0.7))
        
        self.wolverine.textures.append(arcade.load_texture("Sprite/Wolverine_ani/Ja/Wolverine9.jpg", scale=0.7))
        self.wolverine.textures.append(arcade.load_texture("Sprite/Wolverine_ani/Ja/Wolverine8.jpg", scale=0.7))
        self.wolverine.textures.append(arcade.load_texture("Sprite/Wolverine_ani/Ja/Wolverine7.jpg", scale=0.7))
        self.wolverine.textures.append(arcade.load_texture("Sprite/Wolverine_ani/Ja/Wolverine6.jpg", scale=0.7))
        self.wolverine.textures.append(arcade.load_texture("Sprite/Wolverine_ani/Ja/Wolverine5.jpg", scale=0.7))
        self.wolverine.textures.append(arcade.load_texture("Sprite/Wolverine_ani/Ja/Wolverine4.jpg", scale=0.7))
        self.wolverine.textures.append(arcade.load_texture("Sprite/Wolverine_ani/Ja/Wolverine3.jpg", scale=0.7))
        self.wolverine.textures.append(arcade.load_texture("Sprite/Wolverine_ani/Ja/Wolverine2.jpg", scale=0.7))
        self.wolverine.textures.append(arcade.load_texture("Sprite/Wolverine_ani/Ja/Wolverine1.jpg", scale=0.7))
        self.wolverine.textures.append(arcade.load_texture("Sprite/Wolverine_ani/Ja/Wolverine0.jpg", scale=0.7))
        self.wolverine.textures.append(arcade.load_texture("Sprite/Wolverine_ani/Ja/Wolverine.jpg", scale=0.7))
        """
        self.sprite_list.append(self.wolverine)
        self.wolverine.center_x = 500
        self.wolverine.center_y = 300
        self.oppdater = False

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

        #self.sprite_list.append(self.sprite2)

        self.up = False
        self.down = False
        self.right = False
        self.left = False


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

        #self.background = arcade.load_texture("Sprite/Wolverine.jpg")
        # self.background.draw(0, 0, self.width, self.height)
        #arcade.draw_texture_rectangle(self.width // 2, self.height // 2, self.width, self.height, self.background)

        #if self.oppdater:
        self.sprite_list.draw()

        #arcade.draw_text(f"{self.target_x}, {self.target_y}", 50, self.height - 100, arcade.color.DARK_RED, 20)

        self.shape_list.draw()

        arcade.draw_point(self.width/2, self.height/2, arcade.color.RED, 5)


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


        self.sprite_list.update_animation()


    def on_mouse_motion(self, x, y, dx, dy):
        self.target_x = x
        self.target_y = y
        # print(x, y)

        self.x = x
        self.y = y


    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):

        self.x = x
        self.y = y

        print(arcade.get_pixel(x, y))

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
            self.oppdater = True



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
