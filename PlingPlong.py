import arcade
import math
import random

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

class MyGameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title, resizable=True)
        self.set_mouse_visible(False)

        self.sprite_list = None
        self.sprite_list = arcade.SpriteList()

        self.shape_list = None
        self.shape_list = arcade.ShapeElementList()

        #self.sprite = arcade.Sprite("Sprite/ShrekIMG5.png", center_x=100, center_y=100, scale=0.1)
        #self.x = 0
        #self.y = 0
        #self.sprite.set_position(self.x, self.y)

        #self.sprite_list.append(self.sprite)

        self.up = False
        self.down = False
        self.right = False
        self.left = False

        bottom = arcade.create_line(0, 0, 1000, 0, arcade.color.RED, 5)
        top = arcade.create_line(0, 600, 1000, 600, arcade.color.RED, 5)
        left = arcade.create_line(0, 0, 0, 600, arcade.color.RED, 5)
        right = arcade.create_line(1000, 0, 1000, 600, arcade.color.RED, 5)

        self.shape_list.append(bottom)
        self.shape_list.append(top)
        self.shape_list.append(left)
        self.shape_list.append(right)

        self.player1 = arcade.Sprite("Sprite/Racket.png", center_x=100, center_y=100, scale=0.3)
        self.player1_x = self.width - 100
        self.player1_y = 300
        self.y = self.player1_y
        self.player1_speed = 100
        self.player1.set_position(self.player1_x, self.player1_y)

        self.sprite_list.append(self.player1)

        self.player2 = arcade.Sprite("Sprite/Racket.png", center_x=100, center_y=100, scale=0.3)
        self.player2_x = 100
        self.player2_y = 300
        self.player2_speed = 20
        self.player2.set_position(self.player2_x, self.player2_y)

        self.sprite_list.append(self.player2)

        self.ball = arcade.Sprite("Sprite/PingPongBall.png", center_x=500, center_y=300, scale=0.01)
        self.sprite_list.append(self.ball)
        self.ball_angle = random.randint(-28, 28)
        self.ball_speed = 10
        self.PingPongBing = arcade.sound.load_sound("Lyder/PingPong.wav")
        self.target = 300

        self.ball_x = 500
        self.ball_y = 300

        self.run = False
        self.goals_1 = 0
        self.goals_2 = 0
        self.hit = 0

        self.total_time = 0.0
        """
        for i in range(0, 1000, 5):
            for o in range(0, 600, 5):
                self.particle = arcade.Sprite("Sprite/ShrekIMG5.png", center_x=i, center_y=o, scale=0.01)
                if arcade.check_for_collision(self.ball, self.particle) == False:
                    self.sprite_list.append(self.particle)
        
        for i in range(0, 1000, 5):
            for o in range(0, 600, 5):
                self.particle = arcade.Sprite("Sprite/ShrekIMG5.png", center_x=i, center_y=o, scale=0.01)
                self.particle.alpha = 100
                if i > 840 and i < 955:
                    if o > self.player1_y-40 and o < self.player1_y+100:
                        self.sprite_list.append(self.particle)
        """

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
        arcade.draw_text(f"{self.goals_2}   :   {self.goals_1}", self.width/2 - 30, self.height - 50, arcade.color.DARK_RED, 20)
        arcade.draw_point(100, self.target, arcade.color.GREEN, 5)

        self.shape_list.draw()


    def on_update(self, delta_time):

        self.player1_x = self.width - 100
        self.player1_y = self.y
        self.player1.set_position(self.width - 100, self.y)

        if self.run:
            ballx = self.ball_x
            endring_x = math.cos(math.radians(self.ball_angle)) * self.ball_speed
            endring_y = math.sin(math.radians(self.ball_angle)) * self.ball_speed
            self.ball_x += endring_x
            self.ball_y += endring_y
            self.ball.set_position(self.ball_x, self.ball_y)
            retning = ballx - self.ball_x

            if retning < 0:
                if self.ball_x > (self.width-160) and self.ball_x < self.width-60:
                    if self.ball_y > self.player1_y - 40 and self.ball_y < self.player1_y + 100:
                        self.ball_angle = 180-self.ball_angle + random.randint(-10, 10)
                        arcade.sound.play_sound(self.PingPongBing)
                        if self.hit == 1:
                            self.ball_speed += 2
                            self.hit = 0
                        else:
                            self.hit += 1

            if retning > 0:
                if self.ball_x < 160 and self.ball_x > 60:
                    if self.ball_y > self.player2_y - 40 and self.ball_y < self.player2_y + 100:
                        self.ball_angle = 180-self.ball_angle + random.randint(-10, 10)
                        arcade.sound.play_sound(self.PingPongBing)

            if self.ball_y > self.height:
                self.ball_angle = 360 - self.ball_angle
            if self.ball_y < 0:
                self.ball_angle = 360 - self.ball_angle
            if self.ball_x > self.width:
                self.run = False
                self.ball_x = 500
                self.ball_y = 300
                self.ball.set_position(self.ball_x, self.ball_y)
                self.goals_2 += 1
            if self.ball_x < 0:
                self.run = False
                self.ball_x = 500
                self.ball_y = 300
                self.ball.set_position(self.ball_x, self.ball_y)
                self.goals_1 += 1

            if retning > 0:
                #stopp_y = 300 - (100/math.tan(math.radians(270-self.ball_angle)))
                stopp_y = self.ball_y + (math.tan(math.radians(180-self.ball_angle)) * (self.ball_x - 100))
                if abs(self.player2_y-stopp_y) > self.ball_speed:
                    if self.player2_y > stopp_y and self.player2_y > 30:
                        self.player2_y -= self.player2_speed
                    elif self.player2_y < stopp_y and self.player2_y < self.height-30:
                        self.player2_y += self.player2_speed
                self.target = stopp_y
                self.player2.set_position(self.player2_x, self.player2_y)

    def on_mouse_motion(self, x, y, dx, dy):
        self.target_x = x
        self.target_y = y
        # print(x, y)

        self.x = x
        self.y = y


    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):

        self.x = x
        self.y = y

        self.ball_angle = random.randint(-28, 28)
        self.hit = 0
        self.ball_speed = 20
        self.run = True

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
            self.ball_angle = random.randint(-28, 28)
            self.hit = 0
            self.ball_speed = 10
            self.run = True

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
