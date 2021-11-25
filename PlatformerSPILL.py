import arcade
import math
import random


SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
VIEWPORT_MARGIN = 40


class MyGameWindow(arcade.Window):
    sprite_list = None
    sprite_list = arcade.SpriteList()

    def __init__(self, width, height, title):
        super().__init__(width, height, title, resizable=True)


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
        self.player2_speed = 200
        self.sprite2.set_position(self.player2_x, self.player2_y)

        self.sprite_list.append(self.sprite2)

        self.up = False
        self.down = False
        self.right = False
        self.left = False

        self.up_speed = 0.1

        self.total_time = 0.0

        #grinch = enemy(self.width, self.height, "None")
        #grinch.setup()

        self.retning = "høyre"

        self.view_left = 0
        self.view_bottom = 0

        self.antall_forsøk = 1
        self.top_høyde = 0.0

        self.bakgrunn_liste = []
        self.current_map = 0
        self.a = 1
        self.background = arcade.load_texture("Sprite/ChickenBakgrunn10.png")
        self.bakgrunn_liste.append(self.background)
        self.bakgrunn_liste.append(1750)
        self.background2 = arcade.load_texture("Sprite/ChickenBakgrunn11.png")
        self.bakgrunn_liste.append(self.background2)
        self.bakgrunn_liste.append(4500)

        self.god_mode = False


        for i in range(0, 60):
            a = arcade.create_rectangle_filled(self.width-50, i * 300, 50, 2, arcade.color.DARK_RED)
            #arcade.draw_xywh_rectangle_filled(self.width-50, i*100, 40, 5, arcade.color.DARK_RED)
            self.shape_list.append(a)


        self.setup()

    def setup(self):

        self.egg_list = None
        self.egg_list = arcade.SpriteList()

        for i in range(0, 30):
            self.egg = arcade.Sprite("Sprite/Egg.png", center_x=random.randint(0, 1000), center_y=random.randint(300, 3000), scale=0.1)
            self.egg_list.append(self.egg)
        self.egg = arcade.Sprite("Sprite/Egg.png", center_x=random.randint(0, 1000), center_y=50, scale=0.1)
        self.egg_list.append(self.egg)

        self.egg_speed = False

        self.total_time = 0.0
        self.egg_time = 3.0


    def on_resize(self, width, height):

        # Call the parent. Failing to do this will mess up the coordinates, and default to 0,0 at the center and the
        # edges being -1 to 1.
        super().on_resize(width, height)

        self.width = width
        self.height = height

        print(self.width, self.height)

    def on_draw(self):
        arcade.start_render()

        #self.background = arcade.load_texture("Sprite/ChickenBakgrunn.png")
        #self.background.draw(300, 1000, 1500, 3000)
        arcade.draw_texture_rectangle(self.width/2, self.bakgrunn_liste[self.current_map+1], self.width, 4000, self.bakgrunn_liste[self.current_map])

        if self.player2_y >= (self.a) * 3000:
            self.current_map += 2
            self.a += 1
            #self.player2_y = 500
            #arcade.set_viewport(self.view_left, self.view_left+self.width, 0, self.height)
            #self.view_bottom = 0
            self.setup()
        if self.a != 1:
            if self.player2_y <= (self.a - 1) * 3000 - 5:
                #arcade.set_viewport(self.view_left, self.view_left + self.width, 0, self.height)
                #self.view_bottom = 0
                self.current_map -= 2
                self.a -= 1
                #self.player2_y = 2995

        self.sprite_list.draw()
        self.egg_list.draw()

        #arcade.draw_text(f"{self.target_x}, {self.target_y}", 50, self.height - 100, arcade.color.DARK_RED, 20)


        self.shape_list.center_y = -self.view_bottom
        self.shape_list.draw()

        arcade.draw_point(self.width/2, self.height/2, arcade.color.RED, 5)

        if self.egg_speed:
            arcade.draw_text(f"{self.egg_time//1}", 50, self.view_bottom+self.height-100, arcade.color.DARK_RED)

        arcade.draw_text(f"Forsøk:{self.antall_forsøk}", self.width-200, self.view_bottom+self.height-100, arcade.color.DARK_RED, 40)
        #arcade.draw_text(f":{self.view_bottom}", self.width - 200, self.view_bottom + self.height - 150, arcade.color.DARK_RED, 40)
        arcade.draw_text(f"{self.top_høyde//1}", self.width/2, self.view_bottom+self.height-100, arcade.color.DARK_RED, 20)


    def on_update(self, delta_time):
        self.delta_time = delta_time

        if self.egg_speed:
            self.egg_time -= delta_time
            if self.egg_time <= 1.0:
                self.egg_speed = False



        if self.right:
            self.player2_x += self.player2_speed * delta_time
        if self.left:
            self.player2_x -= self.player2_speed * delta_time

        if self.up:
            self.player2_y += 100 * self.up_speed
            self.up_speed -= 0.007

        if self.down:
            self.player2_y -= self.player2_speed * delta_time
        if self.current_map == 0:
            if self.player2_y < 75:
                self.player2_y = 75
        else:
            pass

        if self.player2_x > self.width:
            self.player2_x = 0
        if self.player2_x < 0:
            self.player2_x = self.width

        self.sprite2.set_position(self.player2_x, self.player2_y)

        if self.player2_y > self.top_høyde:
            self.top_høyde = self.sprite2._get_center_y()


        for i in range(0, len(self.egg_list)):
            self.egg_avstand_x = self.egg_list[i]._get_center_x() - self.sprite2._get_center_x()
            self.egg_avstand_y = self.egg_list[i]._get_center_y() - self.sprite2._get_center_y()
            if math.sqrt(self.egg_avstand_x**2 + self.egg_avstand_y**2) < 50:
                self.egg_list[i].remove_from_sprite_lists()
                self.egg_speed = True
                self.egg_time = 2.0
                print(i)
                break

        changed = False

        """
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
        """
        # Scroll up
        top_bndry = self.view_bottom + self.height - VIEWPORT_MARGIN
        if self.sprite2.top > top_bndry:
            self.view_bottom += self.sprite2.top - top_bndry
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


    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):

        self.x = x
        self.y = y

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.RIGHT:
            if self.retning == "venstre":
                self.sprite2.turn_right(theta=180)

            self.retning = "høyre"
            self.right = True
        if symbol == arcade.key.LEFT:
            if self.retning == "høyre":
                self.sprite2.turn_right(theta=180)
            self.retning = "venstre"
            self.left = True
        if symbol == arcade.key.UP:
            if self.egg_speed is True or self.god_mode is True:
                self.up_speed = 0.15
                self.up = True
        if symbol == arcade.key.DOWN:
            self.down = True

        if symbol == arcade.key.SPACE:
            self.antall_forsøk += 1
            self.setup()

        if symbol == arcade.key.O:
            self.god_mode = True
        if symbol == arcade.key.I:
            self.god_mode = False


    def on_key_release(self, symbol, modifiers):
            if symbol == arcade.key.RIGHT:
                self.right = False
            if symbol == arcade.key.LEFT:
                self.left = False
            #if symbol == arcade.key.UP:
            #    self.up = False
            if symbol == arcade.key.DOWN:
                self.down = False
"""
class enemy(MyGameWindow):
    def __init__(self, width, height, title):
        print("hei")
        self.enemy1 = arcade.Sprite("Sprite/ShrekIMG5.png", center_x=100, center_y=100, scale=0.1)
        self.x = width / 2
        self.y = height / 2
        self.enemy1.set_position(self.x, self.y)

        self.sprite_list.append(self.enemy1)
    def setup(self):
        print(222)
        MyGameWindow.sprite_list.append(self.enemy1)

    def move(self):
        pass
"""
MyGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT, 'My Game window')
arcade.run()
