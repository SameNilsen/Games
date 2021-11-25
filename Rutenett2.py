import arcade
import math
import random

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

class MyGameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title, resizable=True)
        #arcade.set_background_color(arcade.color.BLACK)

        self.sprite_list = None
        self.sprite_list = arcade.SpriteList()

        self.shape_list = None
        self.shape_list = arcade.ShapeElementList()

        self.sprite = arcade.Sprite("Sprite/BOX.png", center_x=100, center_y=100, scale=1)
        self.player_x = 110
        self.player_y = 530
        self.sprite.set_position(self.player_x, self.player_y)

        self.sprite_list.append(self.sprite)

        self.up = False
        self.down = False
        self.right = False
        self.left = False
        self.player_speed = 20

        self.shape_list = None
        self.shape_list = arcade.ShapeElementList()
        self.points_list = []
        for i in range(0, 540, 20):
            self.points_list.append([0, i])
            self.points_list.append([1280, i])
        for o in range(0, 1000, 20):
            self.points_list.append([o, 0])
            self.points_list.append([o, 520])
        shape = arcade.create_lines(self.points_list, arcade.color.BROWN, 1)
        self.shape_list.append(shape)

        self.hinder_liste = None
        self.hinder_liste = arcade.ShapeElementList()
        self.hinder_points_liste = []
        for i in range(0, 400):
            a = random.randrange(10, 990, 20)
            b = random.randrange(10, 520, 20)
            self.hinder_points_liste.append([a, b])

        self.goal_x = random.randrange(10, 990, 20)
        self.goal_y = random.randrange(10, 520, 20)
        self.goal = arcade.create_ellipse_filled(self.goal_x, self.goal_y, 5, 5, arcade.color.YELLOW)

        self.input_liste = []
        self.enter = False
        self.go = False

        self.timer = 0.0

        self.win = False
        self.game_over = False

        self.drill_x = self.player_x
        self.drill_y = self.player_y

        self.grave_liste = None
        self.grave_liste = arcade.ShapeElementList()

    def on_resize(self, width, height):
        # Call the parent. Failing to do this will mess up the coordinates, and default to 0,0 at the center and the
        # edges being -1 to 1.
        super().on_resize(width, height)

        self.width = width
        self.height = height

        self.sprite.scale = 0.2

        print(self.width, self.height)

    def on_draw(self):
        arcade.start_render()

        self.background = arcade.load_texture("Sprite/Muldvarp_bakgrunn.png")
        # self.background.draw(0, 0, self.width, self.height)
        arcade.draw_texture_rectangle(self.width // 2, self.height // 2, self.width, self.height, self.background)

        arcade.draw_text(f"{self.target_x}, {self.target_y}", 50, self.height - 50, arcade.color.DARK_RED, 20)

        self.grave_liste.draw()

        self.shape_list.draw()

        self.sprite_list.draw()

        self.hinder_liste.draw()

        self.goal.draw()

        if self.win:
            arcade.draw_text("KULT", self.width/2, self.height/2, arcade.color.PINK, 40)

        if self.game_over:
            arcade.draw_text("TRAGISK", self.width/2, self.height/2, arcade.color.PINK, 40)

    def on_update(self, delta_time):
        self.timer += delta_time

        if self.go:
            #print("timer:", self.timer, "hold", self.hold)
            if self.timer >= (self.hold + 0.3):
                print("aaaaa", self.a)
                if self.input_liste[self.a] == 1:
                    self.player_x += self.player_speed
                if self.input_liste[self.a] == 2:
                    self.player_x -= self.player_speed
                if self.input_liste[self.a] == 3:
                    self.player_y += self.player_speed
                if self.input_liste[self.a] == 4:
                    self.player_y -= self.player_speed
                self.sprite.set_position(self.player_x, self.player_y)
                self.a += 1
                self.hold = self.timer
            if self.a == len(self.input_liste):
                self.input_liste = []
                self.go = False


        if self.right:
            self.player_x += self.player_speed
        if self.left:
            self.player_x -= self.player_speed
        if self.up:
            self.player_y += self.player_speed
        if self.down:
            self.player_y -= self.player_speed

        self.sprite.set_position(self.player_x, self.player_y)

        if self.player_x == self.goal_x:
            if self.player_y == self.goal_y:
                self.go = False
                self.enter = False
                self.win = True

        if arcade.get_pixel(self.player_x, self.player_y) == arcade.color.BLUE:
            self.go = False
            self.enter = False
            self.game_over = True

        for i in range(0, len(self.hinder_points_liste)):
            drill_xy = [self.drill_x, self.drill_y]
            if drill_xy == self.hinder_points_liste[i]:
                print(self.hinder_points_liste[i])
                a = self.drill_x
                b = self.drill_y
                dot = arcade.create_ellipse_filled(a, b, 5, 5, arcade.color.BLUE)
                self.hinder_liste.append(dot)
                break
            else:
                c = self.drill_x
                d = self.drill_y
                square = arcade.create_rectangle_filled(c, d, 10, 10, arcade.color.RED)
                self.grave_liste.append(square)

    def on_mouse_motion(self, x, y, dx, dy):
        self.target_x = x
        self.target_y = y
        # print(x, y)

    def on_key_press(self, symbol, modifiers):
        if self.enter is True and self.go is False:
            if symbol == arcade.key.RIGHT:
                self.input_liste.append(1)
                #self.player_x += self.player_speed
            if symbol == arcade.key.LEFT:
                self.input_liste.append(2)
                #self.player_x -= self.player_speed
            if symbol == arcade.key.UP:
                self.input_liste.append(3)
                #self.player_y += self.player_speed
            if symbol == arcade.key.DOWN:
                self.input_liste.append(4)
                #self.player_y -= self.player_speed
            """
            if symbol == arcade.key.NUM_1:
                self.input_liste.append(5)
            if symbol == arcade.key.NUM_2:
                self.input_liste.append(6)
            if symbol == arcade.key.NUM_3:
                self.input_liste.append(7)
            if symbol == arcade.key.NUM_4:
                self.input_liste.append(8)
            if symbol == arcade.key.NUM_5:
                self.input_liste.append(9)
            if symbol == arcade.key.NUM_6:
                self.input_liste.append(10)
            if symbol == arcade.key.NUM_7:
                self.input_liste.append(11)
            if symbol == arcade.key.NUM_8:
                self.input_liste.append(12)
            """

        #self.sprite.set_position(self.player_x, self.player_y)

        if symbol == arcade.key.ENTER:
            if self.enter == False:
                self.enter = True
            elif self.enter:
                self.enter = False
            print(self.enter)
            print(self.player_x, self.player_y)
            print(self.goal_x, self.goal_y)

        if len(self.input_liste) > 0:
            if symbol == arcade.key.SPACE:
                self.go = True
                self.hold = self.timer
                self.a = 0
                print(self.input_liste)

        if symbol == arcade.key.P:
            print(self.hinder_points_liste)


        if symbol == arcade.key.ESCAPE:
            arcade.close_window()

        if symbol == arcade.key.D:
            self.drill_x = self.player_x + 20
            self.drill_y = self.player_y
        if symbol == arcade.key.A:
            self.drill_x = self.player_x - 20
            self.drill_y = self.player_y
        if symbol == arcade.key.W:
            self.drill_x = self.player_x
            self.drill_y = self.player_y + 20
        if symbol == arcade.key.S:
            self.drill_x = self.player_x
            self.drill_y = self.player_y - 20

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
