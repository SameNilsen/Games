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

        #self.sprite_list.append(self.sprite2)

        self.up = False
        self.down = False
        self.right = False
        self.left = False

        self.particle_x_liste = []
        self.particle_y_liste = []

        self.particle_move_liste = []
        self.angle_liste = []
        self.distance = 0
        self.variabel_liste = []

        for i in range(100, 500, 5):
            for o in range(200, 800, 5):
                #particle = arcade.create_ellipse_filled(o, i, 1, 1, arcade.color.RED)
                self.particle = arcade.Sprite("Sprite/ShrekIMG5.png", center_x=100, center_y=100, scale=0.01)
                self.x = o
                self.y = i
                self.particle.set_position(self.x, self.y)
                self.sprite_list.append(self.particle)
                self.particle_x_liste.append(o)
                self.particle_y_liste.append(i)
                self.variabel_liste.append(1)
                self.particle_move_liste.append(0)
                self.angle_liste.append(0)
                print(i, o)

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

        arcade.draw_text(f"{self.target_x}, {self.target_y}", 50, self.height - 100, arcade.color.DARK_RED, 20)

        self.shape_list.draw()


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

        for i in range(0, len(self.variabel_liste)):
            self.distance = math.sqrt(abs((self.x - self.particle_x_liste[i]) ** 2 + (self.y - self.particle_y_liste[i]) ** 2))
            if self.particle_move_liste[i] == 1:
                change = 25 - ((self.distance * 0.08) * self.variabel_liste[i])
                if change >= 0:
                    change_x = (math.cos(math.radians(self.angle_liste[i]))) * change
                    change_y = (math.sin(math.radians(self.angle_liste[i]))) * change
                    self.sprite_list[i].set_position((self.sprite_list[i]._get_center_x() + change_x), (self.sprite_list[i]._get_center_y() + change_y))
                    self.variabel_liste[i] += 0.5
                    self.particle_x_liste[i] += change_x
                    self.particle_y_liste[i] += change_y
                else:
                    self.particle_move_liste[i] = 0
                    self.variabel_liste[i] = 1
                    print("FLYTTA")


    def on_mouse_motion(self, x, y, dx, dy):
        self.target_x = x
        self.target_y = y
        # print(x, y)

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):

        self.x = x
        self.y = y

        #print(1111, self.distance)
        #print(2222, self.particle_x, x, self.particle_y, y, (x - self.particle_x), (y - self.particle_y))
        for i in range(0, len(self.variabel_liste)):
            self.distance = math.sqrt(abs((self.x - self.particle_x_liste[i]) ** 2 + (self.y - self.particle_y_liste[i]) ** 2))
            if (y - self.particle_y_liste[i]) != 0 and (x - self.particle_x_liste[i]) != 0:
                print(2342342343242424)
                self.angle = math.degrees(math.atan((y - self.particle_y_liste[i])/(x - self.particle_x_liste[i])))
                if (y-self.particle_y_liste[i]) > 0:
                    if self.angle < 0:
                        self.angle += 360
                    else:
                        self.angle += 180
                else:
                    if (x-self.particle_x_liste[i]) > 0:
                        self.angle += 180
            elif (y - self.particle_y_liste[i]) == 0:
                if (x - self.particle_x_liste[i]) > 0:
                    self.angle = 180
                elif (x - self.particle_x_liste[i]) < 0:
                    self.angle = 0
            elif (x - self.particle_x_liste[i]) == 0:
                if (y - self.particle_y_liste[i]) > 0:
                    self.angle = 270
                elif (y - self.particle_y_liste[i]) < 0:
                    self.angle = 90
            self.angle_liste[i] = self.angle
            print("angle:", (self.angle-180), "retning:", self.angle)

            if self.distance < 300:
                self.particle_move_liste[i] = 1
        #self.shape_list.move((math.cos(math.radians(angle)))*20, (math.sin(math.radians(angle)))*20)

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.RIGHT:
            self.right = True
        if symbol == arcade.key.LEFT:
            self.left = True
        if symbol == arcade.key.UP:
            self.up = True
        if symbol == arcade.key.DOWN:
            self.down = True



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
