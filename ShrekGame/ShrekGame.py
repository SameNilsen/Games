import arcade
from time import sleep
import random
#from arcade.geometry import check_for_collision
from numpy import sqrt
import math
import numpy as np

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
VIEWPORT_MARGIN = 40
MOVEMENT_SPEED = 1

FACE_RIGHT = 1
FACE_LEFT = 2
FACE_UP = 3
FACE_DOWN = 4


class MyGameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title, resizable=True)

        self.data = np.loadtxt('Data_test.csv', delimiter=',')
        self.data = np.sort(self.data)
        print(self.data)

        self.seconds = 0

        self.width = width
        self.height = height

        self.map_x = 3000
        self.map_y = 1700

        #self.set_mouse_visible(False)

        # self.set_location(400, 200)

        # Startsposisjoner for Sprite1 og Sprite2 og Hamster

        self.player1_x = self.width / 2 - 300
        self.player1_y = self.height / 2
        self.player1_speed = 300

        self.player2_x = self.width / 2 + 300
        self.player2_y = self.height / 2
        self.player2_speed = 400

        self.sprite_list = None
        # self.sprite1 = arcade.Sprite("Sprite/Stan.png", center_x=100, center_y=100, scale=0.8)

        self.sprite2 = arcade.Sprite("Sprite/Høne.png", center_x=100, center_y=100, scale=0.1)
        self.sprite2.set_position(self.player2_x, self.player2_y)

        self.right1 = False
        self.left1 = False
        self.up1 = False
        self.down1 = False

        self.right2 = False
        self.left2 = False
        self.up2 = False
        self.down2 = False

        self.background = None

        self.total_time = 0.0

        self.round_counter = 0

        self.y_list = []

        self.enemy2_list = None

        self.sprite_list = arcade.SpriteList()
        self.enemy2_list = arcade.SpriteList()

        self.poeng1 = 100
        self.poeng2 = 100
        # self.sprite_list.append(self.sprite2)
        # self.sprite_list.append(self.sprite1)

        self.sprite5_x = 800
        self.sprite5_y = 100
        self.sprite5_speed = 250

        self.sprite5_follow = False

        self.sprite1_delete = False
        self.sprite2_delete = False

        self.test2 = False

        self.crash_fart = 0.5

        self.bullet_list = []

        self.bullet_list_x = None
        self.bullet_list_x = arcade.SpriteList()
        self.bullet_list.append(self.bullet_list_x)

        self.bullet_list_xn = None
        self.bullet_list_xn = arcade.SpriteList()
        self.bullet_list.append(self.bullet_list_xn)

        self.bullet_list_y = None
        self.bullet_list_y = arcade.SpriteList()
        self.bullet_list.append(self.bullet_list_y)

        self.bullet_list_yn = None
        self.bullet_list_yn = arcade.SpriteList()
        self.bullet_list.append(self.bullet_list_yn)

        self.bullet_make = False
        self.bullet_fire = False
        self.test3 = True
        self.test3_xn = True
        self.test3_y = True
        self.test3_yn = True

        self.fire0 = False
        self.fire1 = False
        self.fire2 = False
        self.fire3 = False

        self.player1_retning = 0

        self.gun_sound = arcade.sound.load_sound("Lyder/laser2.wav")
        self.reload_sound = arcade.sound.load_sound("Lyder/Reload.wav")
        self.joy_sound = arcade.sound.load_sound("Lyder/Joy.wav")
        self.sad_sound = arcade.sound.load_sound("Lyder/Sad.wav")
        self.start_sound = arcade.sound.load_sound("Lyder/Start.wav")

        self.view_bottom = 0
        self.view_left = 0

        self.penger = 0
        self.enemy_position = 0

        self.enemy_health = []
        self.enemy_color_list = []

        self.minutes = 0
        self.test4 = False
        self.sprite2_make = False
        self.sprite1_make = False

        self.sprite1_up = False

        self.sprite2_hit = False

        self.player_list = None
        self.sprite1 = None
        self.sprite1_show = False
        self.sprite2_show = False

        self.pause = False
        self.pause_menu = False
        self.test5 = True
        self.start_menu = True
        self.player_number = 1
        self.difficulty = 0
        self.game_over = False

        self.mouse_bullet = False
        self.bullet_01_list = None
        self.bullet_01_list = arcade.SpriteList()
        self.test6 = True
        self.bullet_01_fire = False
        self.degrees_list = []

        self.level_comment = ["Helt elendig", "Elendig", "Dårlig", "Ikke bra", "Innafor", "Bra", "Bedre enn meg", "Legendarisk", "GUD"]

        self.bullet_x_make = False
        self.bullet_xn_make = False
        self.bullet_y_make = False
        self.bullet_yn_make = False
        self.bullet_x_degrees_list = []
        self.bullet_xn_degrees_list = []
        self.bullet_y_degrees_list = []
        self.bullet_yn_degrees_list = []
        self.bullet_spread_max = 2
        self.bullet_spread_min = -2

        self.SH = False
        self.SV = False
        self.SU = False
        self.SD = False

        self.ammo = 20
        self.ammo_reserve = 0
        self.ammo_2 = 0
        self.ammo_pack_list = []
        self.ammo_texture_list = None
        self.ammo_texture_list = arcade.SpriteList()
        self.health_texture_list = None
        self.health_texture_list = arcade.SpriteList()

        self.save_score = True
        self.scoreboard_playernum = 0

        self.shape_list = None
        self.shape_list = arcade.ShapeElementList()
        shape = arcade.create_rectangle_filled(self.view_left + self.width/2, self.view_bottom + self.height/1.06, self.width-20, self.height/11, (100, 76, 160, 180))
        self.shape_list.append(shape)
        shape2 = arcade.create_rectangle_filled(self.view_left + self.width - self.width/6, self.view_bottom + self.height/8, self.width/5, self.height/10, (100, 76, 160, 180))
        self.shape_list.append(shape2)

        self.setup()

    def setup(self):

        self.player_list = arcade.SpriteList()
        self.sprite1 = arcade.AnimatedWalkingSprite()

        self.sprite1.stand_right_textures = []
        self.sprite1.stand_right_textures.append(arcade.load_texture("Sprite/Stan.png"))
        self.sprite1.stand_right_textures.append(arcade.load_texture("Sprite/Stan_Høyre.png"))
        self.sprite1.stand_left_textures = []
        self.sprite1.stand_left_textures.append(arcade.load_texture("Sprite/Stan_Venstre.png"))

        self.sprite1.walk_right_textures = []
        self.sprite1.walk_right_textures.append(arcade.load_texture("Sprite/Stan_Høyre.png"))
        self.sprite1.walk_right_textures.append(arcade.load_texture("Sprite/Høyre_gå.png"))

        self.sprite1.walk_left_textures = []
        self.sprite1.walk_left_textures.append(arcade.load_texture("Sprite/Stan_Venstre.png"))
        self.sprite1.walk_left_textures.append(arcade.load_texture("Sprite/Venstre_gå.png"))

        self.sprite1.walk_up_textures = []
        self.sprite1.walk_up_textures.append(arcade.load_texture("Sprite/Stan_rygg1.png"))
        self.sprite1.walk_up_textures.append(arcade.load_texture("Sprite/Stan_rygg2.png"))

        self.sprite1.walk_down_textures = []
        self.sprite1.walk_down_textures.append(arcade.load_texture("Sprite/Stan_down1.png"))
        self.sprite1.walk_down_textures.append(arcade.load_texture("Sprite/Stan_down2.png"))

        self.sprite1.scale = 0.8
        self.sprite1.texture_change_distance = 35
        self.player_list.append(self.sprite1)
        self.sprite1.set_position(self.player1_x, self.player1_y)

    def update_animation(self, delta_time: float = 1 / 60):
        if self.sprite1.change_x == 0 and self.sprite1.change_y == 0:
            print("y")
            if self.sprite1.state == FACE_LEFT:
                self.texture = self.sprite1.stand_right_textures[0]
            elif self.sprite1.state == FACE_RIGHT:
                self.texture = self.sprite1.stand_right_textures[0]
            elif self.sprite1.state == FACE_UP:
                self.texture = self.sprite1.walk_up_textures[0]
            elif self.sprite1.state == FACE_DOWN:
                self.texture = self.sprite1.walk_down_textures[0]
        print("h")
        if self.sprite1.state == FACE_LEFT:
            AA = self.target_x - self.sprite1._get_center_x()
            print(AA)
            if AA > 0:
                print("x1")
                self.sprite1.state = FACE_RIGHT

    def on_resize(self, width, height):

        # Call the parent. Failing to do this will mess up the coordinates, and default to 0,0 at the center and the
        # edges being -1 to 1.
        super().on_resize(width, height)

        self.width = width
        self.height = height

        print(self.width, self.height)

    def on_draw(self):

        arcade.start_render()

        """
        Tegner bakgrunnen avhengig av variabel
        """
        # arcade.draw_xywh_rectangle_filled(self.map_x/2 * -1, self.map_y/2 * -1, -150, self.map_y, (11, 210, 0))
        # arcade.draw_xywh_rectangle_filled(self.map_x/2, self.map_y/2 * -1, 150, self.map_y, (11, 210, 0))
        # arcade.draw_xywh_rectangle_filled((self.map_x/2 * -1) - 150, self.map_y/2 * -1, self.map_x + 300, -150, (11, 210, 0))
        # arcade.draw_xywh_rectangle_filled((self.map_x/2 * -1) - 150, self.map_y/2, self.map_x + 300, 150, (11, 210, 0))

        self.background = arcade.load_texture("Sprite/Bakgrunn1.png")
        self.background.draw_sized(0, 0, self.map_x, self.map_y)
        # arcade.draw_texture_rectangle(self.width // 2, self.height // 2,
        #                              self.map_x, self.map_y, self.background)
        # arcade.draw_rectangle_outline(0, 0, self.map_x, self.map_y, arcade.color.BLACK)


        if self.start_menu:
            # self.pause = True
            arcade.draw_rectangle_filled(self.view_left + self.width / 2, self.view_bottom + self.height / 2, 350, 300, (255, 255, 255, 180))
            arcade.draw_text(f"SPILLNAVN", (self.view_left + self.width / 2 - 100), (self.view_bottom + self.height / 2 - 20), arcade.color.BLACK, 40)
            arcade.draw_text(f"Press enter to start", (self.view_left + self.width / 2 - 100), (self.view_bottom + self.height / 2 - 50), arcade.color.BLACK, 20)
            arcade.draw_text(f"Hvor mange spillere?", (self.view_left + self.width / 2 - 100), (self.view_bottom + self.height / 2 - 70), arcade.color.BLACK, 20)
            arcade.draw_text(f"1", (self.view_left + self.width / 2 - 60), (self.view_bottom + self.height / 2 + 30), arcade.color.BLACK, 40)
            arcade.draw_text(f"2", (self.view_left + self.width / 2 + 40), (self.view_bottom + self.height / 2 + 30), arcade.color.BLACK, 40)
            if self.player_number == 1:
                arcade.draw_rectangle_outline(self.view_left + self.width / 2 - 50, self.view_bottom + self.height / 2 + 50, 50, 50, arcade.color.RED)
            if self.player_number == 2:
                arcade.draw_rectangle_outline(self.view_left + self.width / 2 + 50, self.view_bottom + self.height / 2 + 50, 50, 50, arcade.color.RED)
            arcade.draw_text(f"Difficulty:", (self.view_left + self.width / 2 - 100), (self.view_bottom + self.height / 2 - 90), arcade.color.BLACK, 20)
            if self.difficulty == 0:
                arcade.draw_text(f"Easy", (self.view_left + self.width/2 - 170), (self.view_bottom + self.height/2 - 120), arcade.color.RED, 25)
            else:
                arcade.draw_text(f"Easy", (self.view_left + self.width / 2 - 170), (self.view_bottom + self.height / 2 - 120), arcade.color.BLACK, 20)
            if self.difficulty == 1:
                arcade.draw_text(f"Medium", (self.view_left + self.width / 2 - 120), (self.view_bottom + self.height / 2 - 120), arcade.color.RED, 25)
            else:
                arcade.draw_text(f"Medium", (self.view_left + self.width / 2 - 110), (self.view_bottom + self.height / 2 - 120), arcade.color.BLACK, 20)
            if self.difficulty == 2:
                arcade.draw_text(f"Hard", (self.view_left + self.width / 2 - 20), (self.view_bottom + self.height / 2 - 120), arcade.color.RED, 25)
            else:
                arcade.draw_text(f"Hard", (self.view_left + self.width / 2 - 10), (self.view_bottom + self.height / 2 - 120), arcade.color.BLACK, 20)
            if self.difficulty == 3:
                arcade.draw_text(f"Impossible", (self.view_left + self.width / 2 + 40), (self.view_bottom + self.height / 2 - 120), arcade.color.RED, 25)
            else:
                arcade.draw_text(f"Impossible", (self.view_left + self.width / 2 + 50), (self.view_bottom + self.height / 2 - 120), arcade.color.BLACK, 20)

        if self.sprite2_make:
            # self.sprite2 = arcade.Sprite("Sprite/Høne.png", center_x=100, center_y=100, scale=0.1)
            self.sprite_list.append(self.sprite2)
            self.sprite2_make = False
        if self.player_number == 1:
            self.sprite1_show = True
        if self.player_number == 2:
            self.sprite1_show = True
            self.sprite2_show = True
            # self.player_number = 0
        if self.sprite1_make:
            self.setup()
            self.player_list.update()
            self.player_list.update_animation()
            self.sprite1_make = False

        if self.start_menu == True or self.game_over == True:
            arcade.draw_rectangle_filled(self.view_left + (5 * self.width / 6), self.view_bottom + self.height / 2, self.width/4, self.height -50, (255, 255, 255, 180))
            arcade.draw_text(f"ScoreBoard:", (self.view_left + (4 * self.width / 5)), (self.view_bottom + (4 * self.height / 5)) + 30, arcade.color.BLACK, 20)
            for i in range(0, 5):
                arcade.draw_text(f"{i+1}: {self.data[self.difficulty + self.scoreboard_playernum, -(i+1)]}", (self.view_left + (4 * self.width / 5)), (self.view_bottom + (4 * self.height / 5)) - i * 30, arcade.color.BLACK, 20)

        """
        Tegner Fiender
        """
        if self.test2:
            if self.difficulty == 3:
                enemy_number = self.round_counter + 10
            elif self.difficulty == 2:
                enemy_number = self.round_counter + 5
            elif self.difficulty == 1:
                enemy_number = self.round_counter + 3
            else:
                enemy_number = self.round_counter
            for i in range(0, enemy_number):
                self.sprite5 = arcade.Sprite("Sprite/Panda.png", center_x=100, center_y=100, scale=0.13)
                self.enemy_position = random.randint(0, 3)

                if self.enemy_position == 0:
                    self.sprite5.set_position((self.map_x / 2) + (50 * i), random.randint(-850, 850))
                if self.enemy_position == 1:
                    self.sprite5.set_position(-1 * (self.map_x / 2) - (50 * i), random.randint(-850, 850))
                if self.enemy_position == 2:
                    self.sprite5.set_position(random.randint(-1500, 1500), (self.map_y / 2) + (50 * i))
                if self.enemy_position == 3:
                    self.sprite5.set_position(random.randint(-1500, 1500), -1 * (self.map_y / 2) - (50 * i))
                #print(self.sprite5._get_center_x(), self.sprite5._get_center_y())

                self.enemy2_list.append(self.sprite5)
                self.enemy_health.append(self.round_counter + 1)
                self.enemy_color_list.append(0)
                #self.enemy_position += 1
                #if self.enemy_position == 4:
                #    self.enemy_position = 0
            #self.enemy_position = 0
            print("Antall fiender:", len(self.enemy_health))
            print("Faktisk antall fiender:", len(self.enemy2_list))
            print("Liv per fiende:", self.enemy_health[0])
            self.test2 = False

        """
        Tegner tekst shape2 = arcade.create_rectangle_filled(self.view_left + self.width - self.width/8, self.view_bottom + self.height/8, self.width/10, self.height/10, (100, 76, 160, 180))
        """
        if self.pause == False or self.pause_menu == True:
            self.shape_list.draw()
            arcade.draw_text(f"{self.ammo}/{self.ammo_reserve}", self.view_left + self.width - self.width/4, self.view_bottom + self.height/11, arcade.color.DARK_RED, self.height/13)
            arcade.draw_text(f"Level: {self.round_counter}", (self.view_left + 50), (self.view_bottom + self.height/1.06), arcade.color.DARK_RED, (self.height/11)/2)
            arcade.draw_text(f"{self.penger}", self.view_left + self.width/2 - self.width/14, (self.view_bottom + self.height/1.06 - (self.height/11)/2), arcade.color.DARK_RED, (self.height/11))
            if self.difficulty != 3:
                if self.minutes == 0:
                    arcade.draw_text(f"Tid: {int(self.seconds//1)}s", self.view_left + 50, (self.view_bottom + self.height/1.06 - (self.height/11)/2), arcade.color.DARK_RED, (self.height/11)/2)
                else:
                    arcade.draw_text(f"Tid: {self.minutes}m:{int(self.seconds//1)}s", self.view_left + 50, (self.view_bottom + self.height/1.06 - (self.height/11)/2), arcade.color.DARK_RED, (self.height/11)/2)
                if self.sprite5_follow:
                    arcade.draw_text(f"{len(self.enemy2_list)}", self.view_left + self.width - self.width/5, (self.view_bottom + self.height/1.06), arcade.color.DARK_RED, (self.height/11)/2)
                else:
                    arcade.draw_text(f"0", self.view_left + self.width - self.width/5, (self.view_bottom + self.height/1.06), arcade.color.DARK_RED, (self.height/11)/2)
                #arcade.draw_text(f"Ammo: {self.ammo}", self.view_left + self.width - self.width/5, (self.view_bottom + self.height/1.06 - (self.height/11)/2), arcade.color.DARK_RED, (self.height/11)/2)
            arcade.draw_text(f"Posisjon: {self.player1_x//1}, {self.player1_y//1}", self.view_left + 200, (self.view_bottom + self.height - 20), arcade.color.DARK_RED, 20)
            if self.round_counter < 40:
                arcade.draw_text(f"{self.level_comment[self.round_counter//5]}", self.view_left + 500, (self.view_bottom + self.height - 20), arcade.color.DARK_RED, 20)
            else:
                arcade.draw_text(f"{self.level_comment[8]}", self.view_left + self.width/2 + 200, (self.view_bottom + self.height - 20), arcade.color.DARK_RED, 20)


            if self.sprite1_delete == False:
                arcade.draw_xywh_rectangle_filled(self.player1_x - 50, self.player1_y + 60, self.poeng1, 10, arcade.color.RED)
                arcade.draw_xywh_rectangle_outline(self.player1_x - 51, self.player1_y + 59, 101, 11, arcade.color.BLACK, border_width=2)
            if self.sprite2_delete == False:
                arcade.draw_xywh_rectangle_filled(self.player2_x - 50, self.player2_y + 60, self.poeng2, 10, arcade.color.RED)
                arcade.draw_xywh_rectangle_outline(self.player2_x - 51, self.player2_y + 59, 101, 11, arcade.color.BLACK, border_width=2)
        """
        Tegner skuddene og legger dem til i en liste gitt av retning
        """
        if self.ammo > 0:
            self.bullet_fire = True
            self.bullet_x = self.player1_x
            self.bullet_y = self.player1_y


            if self.bullet_x_make:
                self.fire0 = True
                if self.test3:
                    arcade.sound.play_sound(self.gun_sound)
                    self.bullet = arcade.Sprite("Sprite/Laser.png", center_x=self.bullet_x, center_y=self.bullet_y, scale=1)
                    a = math.radians(random.randint(self.bullet_spread_min, self.bullet_spread_max))
                    b = math.tan(a)
                    self.bullet.angle = math.degrees(a)
                    self.bullet_x_degrees_list.append(b)
                    self.bullet_list_x.append(self.bullet)
                    self.ammo -= 1
                    self.test3 = False
                for i in range(0, len(self.bullet_list_x)):
                    if arcade.get_distance_between_sprites(self.sprite1, self.bullet_list_x[-1]) > 50:
                        arcade.sound.play_sound(self.gun_sound)
                        self.bullet = arcade.Sprite("Sprite/Laser.png", center_x=self.bullet_x, center_y=self.bullet_y,
                                                    scale=1)
                        a = math.radians(random.randint(self.bullet_spread_min, self.bullet_spread_max))
                        b = math.tan(a)
                        self.bullet.angle = math.degrees(a)
                        self.bullet_x_degrees_list.append(b)
                        self.bullet_list_x.append(self.bullet)
                        self.ammo -= 1

            if self.bullet_xn_make:
                self.fire1 = True
                if self.test3_xn:
                    self.bullet = arcade.Sprite("Sprite/Laser.png", center_x=self.bullet_x, center_y=self.bullet_y, scale=1)
                    arcade.sound.play_sound(self.gun_sound)
                    a = math.radians(random.randint(self.bullet_spread_min, self.bullet_spread_max))
                    b = math.tan(a)
                    self.bullet.angle = math.degrees(a) + 180
                    self.bullet_xn_degrees_list.append(b)
                    self.bullet_list_xn.append(self.bullet)
                    self.ammo -= 1
                    self.test3_xn = False
                for i in range(0, len(self.bullet_list_xn)):
                    if arcade.get_distance_between_sprites(self.sprite1, self.bullet_list_xn[-1]) > 50:
                        # print("i:", i)
                        self.bullet = arcade.Sprite("Sprite/Laser.png", center_x=self.bullet_x, center_y=self.bullet_y,
                                                    scale=1)
                        a = math.radians(random.randint(self.bullet_spread_min, self.bullet_spread_max))
                        b = math.tan(a)
                        self.bullet.angle = math.degrees(a) + 180
                        self.bullet_xn_degrees_list.append(b)
                        arcade.sound.play_sound(self.gun_sound)
                        self.bullet_list_xn.append(self.bullet)
                        self.ammo -= 1

            if self.bullet_y_make:
                self.fire2 = True
                if self.test3_y:
                    self.bullet = arcade.Sprite("Sprite/Laser.png", center_x=self.bullet_x, center_y=self.bullet_y, scale=1)
                    arcade.sound.play_sound(self.gun_sound)
                    a = math.radians(random.randint(self.bullet_spread_min, self.bullet_spread_max))
                    b = math.tan(a)
                    self.bullet.angle = math.degrees(a) + 90
                    self.bullet_y_degrees_list.append(b)
                    self.bullet_list_y.append(self.bullet)
                    self.ammo -= 1
                    self.test3_y = False
                for i in range(0, len(self.bullet_list_y)):
                    if arcade.get_distance_between_sprites(self.sprite1, self.bullet_list_y[-1]) > 50:
                        # print("i:", i)
                        self.bullet = arcade.Sprite("Sprite/Laser.png", center_x=self.bullet_x, center_y=self.bullet_y,
                                                    scale=1)
                        arcade.sound.play_sound(self.gun_sound)
                        a = math.radians(random.randint(self.bullet_spread_min, self.bullet_spread_max))
                        b = math.tan(a)
                        self.bullet.angle = math.degrees(a) + 90
                        self.bullet_y_degrees_list.append(b)
                        self.bullet_list_y.append(self.bullet)
                        self.ammo -= 1

            if self.bullet_yn_make:
                self.fire3 = True
                if self.test3_yn:
                    self.bullet = arcade.Sprite("Sprite/Laser.png", center_x=self.bullet_x, center_y=self.bullet_y, scale=1)
                    arcade.sound.play_sound(self.gun_sound)
                    a = math.radians(random.randint(self.bullet_spread_min, self.bullet_spread_max))
                    b = math.tan(a)
                    self.bullet.angle = math.degrees(a) + 270
                    self.bullet_yn_degrees_list.append(b)
                    self.bullet_list_yn.append(self.bullet)
                    self.ammo -= 1
                    self.test3_yn = False
                for i in range(0, len(self.bullet_list_yn)):
                    if arcade.get_distance_between_sprites(self.sprite1, self.bullet_list_yn[-1]) > 50:
                        # print("i:", i)
                        self.bullet = arcade.Sprite("Sprite/Laser.png", center_x=self.bullet_x, center_y=self.bullet_y,
                                                    scale=1)
                        arcade.sound.play_sound(self.gun_sound)
                        a = math.radians(random.randint(self.bullet_spread_min, self.bullet_spread_max))
                        b = math.tan(a)
                        self.bullet.angle = math.degrees(a) + 270
                        self.bullet_yn_degrees_list.append(b)
                        self.bullet_list_yn.append(self.bullet)
                        self.ammo -= 1

            if self.mouse_bullet:
                self.bullet_01_fire = True
                # if self.degrees_make:
                self.start_x = self.sprite1._get_center_x()
                self.start_y = self.sprite1._get_center_y()

                self.difference_x = (self.target_x + self.view_left) - self.start_x
                self.difference_y = (self.target_y + self.view_bottom) - self.start_y

                self.degrees_rad = math.atan2(self.difference_y, self.difference_x)
                self.degrees_deg = math.degrees(self.degrees_rad)
                # print("Grader:", self.degrees_deg)
                # self.degrees_make = False
                if self.test6:
                    self.bullet_01 = arcade.Sprite("Sprite/Laser.png", center_x=self.start_x, center_y=self.start_y, scale=1)
                    self.bullet_01.angle = self.degrees_deg
                    arcade.sound.play_sound(self.gun_sound)
                    self.bullet_01_list.append(self.bullet_01)
                    self.degrees_list.append(self.degrees_rad)
                    self.ammo -= 1
                    self.test6 = False
                for i in range(0, len(self.bullet_01_list)):
                    # print("i:", i)
                    self.bullet_01 = arcade.Sprite("Sprite/Laser.png", center_x=self.start_x, center_y=self.start_y, scale=1)
                    self.bullet_01.angle = self.degrees_deg
                    if arcade.get_distance_between_sprites(self.bullet_01, self.bullet_01_list[-1]) > 70:
                        arcade.sound.play_sound(self.gun_sound)
                        self.bullet_01_list.append(self.bullet_01)
                        self.degrees_list.append(self.degrees_rad)
                        self.ammo -= 1

        """
        Tegner listene
        """

        self.ammo_texture_list.draw()
        self.health_texture_list.draw()

        if self.sprite5_follow:
            self.enemy2_list.draw()

        self.bullet_list_x.draw()
        self.bullet_list_xn.draw()
        self.bullet_list_y.draw()
        self.bullet_list_yn.draw()
        self.bullet_01_list.draw()
        if self.sprite1_show:
            self.player_list.draw()
        if self.sprite2_show:
            self.sprite_list.draw()

        if self.pause_menu:
            arcade.draw_xywh_rectangle_filled(self.view_left + self.width / 3, self.view_bottom + self.height / 3, self.width / 3, self.height / 3, (255, 255, 255, 180))
            arcade.draw_text(f"PAUSE", (self.view_left + self.width / 2 - 70), (self.view_bottom + self.height / 2 - 20), arcade.color.BLACK, 40)
            arcade.draw_text(f"Press escape to continue", (self.view_left + self.width / 2 - 120), (self.view_bottom + self.height / 2 - 50), arcade.color.BLACK, 20)
            arcade.draw_text(f"Press enter to restart", (self.view_left + self.width / 2 - 100), (self.view_bottom + self.height / 2 - 70), arcade.color.BLACK, 20)
            arcade.draw_rectangle_filled(self.view_left + (5 * self.width) / 6, self.view_bottom + self.height / 2, self.width / 4, self.height - 50, (255, 255, 255, 180))
            arcade.draw_text(f"Player 1", (self.view_left + self.width - 200), (self.view_bottom + self.height - 70), arcade.color.BLACK, 20)
            arcade.draw_text(f"Move: AWSD", (self.view_left + self.width - 220), (self.view_bottom + self.height - 100), arcade.color.BLACK, 20)
            arcade.draw_text(f"Shoot: Lshift or Mouse click", (self.view_left + self.width - 330), (self.view_bottom + self.height - 130), arcade.color.BLACK, 20)
            arcade.draw_text(f"Alternative shooting: K", (self.view_left + self.width - 280), (self.view_bottom + self.height - 160), arcade.color.BLACK, 20)
            arcade.draw_text(f" Player 2 \n Move: piler \n Punch: G \n Start wave: F", (self.view_left + self.width - 280), (self.view_bottom + self.height - 260), arcade.color.BLACK, 20)

        if self.game_over:
            self.pause = True
            arcade.draw_rectangle_filled(self.view_left + self.width / 2, self.view_bottom + self.height / 2, 300, 200, (255, 255, 255, 180))
            arcade.draw_text(f"HAHAHAHAHA", (self.view_left + self.width / 2 - 100), (self.view_bottom + self.height / 2 + 20), arcade.color.BLACK, 40)
            arcade.draw_text(f"GAME OVER", (self.view_left + self.width / 2 - 100), (self.view_bottom + self.height / 2 - 20), arcade.color.BLACK, 40)
            arcade.draw_text(f"Press enter to restart", (self.view_left + self.width / 2 - 100), (self.view_bottom + self.height / 2 - 50), arcade.color.BLACK, 20)
            arcade.draw_text(f"Score: {self.penger}", (self.view_left + self.width / 2 - 100), (self.view_bottom + self.height / 2 - 70), arcade.color.BLACK, 20)
            arcade.draw_text(f"Round: {self.round_counter}", (self.view_left + self.width / 2 - 100), (self.view_bottom + self.height / 2 - 90), arcade.color.BLACK, 20)

    def on_update(self, delta_time):
        # print(delta_time)
        self.player_list.update()
        self.player_list.update_animation()

        if self.start_menu:
            self.pause = True

        if self.pause:
            self.right1 = False
            self.left1 = False
            self.up1 = False
            self.down1 = False

            self.sprite1.set_position(self.player1_x, self.player1_y)

        if self.pause == False:
            # print(self.sprite1.texture_list)
            self.pause_menu = False

            self.seconds = self.total_time % 60

            if self.seconds // 1 == 59:
                self.test4 = True
            if self.seconds // 1 == 0:
                # print("2")
                if self.test4:
                    self.minutes += 1
                    self.test4 = False

            """
            Beveger og avgrenser sprite1 og sprite2
            """

            if self.right1:
                self.sprite1.change_x = MOVEMENT_SPEED
                self.player1_x += self.player1_speed * delta_time
            if self.left1:
                self.sprite1.change_x = -MOVEMENT_SPEED
                self.player1_x -= self.player1_speed * delta_time
            if self.up1:
                self.sprite1.change_y = MOVEMENT_SPEED
                self.player1_y += self.player1_speed * delta_time
            if self.down1:
                self.sprite1.change_y = -MOVEMENT_SPEED
                self.player1_y -= self.player1_speed * delta_time

            self.sprite1.set_position(self.player1_x, self.player1_y)

            if self.player1_y > self.map_y / 2:
                self.player1_y = self.map_y / 2
            if self.player1_x < -1 * self.map_x / 2:
                self.player1_x = -1 * self.map_x / 2
            if self.player1_x > self.map_x / 2:
                self.player1_x = self.map_x / 2
            if self.player1_y < -1 * self.map_y / 2:
                self.player1_y = -1 * self.map_y / 2

            if self.sprite1.state == FACE_LEFT:
                AA = self.target_x - self.sprite1._get_center_x()
                #print(AA)
                if AA > 0:
                    if self.bullet_01_fire:
                        #print("x1")
                        self.sprite1.state = FACE_RIGHT
                        #change_direction = True
                        #texture_list = self.sprite1.walk_right_textures

            if self.right2:
                self.player2_x += self.player2_speed * delta_time
            if self.left2:
                self.player2_x -= self.player2_speed * delta_time
            if self.up2:
                self.player2_y += self.player2_speed * delta_time
            if self.down2:
                self.player2_y -= self.player2_speed * delta_time

            self.sprite2.set_position(self.player2_x, self.player2_y)

            if self.player2_y > self.map_y / 2:
                self.player2_y = self.map_y / 2
            if self.player2_x < -1 * self.map_x / 2:
                self.player2_x = -1 * self.map_x / 2
            if self.player2_x > self.map_x / 2:
                self.player2_x = self.map_x / 2
            if self.player2_y < -1 * self.map_y / 2:
                self.player2_y = -1 * self.map_y / 2

            """
            if self.sprite1_delete:
                if self.background_num == 0:
                    if self.player2_x > (self.width+20):
                        self.player2_x = 50
                        self.sprite2.set_position(self.player2_x, self.player2_y)
                        self.background_num = 1
                elif self.background_num == 1:
                    if self.player2_x < -20:
                        self.player2_x = self.width - 50
                        self.sprite2.set_position(self.player2_x, self.player2_y)
                        self.background_num = 0
            if self.sprite2_delete:
                if self.background_num == 0:
                    if self.player1_x > (self.width+20):
                        self.player1_x = 50
                        self.sprite1.set_position(self.player1_x, self.player1_y)
                        self.background_num = 1
                elif self.background_num == 1:
                    if self.player1_x < -20:
                        self.player1_x = self.width - 50
                        self.sprite1.set_position(self.player1_x, self.player1_y)
                        self.background_num = 0
            else:
                if self.background_num == 0:
                    if self.player1_x > (self.width+20):
                        if self.player2_x > (self.width+20):
                            self.player1_x = 50
                            self.player2_x = 50
                            self.sprite1.set_position(self.player1_x, self.player1_y)
                            self.sprite2.set_position(self.player2_x, self.player2_y)
                            self.background_num = 1
                if self.background_num == 1:
                    if self.player1_x < -20:
                        if self.player2_x < -20:
                            self.player1_x = self.width-50
                            self.player2_x = self.width-50
                            self.sprite1.set_position(self.player1_x, self.player1_y)
                            self.sprite2.set_position(self.player2_x, self.player2_y)
                            self.background_num = 0
            """

            """
            Beveger fiender og fjerner dem etter hver runde
            """

            if self.sprite5_follow:
                #print("1a")
                self.total_time += delta_time

                for i in range(0, len(self.enemy2_list)):

                    self.endring2_x = self.sprite2._get_center_x() - self.enemy2_list[i]._get_center_x()
                    self.endring2_y = self.sprite2._get_center_y() - self.enemy2_list[i]._get_center_y()

                    self.endring1_x = self.sprite1._get_center_x() - self.enemy2_list[i]._get_center_x()
                    self.endring1_y = self.sprite1._get_center_y() - self.enemy2_list[i]._get_center_y()

                    try:
                        if self.difficulty == 3:
                            d = sqrt(((self.round_counter * 2) + 75) / (self.endring1_x ** 2 + self.endring1_y ** 2))
                        elif self.difficulty == 2:
                            d = sqrt(((self.round_counter * 2) + 50) / (self.endring1_x ** 2 + self.endring1_y ** 2))
                        elif self.difficulty == 1:
                            d = sqrt(((self.round_counter * 2) + 35) / (self.endring1_x ** 2 + self.endring1_y ** 2))
                        else:
                            d = sqrt(((self.round_counter * 2) + 15) / (self.endring1_x ** 2 + self.endring1_y ** 2))
                    except:
                        d = 0
                    try:
                        d2 = sqrt(((self.round_counter * 2) + 15) / (self.endring2_x ** 2 + self.endring2_y ** 2))
                    except:
                        d2 = 0

                    k = 0
                    l = 0
                    u = 1

                    if self.sprite1_delete:
                        # print("0")
                        # if arcade.get_distance_between_sprites(self.sprite2, self.enemy2_list[i]) > 50:
                        for o in range(0, len(self.enemy2_list)):
                            if o != i:
                                if arcade.check_for_collision(self.enemy2_list[i], self.enemy2_list[o]):
                                    k += 1
                                    j = random.randint(0, 1000)
                                    if arcade.get_distance_between_sprites(self.enemy2_list[i],
                                                                           self.sprite2) > arcade.get_distance_between_sprites(
                                        self.enemy2_list[o], self.sprite2):
                                        l += 1
                                    if j > 800:
                                        if arcade.get_distance_between_sprites(self.sprite2, self.enemy2_list[i]) < 20:
                                            u = -10
                                    if j > 980:
                                        if arcade.get_distance_between_sprites(self.enemy2_list[i], self.enemy2_list[o]) < 20:
                                            u = 10
                        if k > 0:
                            if l > 0:
                                self.fart_x = self.endring2_x * d2 * self.crash_fart * u
                                self.fart_y = self.endring2_y * d2 * self.crash_fart * u
                            else:
                                self.fart_x = self.endring2_x * d2
                                self.fart_y = self.endring2_y * d2
                        else:
                            self.fart_x = self.endring2_x * d2
                            self.fart_y = self.endring2_y * d2
                    elif self.sprite2_delete:
                        # print("11")
                        for o in range(0, len(self.enemy2_list)):
                            if o != i:
                                if arcade.check_for_collision(self.enemy2_list[i], self.enemy2_list[o]):
                                    k += 1
                                    j = random.randint(0, 1000)
                                    if arcade.get_distance_between_sprites(self.enemy2_list[i],
                                                                           self.sprite1) > arcade.get_distance_between_sprites(
                                        self.enemy2_list[o], self.sprite1):
                                        l += 1
                                    if j > 800:
                                        if arcade.get_distance_between_sprites(self.sprite1, self.enemy2_list[i]) < 20:
                                            u = -10
                                    if j > 990:
                                        if arcade.get_distance_between_sprites(self.enemy2_list[i], self.enemy2_list[o]):
                                            u = 10
                        if k > 0:
                            if l > 0:
                                self.fart_x = self.endring1_x * d * self.crash_fart * u
                                self.fart_y = self.endring1_y * d * self.crash_fart * u
                            else:
                                self.fart_x = self.endring1_x * d
                                self.fart_y = self.endring1_y * d
                        else:
                            self.fart_x = self.endring1_x * d
                            self.fart_y = self.endring1_y * d
                    else:
                        if arcade.get_distance_between_sprites(self.sprite1, self.enemy2_list[i]) < arcade.get_distance_between_sprites(self.sprite2, self.enemy2_list[i]):
                            # print("2")
                            for o in range(0, len(self.enemy2_list)):
                                if o != i:
                                    if arcade.check_for_collision(self.enemy2_list[i], self.enemy2_list[o]):
                                        k += 1
                                        j = random.randint(0, 1000)
                                        if arcade.get_distance_between_sprites(self.enemy2_list[i],
                                                                               self.sprite1) > arcade.get_distance_between_sprites(
                                            self.enemy2_list[o], self.sprite1):
                                            l += 1
                                        if j > 800:
                                            if arcade.get_distance_between_sprites(self.sprite1, self.enemy2_list[i]) < 20:
                                                u = -10
                                        if j > 990:
                                            if arcade.get_distance_between_sprites(self.enemy2_list[i], self.enemy2_list[o]):
                                                u = 10
                            if k > 0:
                                if l > 0:
                                    self.fart_x = self.endring1_x * d * self.crash_fart * u
                                    self.fart_y = self.endring1_y * d * self.crash_fart * u
                                else:
                                    self.fart_x = self.endring1_x * d
                                    self.fart_y = self.endring1_y * d
                            else:
                                self.fart_x = self.endring1_x * d
                                self.fart_y = self.endring1_y * d
                        elif arcade.get_distance_between_sprites(self.sprite2, self.enemy2_list[i]) < arcade.get_distance_between_sprites(self.sprite1, self.enemy2_list[i]):
                            # print("3")
                            for o in range(0, len(self.enemy2_list)):
                                if o != i:
                                    if arcade.check_for_collision(self.enemy2_list[i], self.enemy2_list[o]):
                                        k += 1
                                        j = random.randint(0, 1000)
                                        if arcade.get_distance_between_sprites(self.enemy2_list[i], self.sprite2) > arcade.get_distance_between_sprites(self.enemy2_list[o], self.sprite2):
                                            l += 1
                                        if j > 800:
                                            if arcade.get_distance_between_sprites(self.sprite2, self.enemy2_list[i]) < 20:
                                                u = -10
                                        if j > 990:
                                            if arcade.get_distance_between_sprites(self.enemy2_list[i], self.enemy2_list[o]):
                                                u = 10
                            if k > 0:
                                if l > 0:
                                    self.fart_x = self.endring2_x * d2 * self.crash_fart * u
                                    self.fart_y = self.endring2_y * d2 * self.crash_fart * u
                                else:
                                    self.fart_x = self.endring2_x * d2
                                    self.fart_y = self.endring2_y * d2
                            else:
                                self.fart_x = self.endring2_x * d2
                                self.fart_y = self.endring2_y * d2

                    self.sprite5_x = self.enemy2_list[i]._get_center_x() + self.fart_x
                    self.sprite5_y = self.enemy2_list[i]._get_center_y() + self.fart_y

                    self.enemy2_list[i].set_position(self.sprite5_x, self.sprite5_y)
                if self.test2 == False:
                    if len(self.enemy2_list) == 0:
                        self.sprite5_x = 800
                        self.sprite5_y = 100
                        # self.round_counter += 1
                        while self.enemy2_list:
                            self.enemy2_list.pop()
                        self.enemy_list = None
                        self.enemy_list = arcade.SpriteList()
                        # self.total_time = 0.0
                        self.sprite5_follow = False
                        #self.test2 = True

            if self.sprite5_follow:
                for i in range(0, len(self.enemy2_list)):
                    if arcade.get_distance_between_sprites(self.sprite2, self.enemy2_list[i]) < 70:
                        self.poeng2 -= 1
                    if arcade.get_distance_between_sprites(self.sprite1, self.enemy2_list[i]) < 120:
                        #print(self.seconds)
                        if self.difficulty == 0 or self.difficulty == 1:
                            self.poeng1 -= 1
                        elif self.difficulty == 2:
                            self.poeng1 -= 2
                        else:
                            self.poeng1 -= 10

            if self.sprite2_delete == False:
                if self.poeng2 <= 0:
                    self.sprite2.remove_from_sprite_lists()
                    self.poeng2 = 0
                    self.sprite2_delete = True
            if self.sprite1_delete == False:
                if self.poeng1 <= 0:
                    print(len(self.player_list))
                    self.player_list.pop()
                    self.poeng1 = 0
                    self.sprite1_delete = True

            """
            Beveger og fjerner bullets
            """

            if self.bullet_fire:
                #print("e")
                if self.fire0:
                    for i in range(0, len(self.bullet_list_x)):
                        self.bullet_x = self.bullet_list_x[i]._get_center_x() + 20
                        self.bullet_y = self.bullet_list_x[i]._get_center_y() + (20*self.bullet_x_degrees_list[i])
                        self.bullet_list_x[i].set_position(self.bullet_x, self.bullet_y)

                if self.fire1:
                    for i in range(0, len(self.bullet_list_xn)):
                        self.bullet_x = self.bullet_list_xn[i]._get_center_x() - 20
                        self.bullet_y = self.bullet_list_xn[i]._get_center_y() + (-20*self.bullet_xn_degrees_list[i])
                        self.bullet_list_xn[i].set_position(self.bullet_x, self.bullet_y)

                if self.fire2:

                    for i in range(0, len(self.bullet_list_y)):
                        self.bullet_y = self.bullet_list_y[i]._get_center_y() + 20
                        self.bullet_x = self.bullet_list_y[i]._get_center_x() + (-20*self.bullet_y_degrees_list[i])
                        self.bullet_list_y[i].set_position(self.bullet_x, self.bullet_y)

                if self.fire3:

                    for i in range(0, len(self.bullet_list_yn)):
                        self.bullet_y = self.bullet_list_yn[i]._get_center_y() - 20
                        self.bullet_x = self.bullet_list_yn[i]._get_center_x() + (20*self.bullet_yn_degrees_list[i])
                        self.bullet_list_yn[i].set_position(self.bullet_x, self.bullet_y)

                for i in range(0, len(self.bullet_list_x)):
                    try:
                        if self.bullet_list_x[i]._get_center_x() > self.map_x / 2:
                            self.bullet_x_degrees_list.pop(i)
                            self.bullet_list_x[i].remove_from_sprite_lists()
                    except:
                        pass
                    if self.sprite5_follow:
                        try:
                            for o in range(0, len(self.enemy2_list)):
                                if arcade.check_for_collision(self.bullet_list_x[i], self.enemy2_list[o]):
                                    self.bullet_x_degrees_list.pop(i)
                                    self.bullet_list_x[i].remove_from_sprite_lists()
                                    self.penger += 1
                                    self.enemy_health[o] -= 1
                                    self.enemy2_list[o].color = (255, 100, 100)
                                    if self.enemy_health[o] <= 0:
                                        self.ammo_pack_list.append(self.enemy2_list[o]._get_center_x())
                                        self.ammo_pack_list.append(self.enemy2_list[o]._get_center_y())
                                        ammo_pack = arcade.Sprite("Sprite/Ammo.png", center_x=self.enemy2_list[o]._get_center_x(), center_y=self.enemy2_list[o]._get_center_y(), scale=0.5)
                                        self.ammo_texture_list.append(ammo_pack)
                                        if self.difficulty == 0 or self.difficulty == 1:
                                            tall = random.randint(0, 1000)
                                            if tall > 900:
                                                health_pack = arcade.Sprite("Sprite/Health.png", center_x=(self.enemy2_list[o]._get_center_x() + (1000-tall)), center_y=self.enemy2_list[o]._get_center_y() + (1000-tall),
                                                                            scale=0.5)
                                                self.health_texture_list.append(health_pack)
                                        self.enemy2_list[o].remove_from_sprite_lists()
                                        self.enemy_health.pop(o)
                                        self.enemy_color_list.pop(o)
                        except:
                            pass
                for i in range(0, len(self.bullet_list_xn)):
                    try:
                        if self.bullet_list_xn[i]._get_center_x() < (self.map_x / 2) * -1:
                            self.bullet_xn_degrees_list.pop(i)
                            self.bullet_list_xn[i].remove_from_sprite_lists()
                    except:
                        pass
                    if self.sprite5_follow:
                        try:
                            for o in range(0, len(self.enemy2_list)):
                                if arcade.check_for_collision(self.bullet_list_xn[i], self.enemy2_list[o]):
                                    self.bullet_xn_degrees_list.pop(i)
                                    self.bullet_list_xn[i].remove_from_sprite_lists()
                                    self.penger += 1
                                    self.enemy_health[o] -= 1
                                    self.enemy2_list[o].color = (255, 100, 100)
                                    if self.enemy_health[o] <= 0:
                                        self.ammo_pack_list.append(self.enemy2_list[o]._get_center_x())
                                        self.ammo_pack_list.append(self.enemy2_list[o]._get_center_y())
                                        ammo_pack = arcade.Sprite("Sprite/Ammo.png", center_x=self.enemy2_list[o]._get_center_x(), center_y=self.enemy2_list[o]._get_center_y(), scale=0.5)
                                        self.ammo_texture_list.append(ammo_pack)
                                        if self.difficulty == 0 or self.difficulty == 1:
                                            tall = random.randint(0, 1000)
                                            if tall > 900:
                                                health_pack = arcade.Sprite("Sprite/Health.png", center_x=(self.enemy2_list[o]._get_center_x() + (1000-tall)), center_y=self.enemy2_list[o]._get_center_y() + (1000-tall),
                                                                            scale=0.5)
                                                self.health_texture_list.append(health_pack)
                                        self.enemy2_list[o].remove_from_sprite_lists()
                                        self.enemy_health.pop(o)
                                        self.enemy_color_list.pop(o)
                        except:
                            pass
                for i in range(0, len(self.bullet_list_y)):
                    try:
                        if self.bullet_list_y[i]._get_center_y() > self.map_y / 2:
                            self.bullet_y_degrees_list.pop(i)
                            self.bullet_list_y[i].remove_from_sprite_lists()
                    except:
                        pass
                    if self.sprite5_follow:
                        try:
                            for o in range(0, len(self.enemy2_list)):
                                if arcade.check_for_collision(self.bullet_list_y[i], self.enemy2_list[o]):
                                    self.bullet_y_degrees_list.pop(i)
                                    self.bullet_list_y[i].remove_from_sprite_lists()
                                    self.penger += 1
                                    self.enemy_health[o] -= 1
                                    self.enemy2_list[o].color = (255, 100, 100)
                                    if self.enemy_health[o] <= 0:
                                        self.ammo_pack_list.append(self.enemy2_list[o]._get_center_x())
                                        self.ammo_pack_list.append(self.enemy2_list[o]._get_center_y())
                                        ammo_pack = arcade.Sprite("Sprite/Ammo.png", center_x=self.enemy2_list[o]._get_center_x(), center_y=self.enemy2_list[o]._get_center_y(), scale=0.5)
                                        self.ammo_texture_list.append(ammo_pack)
                                        if self.difficulty == 0 or self.difficulty == 1:
                                            tall = random.randint(0, 1000)
                                            if tall > 900:
                                                health_pack = arcade.Sprite("Sprite/Health.png", center_x=(self.enemy2_list[o]._get_center_x() + (1000-tall)), center_y=self.enemy2_list[o]._get_center_y() + (1000-tall),
                                                                            scale=0.5)
                                                self.health_texture_list.append(health_pack)
                                        self.enemy2_list[o].remove_from_sprite_lists()
                                        self.enemy_health.pop(o)
                                        self.enemy_color_list.pop(o)
                        except:
                            pass
                for i in range(0, len(self.bullet_list_yn)):
                    try:
                        if self.bullet_list_yn[i]._get_center_y() < (self.map_y / 2) * -1:
                            self.bullet_yn_degrees_list.pop(i)
                            self.bullet_list_yn[i].remove_from_sprite_lists()
                    except:
                        pass
                    if self.sprite5_follow:
                        try:
                            for o in range(0, len(self.enemy2_list)):
                                if arcade.check_for_collision(self.bullet_list_yn[i], self.enemy2_list[o]):
                                    self.bullet_yn_degrees_list.pop(i)
                                    self.bullet_list_yn[i].remove_from_sprite_lists()
                                    self.penger += 1
                                    self.enemy_health[o] -= 1
                                    self.enemy2_list[o].color = (255, 100, 100)
                                    if self.enemy_health[o] <= 0:
                                        self.ammo_pack_list.append(self.enemy2_list[o]._get_center_x())
                                        self.ammo_pack_list.append(self.enemy2_list[o]._get_center_y())
                                        ammo_pack = arcade.Sprite("Sprite/Ammo.png", center_x=self.enemy2_list[o]._get_center_x(), center_y=self.enemy2_list[o]._get_center_y(), scale=0.5)
                                        self.ammo_texture_list.append(ammo_pack)
                                        if self.difficulty == 0 or self.difficulty == 1:
                                            tall = random.randint(0, 1000)
                                            if tall > 900:
                                                health_pack = arcade.Sprite("Sprite/Health.png", center_x=(self.enemy2_list[o]._get_center_x() + (1000-tall)), center_y=self.enemy2_list[o]._get_center_y() + (1000-tall),
                                                                            scale=0.5)
                                                self.health_texture_list.append(health_pack)
                                        self.enemy2_list[o].remove_from_sprite_lists()
                                        self.enemy_health.pop(o)
                                        self.enemy_color_list.pop(o)
                        except:
                            pass

            for i in range(0, len(self.enemy2_list)):
                if self.enemy2_list[i].color == (255, 100, 100):
                    # print(self.enemy_color_list)
                    self.enemy_color_list[i] += 1
                    if self.enemy_color_list[i] == 5:
                        self.enemy2_list[i].color = (255, 255, 255)
                        self.enemy_color_list[i] = 0

                if self.enemy2_list[i].color == (255, 100, 99):
                    # print(self.enemy_color_list)
                    self.enemy_color_list[i] += 1
                    if self.enemy_color_list[i] == 10:
                        try:
                            if self.enemy_health[i] <= 0:
                                self.ammo_pack_list.append(self.enemy2_list[i]._get_center_x())
                                self.ammo_pack_list.append(self.enemy2_list[i]._get_center_y())
                                ammo_pack = arcade.Sprite("Sprite/Ammo.png", center_x=self.enemy2_list[i]._get_center_x(), center_y=self.enemy2_list[i]._get_center_y(), scale=0.5)
                                self.ammo_texture_list.append(ammo_pack)
                                if self.difficulty == 0 or self.difficulty == 1:
                                    tall = random.randint(0, 1000)
                                    if tall > 900:
                                        health_pack = arcade.Sprite("Sprite/Health.png", center_x=(self.enemy2_list[i]._get_center_x() + (1000-tall)), center_y=self.enemy2_list[i]._get_center_y() + (1000-tall), scale=0.5)
                                        self.health_texture_list.append(health_pack)
                                self.enemy2_list[i].remove_from_sprite_lists()
                                self.enemy_health.pop(i)
                                self.enemy_color_list.pop(i)
                                break
                        except:
                            pass
                        try:
                            self.enemy2_list[i].color = (255, 255, 255)
                            self.enemy_color_list[i] = 0
                        except:
                            pass


            if self.sprite2_hit:
                for i in range(0, len(self.enemy2_list)):
                    if arcade.check_for_collision(self.sprite2, self.enemy2_list[i]):
                        avstand_y = self.sprite2._get_center_y() - self.enemy2_list[i]._get_center_y()
                        avstand_x = self.sprite2._get_center_x() - self.enemy2_list[i]._get_center_x()
                        x_add = 0
                        y_add = 0
                        #print(1, self.player2_retning, avstand_x, avstand_y)
                        #print(2, arcade.get_distance_between_sprites(self.sprite2, self.enemy2_list[i]))
                        if avstand_y < -70:
                            if self.player2_retning == 2:
                                x_add = 0
                                y_add = 75
                                self.enemy_health[i] -= 1
                                self.enemy2_list[i].color = (255, 100, 99)
                                #print(3, "Opp")
                        if avstand_x < -70:
                            if self.player2_retning == 0:
                                x_add = 75
                                y_add = 0
                                self.enemy_health[i] -= 1
                                self.enemy2_list[i].color = (255, 100, 99)
                                #print(3, "Høyre")
                            else:
                                pass
                        if avstand_y > 70:
                            if self.player2_retning == 3:
                                x_add = 0
                                y_add = -75
                                self.enemy_health[i] -= 1
                                self.enemy2_list[i].color = (255, 100, 99)
                                #print(3, "Ned")
                        if avstand_x > 70:
                            if self.player2_retning == 1:
                                x_add = -75
                                y_add = 0
                                self.enemy_health[i] -= 1
                                self.enemy2_list[i].color = (255, 100, 99)
                                #print(3, "Venstre")
                        if arcade.get_distance_between_sprites(self.sprite2, self.enemy2_list[i]) < 70:
                            x_add = random.randint(-50, 50)
                            y_add = random.randint(-50, 50)
                            self.enemy_health[i] -= 1
                            self.enemy2_list[i].color = (255, 100, 99)
                            #print(3, "Tilfeldig")

                        self.sprite5_x = self.enemy2_list[i]._get_center_x() + x_add
                        self.sprite5_y = self.enemy2_list[i]._get_center_y() + y_add
                        self.enemy2_list[i].set_position(self.sprite5_x, self.sprite5_y)
                        #print(4, self.sprite2._get_center_x() - self.enemy2_list[i]._get_center_x(), self.sprite2._get_center_y() - self.enemy2_list[i]._get_center_y())
                        #print(5, arcade.get_distance_between_sprites(self.sprite2, self.enemy2_list[i]))


                        self.sprite2_hit = False
                        #print(self.enemy_health)
                        #print(len(self.enemy2_list))
                        break
                self.sprite2_hit = False

            if self.player_number == 2:
                if self.poeng1 <= 0:
                    if self.poeng2 <= 0:
                        arcade.sound.play_sound(self.sad_sound)
                        min_score = self.data[self.difficulty + self.scoreboard_playernum].min()
                        if self.penger > min_score:
                            self.data[self.difficulty + self.scoreboard_playernum, 0] = self.penger
                            self.data[self.difficulty + self.scoreboard_playernum] = np.sort(self.data[self.difficulty + self.scoreboard_playernum])
                            np.savetxt("Data_test.csv", self.data, delimiter=",")
                        self.game_over = True
            elif self.player_number == 1:
                if self.poeng1 <= 0:
                    arcade.sound.play_sound(self.sad_sound)
                    #print(self.data[self.difficulty])
                    min_score = self.data[self.difficulty].min()
                    if self.penger > min_score:
                        self.data[self.difficulty, 0] = self.penger
                        #print(np.sort(self.data))
                        self.data[self.difficulty] = np.sort(self.data[self.difficulty])
                        np.savetxt("Data_test.csv", self.data, delimiter=",")
                        #print(self.data)
                    self.game_over = True

            """
            if self.mouse_bullet:
                self.start_x = self.sprite1._get_center_x()
                self.start_y = self.sprite1._get_center_y()

                self.difference_x = (self.target_x + self.view_left) - self.start_x
                self.difference_y = (self.target_y + self.view_bottom) - self.start_y

                degrees_rad = math.atan2(self.difference_y, self.difference_x)
                degrees_deg = math.degrees(degrees_rad)
                print("Grader:", degrees_deg)
            """
            if self.bullet_01_fire:
                #print(len(self.bullet_01_list))
                for i in range(0, len(self.bullet_01_list)):
                    # print("grader00:",i,  self.degrees_list[i])

                    self.bullet_01_y = self.bullet_01_list[i]._get_center_y() + math.sin(self.degrees_list[i]) * 20
                    self.bullet_01_x = self.bullet_01_list[i]._get_center_x() + math.cos(self.degrees_list[i]) * 20

                    self.bullet_01_list[i].set_position(self.bullet_01_x, self.bullet_01_y)
                for u in range(0, len(self.bullet_01_list)):
                    try:
                        if self.bullet_01_list[u]._get_center_y() < (self.map_y / 2) * -1:
                            self.bullet_01_list[u].remove_from_sprite_lists()
                            self.degrees_list.pop(u)
                        if self.bullet_01_list[u]._get_center_y() > (self.map_y / 2):
                            # print(self.degrees_list)
                            self.bullet_01_list[u].remove_from_sprite_lists()
                            self.degrees_list.pop(u)
                        if self.bullet_01_list[u]._get_center_x() < (self.map_x / 2) * -1:
                            self.bullet_01_list[u].remove_from_sprite_lists()
                            self.degrees_list.pop(u)
                        if self.bullet_01_list[u]._get_center_x() > (self.map_x / 2):
                            self.bullet_01_list[u].remove_from_sprite_lists()
                            self.degrees_list.pop(u)
                    except:
                        pass
                    if self.sprite5_follow:
                        try:
                            for o in range(0, len(self.enemy2_list)):
                                if arcade.check_for_collision(self.bullet_01_list[u], self.enemy2_list[o]):
                                    self.bullet_01_list[u].remove_from_sprite_lists()
                                    self.degrees_list.pop(u)
                                    self.penger += 1
                                    self.enemy_health[o] -= 1
                                    self.enemy2_list[o].color = (255, 100, 100)
                                    if self.enemy_health[o] <= 0:
                                        self.ammo_pack_list.append(self.enemy2_list[o]._get_center_x())
                                        self.ammo_pack_list.append(self.enemy2_list[o]._get_center_y())
                                        ammo_pack = arcade.Sprite("Sprite/Ammo.png", center_x=self.enemy2_list[o]._get_center_x(), center_y=self.enemy2_list[o]._get_center_y(), scale=0.5)
                                        self.ammo_texture_list.append(ammo_pack)
                                        if self.difficulty == 0 or self.difficulty == 1:
                                            tall = random.randint(0, 1000)
                                            if tall > 900:
                                                health_pack = arcade.Sprite("Sprite/Health.png", center_x=(self.enemy2_list[o]._get_center_x() + (1000-tall)), center_y=(self.enemy2_list[o]._get_center_y() + (1000-tall)), scale=0.5)
                                                self.health_texture_list.append(health_pack)
                                        self.enemy2_list[o].remove_from_sprite_lists()
                                        self.enemy_health.pop(o)
                                        self.enemy_color_list.pop(o)
                        except:
                            pass
                if len(self.bullet_01_list) == 0:
                    self.bullet_01_fire = False

            if self.SV == True and self.SH == False and self.SU == False and self.SD == False:
                self.bullet_xn_make = True
                #print(self.test3_xn)
                #self.test3 = True
            if self.SH == True and self.SV == False and self.SU == False and self.SD == False:
                self.bullet_x_make = True
                #self.test3 = Truew
            if self.SU == True and self.SH == False and self.SV == False and self.SD == False:
                self.bullet_y_make = True
                #self.test3 = True
            if self.SD == True and self.SH == False and self.SU == False and self.SV == False:
                self.bullet_yn_make = True
                #self.test3 = True

            for i in range(0, len(self.ammo_pack_list), 2):
                ammo_avstand_x = self.ammo_pack_list[i] - self.sprite1._get_center_x()
                ammo_avstand_y = self.ammo_pack_list[i+1] - self.sprite1._get_center_y()
                ammo_avstand_x_2 = self.ammo_pack_list[i] - self.sprite2._get_center_x()
                ammo_avstand_y_2 = self.ammo_pack_list[i + 1] - self.sprite2._get_center_y()
                if sqrt((ammo_avstand_x**2 + ammo_avstand_y**2)) < 50:
                    self.ammo_texture_list[int(i/2)].remove_from_sprite_lists()
                    self.ammo_pack_list.pop(i+1)
                    self.ammo_pack_list.pop(i)
                    if self.difficulty == 0:
                        if self.ammo_reserve <= (300-self.round_counter*2):
                            self.ammo_reserve += (self.round_counter*2)
                        else:
                            self.ammo_reserve = 300
                    if self.difficulty == 1:
                        if self.ammo_reserve <= (300 - self.round_counter + 5):
                            self.ammo_reserve += (self.round_counter+5)
                        else:
                            self.ammo_reserve = 300
                    if self.difficulty == 2:
                        if self.ammo_reserve <= (300 - self.round_counter + 2):
                            self.ammo_reserve += (self.round_counter+2)
                        else:
                            self.ammo_reserve = 300
                    if self.difficulty == 3:
                        if self.ammo_reserve <= (300 - self.round_counter + 1):
                            self.ammo_reserve += (self.round_counter+1)
                        else:
                            self.ammo_reserve = 300
                    arcade.sound.play_sound(self.reload_sound)
                    break
                if sqrt((ammo_avstand_x_2**2 + ammo_avstand_y_2**2)) < 50:
                    self.ammo_texture_list[int(i/2)].remove_from_sprite_lists()
                    self.ammo_pack_list.pop(i+1)
                    self.ammo_pack_list.pop(i)
                    if self.difficulty == 0:
                        self.ammo_2 += (self.round_counter*2)
                    if self.difficulty == 1:
                        self.ammo_2 += (self.round_counter+5)
                    if self.difficulty == 2:
                        self.ammo_2 += (self.round_counter+2)
                    if self.difficulty == 3:
                        self.ammo_2 += (self.round_counter+1)
                    break
            if arcade.get_distance_between_sprites(self.sprite1, self.sprite2) < 50:
                if self.ammo_2 > 0:
                    arcade.sound.play_sound(self.reload_sound)
                if self.ammo_reserve <= (300-self.ammo_2):
                    self.ammo_reserve += self.ammo_2
                    self.ammo_2 = 0
                else:
                    self.ammo_reserve = 300
            for i in range(0, len(self.health_texture_list)):
                if arcade.get_distance_between_sprites(self.sprite1, self.health_texture_list[i]) < 50:
                    self.health_texture_list[i].remove_from_sprite_lists()
                    if self.difficulty == 0:
                        self.poeng1 = 100
                    if self.difficulty == 1:
                        if self.poeng1 <= 50:
                            self.poeng1 += 50
                        else:
                            self.poeng1 = 100
                    arcade.sound.play_sound(self.joy_sound)
                    break
                if arcade.get_distance_between_sprites(self.sprite2, self.health_texture_list[i]) < 50:
                    self.health_texture_list[i].remove_from_sprite_lists()
                    if self.difficulty == 0:
                        self.poeng2 = 100
                    if self.difficulty == 1:
                        if self.poeng2 <= 50:
                            self.poeng2 += 50
                        else:
                            self.poeng2 = 100
                    arcade.sound.play_sound(self.joy_sound)
                    break


        changed = False

        # Scroll left
        left_bndry = self.view_left + VIEWPORT_MARGIN
        if self.sprite1.left < left_bndry:
            self.view_left -= left_bndry - self.sprite1.left
            changed = True

        # Scroll right
        right_bndry = self.view_left + self.width - VIEWPORT_MARGIN
        if self.sprite1.right > right_bndry:
            self.view_left += self.sprite1.right - right_bndry
            changed = True
        #print(self.view_bottom)
        # Scroll up
        top_bndry = self.view_bottom + self.height - VIEWPORT_MARGIN
        if self.sprite1.top > top_bndry:
            self.view_bottom += self.sprite1.top - top_bndry
            changed = True

        # Scroll down
        bottom_bndry = self.view_bottom + VIEWPORT_MARGIN
        if self.sprite1.bottom < bottom_bndry:
            self.view_bottom -= bottom_bndry - self.sprite1.bottom
            changed = True

        if changed:
            arcade.set_viewport(self.view_left,
                                self.width + self.view_left,
                                self.view_bottom,
                                self.height + self.view_bottom)

    def on_mouse_press(self, x, y, button, modifiers):

        self.target_x = x
        self.target_y = y
        if len(self.bullet_01_list) == 0:
            self.test6 = True
        self.degrees_make = True
        self.mouse_bullet = True
        # print(x, y)

    def on_mouse_release(self, x, y, button, modifiers):
        self.mouse_bullet = False

    def on_mouse_motion(self, x, y, dx, dy):
        pass
        self.target_x = x
        self.target_y = y
        # print(x, y)

    def on_key_press(self, symbol, modifiers):

        """
        Keyboard input fra player 1
        """
        if self.pause == False:
            if self.sprite1_delete == False:
                if symbol == arcade.key.D:
                    #self.sprite1.change_x = MOVEMENT_SPEED
                    self.right1 = True
                    self.player1_retning = 0
                if symbol == arcade.key.A:
                    #self.sprite1.change_x = -MOVEMENT_SPEED
                    self.left1 = True
                    self.player1_retning = 1
                if symbol == arcade.key.W:
                    self.player_list.update()
                    self.player_list.update_animation()
                    #self.sprite1.change_y = MOVEMENT_SPEED
                    self.up1 = True
                    """
                    if self.sprite1_up == False:
                        self.sprite1.remove_from_sprite_lists()
                        self.sprite1 = arcade.Sprite("Sprite/Stan_rygg.png", center_x=100, center_y=100, scale=0.8)
                        self.sprite_list.append(self.sprite1)
                        self.sprite1_up = True
                    """
                    self.player1_retning = 2
                if symbol == arcade.key.S:
                    self.player_list.update()
                    self.player_list.update_animation()
                    #self.sprite1.change_y = -MOVEMENT_SPEED
                    self.down1 = True
                    """
                    if self.sprite1_up:
                        self.sprite1.remove_from_sprite_lists()
                        self.sprite1 = arcade.Sprite("Sprite/Stan.png", center_x=100, center_y=100, scale=0.8)
                        self.sprite_list.append(self.sprite1)
                        self.sprite1_up = False
                    """
                    self.player1_retning = 3

            """
            Skyter bullets
            """
            #print("jj")
            if self.sprite1_delete == False:
                if symbol == arcade.key.K:
                    pass
                    #self.bullet_make = True
                    # self.bullet_fire = True
                    #self.test3 = True
                    # print(self.sprite1._color)
                    # self.sprite1.color = (255, 100, 100)
                if symbol == arcade.key.R:
                    if self.ammo_reserve > (60-self.ammo):
                        self.ammo_reserve -= (60-self.ammo)
                        self.ammo = 60
                    else:
                        self.ammo += self.ammo_reserve
                        self.ammo_reserve = 0
                    """
                    if self.ammo + self.ammo_reserve <= 60:
                        self.ammo += self.ammo_reserve
                        self.ammo_reserve = 0
                    else:
                        pass
                    if self.ammo > 0 and self.ammo_reserve > 0:
                        while self.ammo <= 60:
                            self.ammo_reserve -= 1
                            self.ammo += 1
                    """
                if self.ammo > 0:
                    if self.player_number == 1:
                        #print("hh")
                        if symbol == arcade.key.RIGHT:
                            self.SH = True
                            #self.bullet_x_make = True
                            self.test3 = True
                            #print("H", self.SV, self.SH)
                        if symbol == arcade.key.LEFT:
                            self.SV = True
                            #self.bullet_xn_make = True
                            self.test3_xn = True
                            #print("V", self.SV, self.SH)
                            #print(len(self.bullet_list_xn))
                        if symbol == arcade.key.UP:
                            #print("U")
                            self.SU = True
                            #self.bullet_y_make = True
                            self.test3_y = True
                        if symbol == arcade.key.DOWN:
                            #print("D")
                            self.SD = True
                            #self.bullet_yn_make = True
                            self.test3_yn = True

            if self.ammo > 0:
                if symbol == arcade.key.LSHIFT:
                    if len(self.bullet_01_list) == 0:
                        self.test6 = True
                    self.degrees_make = True
                    self.mouse_bullet = True

            if symbol == arcade.key.M:
                self.sprite2_hit = True

            if symbol == arcade.key.RIGHT:
                self.player2_retning = 0
                self.right2 = True
            if symbol == arcade.key.LEFT:
                self.player2_retning = 1
                self.left2 = True
            if symbol == arcade.key.UP:
                self.player2_retning = 2
                self.up2 = True
            if symbol == arcade.key.DOWN:
                self.player2_retning = 3
                self.down2 = True

            if self.sprite5_follow == False:
                if symbol == arcade.key.F:
                    self.test2 = True
                    self.save_score = True
                    self.round_counter += 1
                    self.total_time = 0.0
                    self.minutes = 0
                    self.seconds = 0
                    arcade.sound.play_sound(self.start_sound)
                    self.sprite5_follow = True
                    #print("2a")

        if symbol == arcade.key.Y:
            if self.sprite1_delete == False:
                self.poeng1 = 100
            if self.sprite2_delete == False:
                self.poeng2 = 100

        if symbol == arcade.key.T:
            print(len(self.sprite_list))
            if self.sprite2_delete:
                print("kult")
                self.sprite2_make = True
                self.poeng2 = 100
                self.sprite2_delete = False
        if symbol == arcade.key.B:
            print(len(self.sprite_list))
            if self.sprite1_delete:
                print("kult")
                self.sprite1_make = True
                self.poeng1 = 100
                self.sprite1_delete = False
        if symbol == arcade.key.V:
            self.ammo = 60
            self.ammo_reserve = 300

        if symbol == arcade.key.ESCAPE:
            if self.test5:
                self.pause = True
                self.pause_menu = True
            else:
                self.pause = False
                self.pause_menu = False

        if self.start_menu:
            if symbol == arcade.key.ENTER:
                if self.difficulty == 0 or self.difficulty == 1:
                    self.poeng1 = 100
                    self.poeng2 = 100
                if self.difficulty == 2:
                    self.poeng1 = 100
                    self.poeng2 = 100
                if self.difficulty == 3:
                    self.ammo = 2
                    self.poeng1 = 100
                    self.poeng2 = 100
                self.ammo_reserve = 0
                self.sprite1.stand_right_textures.pop(0)
                self.sprite1.state = FACE_DOWN
                if self.player_number == 1:
                    self.sprite2_delete = True
                self.start_menu = False
                self.pause = False
            if symbol == arcade.key.KEY_2:
                self.sprite2_make = True
                # self.sprite_list.append(self.sprite2)
                self.scoreboard_playernum = 4
                self.player_number = 2
            if symbol == arcade.key.KEY_1:
                self.sprite2.remove_from_sprite_lists()
                self.scoreboard_playernum = 0
                self.player_number = 1
            if symbol == arcade.key.RIGHT:
                if self.difficulty == 3:
                    self.difficulty = 0
                else:
                    self.difficulty += 1
            if symbol == arcade.key.LEFT:
                if self.difficulty == 0:
                    self.difficulty = 3
                else:
                    self.difficulty -= 1

        if self.game_over == True or self.pause_menu == True:
            if symbol == arcade.key.ENTER:
                while self.enemy2_list:
                    self.enemy2_list.pop()
                while self.enemy_health:
                    self.enemy_health.pop()
                while self.sprite_list:
                    self.sprite_list.pop()
                while self.ammo_texture_list:
                    self.ammo_texture_list.pop()
                while self.ammo_pack_list:
                    self.ammo_pack_list.pop()
                while self.health_texture_list:
                    self.health_texture_list.pop()
                self.penger = 0
                self.ammo = 20
                self.round_counter = 0
                self.minutes = 0
                self.seconds = 0
                self.sprite1_make = True
                self.poeng1 = 100
                self.sprite1_delete = False
                if self.player_number == 2:
                    self.sprite2_make = True
                    self.sprite2_delete = False
                self.poeng2 = 100
                self.game_over = False
                self.pause = False
                self.player1_x = (self.view_left + self.width / 4)
                self.player1_y = (self.view_bottom + self.height / 2)
                self.pause_menu = False
                self.start_menu = True

    def on_key_release(self, symbol, modifiers):

        if self.pause == False:
            if symbol == arcade.key.D:
                self.sprite1.change_x = 0
                self.right1 = False
            if symbol == arcade.key.A:
                self.sprite1.change_x = 0
                self.left1 = False
            if symbol == arcade.key.W:
                self.sprite1.change_y = 0
                self.up1 = False
            if symbol == arcade.key.S:
                self.sprite1.change_y = 0
                self.down1 = False

            if symbol == arcade.key.RIGHT:
                self.right2 = False
            if symbol == arcade.key.LEFT:
                self.left2 = False
            if symbol == arcade.key.UP:
                self.up2 = False
            if symbol == arcade.key.DOWN:
                self.down2 = False

            if self.player_number == 1:
                if symbol == arcade.key.RIGHT:

                    self.SH = False
                    self.bullet_x_make = False

                    #print("SH", self.SV, self.SH)
                if symbol == arcade.key.LEFT:

                    self.SV = False
                    self.bullet_xn_make = False

                    #print("SV", self.SV, self.SH)
                if symbol == arcade.key.UP:
                    #print("SU")
                    self.SU = False
                    self.bullet_y_make = False
                if symbol == arcade.key.DOWN:
                    #print("SD")
                    self.SD = False
                    self.bullet_yn_make = False

            if symbol == arcade.key.K:
                self.bullet_make = False
                # self.sprite1.color = (255, 255, 255)

            if symbol == arcade.key.LSHIFT:
                self.mouse_bullet = False

            if symbol == arcade.key.M:
                self.sprite2_hit = False

        if symbol == arcade.key.ESCAPE:
            if self.pause:
                self.test5 = False
            else:
                self.test5 = True


MyGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT, 'My Game window')
arcade.run()
