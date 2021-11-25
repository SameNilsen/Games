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

        self.v_0 = 0

        self.alfa = math.radians(90)
        print(math.cos(self.alfa))

        self.total_time = 0.0

        self.run = False

        self.start_dot = True

        self.speed_input = True
        self.angle_input = False

        self.speed_input_list = [0, 0, 0]
        self.angle_input_list = [0, 0, 0]

        self.speed_pressed = False
        self.angle_pressed = False
        self.writing_line_timer = 0.0
        self.speed_writing_line_timer = 0.0
        self.speed_input_position = 0
        self.angle_input_position = 0
        self.angle_writing_line_timer = 0.0


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

        arcade.draw_text(f"Press ENTER to start", 50, self.height - 70, arcade.color.DARK_RED, 20)
        arcade.draw_text(f"{self.target_x}, {self.target_y}", 50, self.height - 100, arcade.color.DARK_RED, 20)

        if self.start_dot:
            if math.sqrt((self.x**2) + (self.y**2)) > 50:
                self.dot_x = self.x
                self.dot_y = self.y
                #dot = arcade.draw_circle_filled(self.dot_x, self.dot_y, 5, arcade.color.RED)
                dot = arcade.create_ellipse_filled_with_colors(self.dot_x, self.dot_y, 5, 5, arcade.color.RED, arcade.color.RED)
                self.shape_list.append(dot)
                self.start_dot = False
        if self.start_dot == False:
            if math.sqrt((self.x - self.dot_x)**2 + (self.dot_y - self.y)**2) > 50:
                self.dot_x = self.x
                self.dot_y = self.y
                #dot = arcade.draw_circle_filled(self.dot_x, self.dot_y, 5, arcade.color.RED)
                dot = arcade.create_ellipse_filled_with_colors(self.dot_x, self.dot_y, 5, 5, arcade.color.RED, arcade.color.RED)
                self.shape_list.append(dot)

        if self.y <= 0 or self.x >= 1920:
            arcade.draw_text(f"{self.x}, {self.y}", 50, self.height - 130, arcade.color.RED, 20)
            #print(self.x, self.y)

        self.shape_list.draw()

        arcade.draw_text(f"Fart: {self.speed_input_list[-3]} {self.speed_input_list[-2]} {self.speed_input_list[-1]}", 50, self.height - 160, arcade.color.RED, 20)
        arcade.draw_text(f"Vinkel: {self.angle_input_list[-3]} {self.angle_input_list[-2]} {self.angle_input_list[-1]}", 50, self.height - 190, arcade.color.RED, 20)

        #arcade.draw_xywh_rectangle_outline(50, self.height - 160, 100, 20, arcade.color.RED)
        #arcade.draw_xywh_rectangle_outline(50, self.height - 190, 125, 20, arcade.color.RED)

        if self.speed_pressed:
            #print(self.writing_line_timer, self.speed_writing_line_timer)
            if (self.speed_writing_line_timer + 0.5) < self.writing_line_timer < (self.speed_writing_line_timer + 1):
                if self.speed_input_position == 0:
                    arcade.draw_rectangle_filled(155, self.height - 150, 2, 20, arcade.color.RED)
                if self.speed_input_position == 1:
                    arcade.draw_rectangle_filled(135, self.height - 150, 2, 20, arcade.color.RED)
                if self.speed_input_position == 2:
                    arcade.draw_rectangle_filled(116, self.height - 150, 2, 20, arcade.color.RED)
            if self.writing_line_timer > (self.speed_writing_line_timer + 1):
                self.speed_writing_line_timer = self.writing_line_timer

        if self.angle_pressed:
            #print(self.writing_line_timer, self.angle_writing_line_timer)
            if (self.angle_writing_line_timer + 0.5) < self.writing_line_timer < (self.angle_writing_line_timer + 1):
                if self.angle_input_position == 0:
                    arcade.draw_rectangle_filled(175, self.height - 180, 2, 20, arcade.color.RED)
                if self.angle_input_position == 1:
                    arcade.draw_rectangle_filled(158, self.height - 180, 2, 20, arcade.color.RED)
                if self.angle_input_position == 2:
                    arcade.draw_rectangle_filled(139, self.height - 180, 2, 20, arcade.color.RED)
            if self.writing_line_timer > (self.angle_writing_line_timer + 1):
                self.angle_writing_line_timer = self.writing_line_timer


    def on_update(self, delta_time):
        self.writing_line_timer += delta_time

        if self.run:
            if self.y >= 0 and self.x <= 1920:
                self.total_time += delta_time
                self.seconds = self.total_time % 60
                #print(self.total_time, self.seconds)
                self.v_0 = (int(self.speed_input_list[-1]) + int(self.speed_input_list[-2])*10 + int(self.speed_input_list[-3])*100)
                #print(self.v_0)

                self.alfa = math.radians((int(self.angle_input_list[-1]) + int(self.angle_input_list[-2]) * 10 + int(self.angle_input_list[-3]) * 100))
                #print(math.cos(self.alfa))

                self.x = self.v_0*(math.cos(self.alfa))*self.total_time
                self.y = (self.v_0*(math.sin(self.alfa))*self.total_time) - (1/2 * 9.81 * (self.total_time)**2)

                self.sprite.set_position(self.x, self.y)

            else:
                self.run = False

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

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        if x > 50:
            if x < 150:
                if y > self.height - 160:
                    if y < self.height - 140:
                        print("hei", random.randint(0, 100))
                        self.speed_pressed = True
                        self.speed_input = True
                        self.angle_input = False
                        self.angle_pressed = False
                        self.speed_writing_line_timer = self.writing_line_timer
        if x > 50:
            if x < 175:
                if y > self.height - 190:
                    if y < self.height - 170:
                        print("hei 3", random.randint(0, 100))
                        self.speed_pressed = False
                        self.speed_input = False
                        self.angle_input = True
                        self.angle_pressed = True
        #button.on_press()

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
            if self.run == False:
                self.run = True
            elif self.run == True:
                self.run = False

        if symbol == arcade.key.S:
            #print(str(chr(symbol)))
            if self.speed_input == False:
                self.speed_input = True
            elif self.speed_input == True:
                self.speed_input = False
            if self.angle_input:
                self.angle_input = False

        if symbol == arcade.key.A:
            if self.angle_input == False:
                self.angle_input = True
            elif self.angle_input == True:
                self.angle_input = False
            if self.speed_input:
                self.speed_input = False

        if symbol == arcade.key.TAB:
            if self.speed_input:
                self.speed_input = False
                self.angle_input = True
                self.speed_pressed = False
                self.angle_pressed = True
            elif self.angle_input:
                self.angle_input = False
                self.speed_input = True
                self.angle_pressed = False
                self.speed_pressed = True

        if self.run == False:
            if self.speed_input:
                if 48 <= symbol <= 57:
                    if len(self.speed_input_list) < 6:
                        print(1)
                        #self.input_list.append(str(chr(symbol)))
                        #self.speed_input_list.append(str(chr(symbol)))
                        self.speed_input_list[(5-self.speed_input_position):(5-self.speed_input_position)] = [str(chr(symbol))]
                        print(len(self.speed_input_list))
                        print(self.speed_input_list)

                if symbol == arcade.key.BACKSPACE:
                    if len(self.speed_input_list) > 3:
                        self.speed_input_list.pop(-(self.speed_input_position + 1))

            if self.angle_input:
                if 48 <= symbol <= 57:
                    if len(self.angle_input_list) < 6:
                        #self.angle_input_list.append(str(chr(symbol)))
                        self.angle_input_list[(5-self.angle_input_position):(5-self.angle_input_position)] = [str(chr(symbol))]

                if symbol == arcade.key.BACKSPACE:
                    if len(self.angle_input_list) > 3:
                        self.angle_input_list.pop(-(self.angle_input_position + 1))

        if symbol == arcade.key.ESCAPE:
            self.run = False
            self.x = 0
            self.y = 0
            self.dot_x = 0
            self.dot_y = 0
            self.sprite.set_position(self.x, self.y)
            self.start_dot = True
            self.total_time = 0.0
            self.shape_list = None
            self.shape_list = arcade.ShapeElementList()

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
