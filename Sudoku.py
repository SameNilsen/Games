import arcade
import math
import random

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

class MyGameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title, resizable=True)

        arcade.set_background_color(arcade.color.WHITE)

        self.sprite_list = None
        self.sprite_list = arcade.SpriteList()

        self.sprite = arcade.Sprite("Sprite/ShrekIMG5.png", center_x=100, center_y=100, scale=0.1)
        self.x = 0
        self.y = 0
        self.sprite.set_position(self.x, self.y)

        self.sprite_list.append(self.sprite)

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

        self.run = False

        self.shape_list = arcade.ShapeElementList()
        i_1 = 3
        for i in range(250, 750, 50):
            if i_1 == 3 or i_1 == 0:
                shape = arcade.create_line(i, 50, i, 500, arcade.color.BLACK, 4)
                i_1 = 3
            else:
                shape = arcade.create_line(i, 50, i, 500, arcade.color.BLACK, 2)
            i_1 -= 1

            self.shape_list.append(shape)
        o_1 = 3
        for o in range(50, 550, 50):
            if o_1 ==3 or o_1 == 0:
                shape = arcade.create_line(250, o, 700, o, arcade.color.BLACK, 4)
                o_1 = 3
            else:
                shape = arcade.create_line(250, o, 700, o, arcade.color.BLACK, 2)
            o_1 -= 1
            self.shape_list.append(shape)

        self.horisontal_liste = []
        for i in range(1, 10):
            self.horisontal_liste.append([(i * 10) + 1])
            for o in range(2, 10):
                self.horisontal_liste[i - 1].append((10 * i) + o)
        self.horisontal_liste[0][1] = None
        print(self.horisontal_liste)

        self.vertikal_liste = []
        for i in range(0, 9):
            self.vertikal_liste.append([])
            for o in range(0, 9):
                self.vertikal_liste[i].append(self.horisontal_liste[o][i])
        print(self.vertikal_liste)

        self.firkant_liste = []
        for a in range(0, 3):
            for i in range(0, 3):
                self.firkant_liste.append([])
                for o in range(0, 3):
                    for b in range(0, 3):
                        self.firkant_liste[((a*3)+i)].append(self.horisontal_liste[((i*3)+o)][((a*3)+b)])
        print(self.firkant_liste)

        self.alt = []
        self.alt.append(self.horisontal_liste)
        self.alt.append(self.vertikal_liste)
        self.alt.append(self.firkant_liste)
        print(len(self.alt), self.alt)

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

        i_2 = 0
        for i in range(460, 10, -50):
            o_2 = 0
            for o in range(260, 710, 50):
                if self.horisontal_liste[i_2][o_2] != None:
                    arcade.draw_text(f"{self.horisontal_liste[i_2][o_2]}", o, i, arcade.color.BLACK, 20)
                #print(self.horisontal_liste[i_2][o_2])
                o_2 += 1
            i_2 += 1

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
        """
        a = [3, 5, 1, 9, 6, 8, 4, 2, 7]
        if len(a) == 9:
            feil = 0
            for b in range(0, len(a)):
                if a[b] == None:
                    feil = 10
            for i in range(0, len(a)):
                for o in range(0, len(a)):
                    if i != o:
                        if a[i] == a[o]:
                            feil += 1
            if feil >= 1:
                print("feil", a)
            else:
                print("ye", a)
        """

    def on_mouse_motion(self, x, y, dx, dy):
        self.target_x = x
        self.target_y = y
        # print(x, y)


    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.RIGHT:
            self.right = True
        if symbol == arcade.key.LEFT:
            self.left = True
        if symbol == arcade.key.UP:
            self.up = True
        if symbol == arcade.key.DOWN:
            self.down = True


        if symbol == arcade.key.LEFT:
            if self.speed_input:
                self.speed_input_position += 1
                if self.speed_input_position > 2:
                    self.speed_input_position = 0
            if self.angle_input:
                self.angle_input_position += 1
                if self.angle_input_position > 2:
                    self.angle_input_position = 0
        if symbol == arcade.key.RIGHT:
            if self.speed_input:
                self.speed_input_position -= 1
                if self.speed_input_position < 0:
                    self.speed_input_position = 2
            if self.angle_input:
                self.angle_input_position -= 1
                if self.angle_input_position < 0:
                    self.angle_input_position = 2

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
