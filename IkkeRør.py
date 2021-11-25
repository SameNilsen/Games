import arcade
from time import sleep
import random
from arcade.geometry import check_for_collision

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
VIEWPORT_MARGIN = 40

class MyGameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title, resizable=True)

        self.width = width
        self.height = height

        #self.set_location(400, 200)

        #Startsposisjoner for Sprite1 og Sprite2 og Hamster

        self.player1_x = 100
        self.player1_y = 200
        self.player1_speed = 250

        self.player2_x = 100
        self.player2_y = 400
        self.player2_speed = 250

        self.sprite3_speed = 100
        self.sprite3_y = 100
        self.sprite3_x = 1000
        self.sprite_list = None
        self.sprite1 = arcade.Sprite("Sprite/Stan.png", center_x=100, center_y=100, scale=0.8)

        self.sprite2 = arcade.Sprite("Sprite/Høne.png", center_x=100, center_y=100, scale=0.1)

        self.right1 = False
        self.left1 = False
        self.up1 = False
        self.down1 = False

        self.right2 = False
        self.left2 = False
        self.up2 = False
        self.down2 = False

        self.sprite3_Move = False

        self.background = None

        self.enemy_list = None
        self.enemy_list_on = False

        self.test1 = True

        self.total_time = 0.0

        self.round_counter = 101

        self.y_list = []

        self.enemy2_list = None

        self.enemy_list = arcade.SpriteList()
        self.sprite_list = arcade.SpriteList()
        self.enemy2_list = arcade.SpriteList()

        self.poeng1 = 1000
        self.poeng2 = 1000
        self.sprite_list.append(self.sprite2)
        self.sprite_list.append(self.sprite1)

        self.sprite5_x = 800
        self.sprite5_y = 100
        self.sprite5_speed = 250

        self.sprite5_follow = False

        # self.sprite5 = arcade.Sprite("Sprite/ShrekIMG5.png", center_x=100, center_y=100, scale=0.07)
        # self.sprite5.set_position(self.sprite5_x, self.sprite5_y)

        self.sprite1_delete = False
        self.sprite2_delete = False

        self.test2 = True

        self.crash_fart = 0.5

        self.background_num = 0

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

        self.fire0 = False
        self.fire1 = False
        self.fire2 = False
        self.fire3 = False

        self.player1_retning = 0

        self.gun_sound = arcade.sound.load_sound("Lyder/laser2.wav")

        self.test4 = 0
        self.enemy_position = 0

    def on_resize(self, width, height):
        """ This method is automatically called when the window is resized. """

        # Call the parent. Failing to do this will mess up the coordinates, and default to 0,0 at the center and the
        # edges being -1 to 1.
        super().on_resize(width, height)

        self.width = width
        self.height = height

        print(width, height)

    def on_draw(self):

        arcade.start_render()

        """
        Tegner Hamsterne og lager en liste med y-verdier 
        """
        if self.test1:
            for n in range(0, self.round_counter * 2):
                for i in range(0, 3):
                    self.sprite3_y = i * 200 + (random.randint(20, 200))
                    self.y_list.append(self.sprite3_y)
                    print(self.sprite3_y)
                    self.sprite3 = arcade.Sprite("Sprite/Hamster.png", center_x=100, center_y=100,
                                                 scale=(random.uniform(0.1, 0.5)))
                    self.enemy_list.append(self.sprite3)
                    self.sprite3.set_position(self.sprite3_x + (n * 200), self.y_list[(3 * n) + i])

                self.enemy_list_on = True
            self.test1 = False
            print("y_list:", self.y_list)
            self.sprite4 = arcade.Sprite("Sprite/Hamster.png", center_x=100, center_y=100, scale=1.8)
            self.sprite4.set_position(1200 + ((self.round_counter - 1) * 400), 300)
            self.enemy_list.append(self.sprite4)

        """
        Tegner Fiender
        """
        if self.test2:
            for i in range(0, (self.round_counter + 1)):
                self.sprite5 = arcade.Sprite("Sprite/ShrekIMG5.png", center_x=100, center_y=100, scale=0.07)
                if self.enemy_position == 0:
                    self.sprite5.set_position(self.width + 200 * i, 300)
                if self.enemy_position == 1:
                    self.sprite5.set_position(0 - 200 * i, 300)
                if self.enemy_position == 2:
                    self.sprite5.set_position(500, self.height + 200*i)
                if self.enemy_position == 3:
                    self.sprite5.set_position(500, 0 - 200*i)
                self.enemy2_list.append(self.sprite5)
                self.enemy_position += 1
                if self.enemy_position == 4:
                    self.enemy_position = 0
            self.enemy_position = 0
            self.test2 = False

        """
        Tegner bakgrunnen avhengig av variabel
        """
        if self.background_num == 0:
            self.background = arcade.load_texture("Sprite/background.png")
            arcade.draw_texture_rectangle(self.width // 2, self.height // 2,
                                          self.width, self.height, self.background)

        if self.background_num == 1:
            self.background = arcade.load_texture("Sprite/background2.png")
            arcade.draw_texture_rectangle(self.width // 2, self.height // 2,
                                          self.width, self.height, self.background)


        """
        Tegner tekst
        """
        arcade.draw_text(f"Level: {self.round_counter}", (self.width-100), (self.height-20), arcade.color.BLACK, 20)
        arcade.draw_text(f"Poeng Høne: {self.poeng2}", (self.width-200), (self.height-40), arcade.color.BLACK, 20)
        arcade.draw_text(f"Poeng Freddie: {self.poeng1}", (self.width-220), (self.height-60), arcade.color.BLACK, 20)
        arcade.draw_text(f"Tid: {10-self.seconds}", (self.width-100), (self.height-80), arcade.color.BLACK, 20)


        """
        Tegner skuddene og legger dem til i en liste gitt av retning
        """
        if self.bullet_make:
            self.bullet_retning = self.player1_retning
            self.bullet_fire = True
            self.bullet_x = self.player1_x
            self.bullet_y = self.player1_y
            if self.bullet_retning == 0:
                self.fire0 = True
                if self.test3:
                    self.bullet = arcade.Sprite("Sprite/Laser.png", center_x=self.bullet_x, center_y=self.bullet_y, scale=1)
                    arcade.sound.play_sound(self.gun_sound)
                    self.bullet_list_x.append(self.bullet)
                    self.test3 = False
                for i in range(0, len(self.bullet_list_x)):
                    if arcade.get_distance_between_sprites(self.sprite1, self.bullet_list_x[-1]) > 50:
                        arcade.sound.play_sound(self.gun_sound)
                        self.bullet = arcade.Sprite("Sprite/Laser.png", center_x=self.bullet_x, center_y=self.bullet_y,
                                                    scale=1)
                        self.bullet_list_x.append(self.bullet)


            if self.bullet_retning == 1:
                self.fire1 = True
                if self.test3:
                    self.bullet = arcade.Sprite("Sprite/Laser.png", center_x=self.bullet_x, center_y=self.bullet_y, scale=1)
                    self.bullet.angle = 180
                    arcade.sound.play_sound(self.gun_sound)
                    self.bullet_list_xn.append(self.bullet)
                    self.test3 = False
                for i in range(0, len(self.bullet_list_xn)):
                    if arcade.get_distance_between_sprites(self.sprite1, self.bullet_list_xn[-1]) > 50:
                        # print("i:", i)
                        self.bullet = arcade.Sprite("Sprite/Laser.png", center_x=self.bullet_x, center_y=self.bullet_y,
                                                    scale=1)
                        self.bullet.angle = 180
                        arcade.sound.play_sound(self.gun_sound)
                        self.bullet_list_xn.append(self.bullet)


            if self.bullet_retning == 2:
                self.fire2 = True
                if self.test3:
                    self.bullet = arcade.Sprite("Sprite/Laser.png", center_x=self.bullet_x, center_y=self.bullet_y, scale=1)
                    self.bullet.angle = 90
                    arcade.sound.play_sound(self.gun_sound)
                    self.bullet_list_y.append(self.bullet)
                    self.test3 = False
                for i in range(0, len(self.bullet_list_y)):
                    if arcade.get_distance_between_sprites(self.sprite1, self.bullet_list_y[-1]) > 50:
                        # print("i:", i)
                        self.bullet = arcade.Sprite("Sprite/Laser.png", center_x=self.bullet_x, center_y=self.bullet_y,
                                                    scale=1)
                        self.bullet.angle = 90
                        arcade.sound.play_sound(self.gun_sound)
                        self.bullet_list_y.append(self.bullet)


            if self.bullet_retning == 3:
                self.fire3 = True
                if self.test3:
                    self.bullet = arcade.Sprite("Sprite/Laser.png", center_x=self.bullet_x, center_y=self.bullet_y, scale=1)
                    self.bullet.angle = 270
                    arcade.sound.play_sound(self.gun_sound)
                    self.bullet_list_yn.append(self.bullet)
                    self.test3 = False
                for i in range(0, len(self.bullet_list_yn)):
                    if arcade.get_distance_between_sprites(self.sprite1, self.bullet_list_yn[-1]) > 50:
                        # print("i:", i)
                        self.bullet = arcade.Sprite("Sprite/Laser.png", center_x=self.bullet_x, center_y=self.bullet_y,
                                                    scale=1)
                        self.bullet.angle = 270
                        arcade.sound.play_sound(self.gun_sound)
                        self.bullet_list_yn.append(self.bullet)


        """
        Tegner listene
        """
        if self.sprite3_Move:
            self.enemy_list.draw()

        self.sprite_list.draw()

        if self.sprite5_follow:
            self.enemy2_list.draw()

        self.bullet_list_x.draw()
        self.bullet_list_xn.draw()
        self.bullet_list_y.draw()
        self.bullet_list_yn.draw()

    def on_update(self, delta_time):
        #print(delta_time)

        self.enemy_list.update()

        self.seconds = self.total_time % 60


        """
        Beveger og avgrenser sprite1 og sprite2
        """

        if self.right1:
            self.player1_x += self.player1_speed * delta_time
        if self.left1:
            self.player1_x -= self.player1_speed * delta_time
        if self.up1:
            self.player1_y += self.player1_speed * delta_time
        if self.down1:
            self.player1_y -= self.player1_speed * delta_time

        self.sprite1.set_position(self.player1_x, self.player1_y)


        if self.player1_y > (self.height-45):
            self.player1_y = (self.height-45)
        if self.background_num == 0:
            if self.player1_x < 40:
                self.player1_x = 40
            if self.player1_x > (self.width-35):
                if self.player1_y < (self.height/3):
                    self.player1_x = (self.width-35)
                elif self.player1_y > (self.height/3)*2:
                    self.player1_x = (self.width - 35)
        if self.background_num == 1:
            if self.player1_x < 40:
                if self.player1_y < (self.height / 3):
                    self.player1_x = 40
                elif self.player1_y > (self.height / 3)*2:
                    self.player1_x = 40
            if self.player1_x > (self.width-35):
                    self.player1_x = (self.width - 35)
        if self.player1_y < 45:
            self.player1_y = 45

        if self.right2:
            self.player2_x += self.player2_speed * delta_time
        if self.left2:
            self.player2_x -= self.player2_speed * delta_time
        if self.up2:
            self.player2_y += self.player2_speed * delta_time
        if self.down2:
            self.player2_y -= self.player2_speed * delta_time

        self.sprite2.set_position(self.player2_x, self.player2_y)

        if self.player2_y > (self.height-35):
            self.player2_y = (self.height-35)
        if self.background_num == 0:
            if self.player2_x < 30:
                self.player2_x = 30
            if self.player2_x > (self.width-25):
                if self.player2_y < (self.height/3):
                    self.player2_x = (self.width-25)
                elif self.player2_y > (self.height/3)*2:
                    self.player2_x = (self.width - 25)
        if self.background_num == 1:
            if self.player2_x < 30:
                if self.player2_y < (self.height / 3):
                    self.player2_x = 30
                elif self.player2_y > (self.height / 3)*2:
                    self.player2_x = 30
            if self.player2_x > (self.width-25):
                    self.player2_x = (self.width - 25)
        if self.player2_y < 35:
            self.player2_y = 35

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
        Beveger og fjerner hamsterne
        """

        if self.sprite3_Move:
            if self.enemy_list_on:
                for n in range(0, self.round_counter * 2):
                    for i in range(0, 3):
                        self.enemy_list[(3 * n) + i].set_position(self.sprite3_x + (n * 200), self.y_list[(3 * n) + i])
                self.enemy_list[-1].set_position(self.sprite3_x + 1000 + (self.round_counter - 1) * 400, 300)
                self.sprite3_x -= self.sprite3_speed * delta_time

                if self.seconds >= (2500 + ((self.round_counter - 1) * 400)) / self.sprite3_speed:
                    self.y_list = []
                    self.enemy_list_on = False
                    self.sprite3_Move = False
                    self.sprite3_x = 1000
                    self.round_counter += 1
                    print(self.seconds)
                    self.enemy_list = None
                    self.enemy_list = arcade.SpriteList()
                    self.total_time = 0.0
                    self.test1 = True
                if self.poeng2 < 950:
                    # print("h")
                    self.sprite2.remove_from_sprite_lists()

            self.total_time += delta_time

        if self.sprite3_Move:
            if len(arcade.check_for_collision_with_list(self.sprite2, self.enemy_list)) > 0:
                self.poeng2 -= 1
            if len(arcade.check_for_collision_with_list(self.sprite1, self.enemy_list)) > 0:
                self.poeng1 -= 1


        """
        Beveger fiender og fjerner dem etter hver runde
        """

        if self.sprite5_follow:

            self.total_time += delta_time

            for i in range(0, len(self.enemy2_list)):
                delta_time1 = 0.016

                self.endring2_x = self.sprite2._get_center_x() - self.enemy2_list[i]._get_center_x()
                self.endring2_y = self.sprite2._get_center_y() - self.enemy2_list[i]._get_center_y()

                self.endring1_x = self.sprite1._get_center_x() - self.enemy2_list[i]._get_center_x()
                self.endring1_y = self.sprite1._get_center_y() - self.enemy2_list[i]._get_center_y()

                k = 0
                l = 0

                if self.sprite1_delete:
                    for o in range(0, len(self.enemy2_list)):
                        if o != i:
                            if arcade.check_for_collision(self.enemy2_list[i], self.enemy2_list[o]):
                                k += 1
                                if arcade.get_distance_between_sprites(self.enemy2_list[i],
                                                                       self.sprite2) > arcade.get_distance_between_sprites(
                                        self.enemy2_list[o], self.sprite2):
                                    l += 1
                    if k > 0:
                        if l > 0:
                            self.fart_x = self.endring2_x * delta_time * self.crash_fart
                            self.fart_y = self.endring2_y * delta_time * self.crash_fart
                        else:
                            self.fart_x = self.endring2_x * delta_time
                            self.fart_y = self.endring2_y * delta_time
                    else:
                        self.fart_x = self.endring2_x * delta_time
                        self.fart_y = self.endring2_y * delta_time
                elif self.sprite2_delete:
                    for o in range(0, len(self.enemy2_list)):
                        if o != i:
                            if arcade.check_for_collision(self.enemy2_list[i], self.enemy2_list[o]):
                                k += 1
                                if arcade.get_distance_between_sprites(self.enemy2_list[i],
                                                                       self.sprite1) > arcade.get_distance_between_sprites(
                                        self.enemy2_list[o], self.sprite1):
                                    l += 1
                    if k > 0:
                        if l > 0:
                            self.fart_x = self.endring1_x * delta_time * self.crash_fart
                            self.fart_y = self.endring1_y * delta_time * self.crash_fart
                        else:
                            self.fart_x = self.endring1_x * delta_time
                            self.fart_y = self.endring1_y * delta_time
                    else:
                        self.fart_x = self.endring1_x * delta_time
                        self.fart_y = self.endring1_y * delta_time
                else:
                    if arcade.get_distance_between_sprites(self.sprite1, self.enemy2_list[i]) < arcade.get_distance_between_sprites(self.sprite2, self.enemy2_list[i]):
                        for o in range(0, len(self.enemy2_list)):
                            if o != i:
                                if arcade.check_for_collision(self.enemy2_list[i], self.enemy2_list[o]):
                                    k += 1
                                    if arcade.get_distance_between_sprites(self.enemy2_list[i],
                                                                           self.sprite1) > arcade.get_distance_between_sprites(
                                            self.enemy2_list[o], self.sprite1):
                                        l += 1
                        if k > 0:
                            if l > 0:
                                self.fart_x = self.endring1_x * delta_time1 * self.crash_fart
                                self.fart_y = self.endring1_y * delta_time1 * self.crash_fart
                            else:
                                self.fart_x = self.endring1_x * delta_time1
                                self.fart_y = self.endring1_y * delta_time1
                        else:
                            self.fart_x = self.endring1_x * delta_time1
                            self.fart_y = self.endring1_y * delta_time1
                    elif arcade.get_distance_between_sprites(self.sprite2, self.enemy2_list[i]) < arcade.get_distance_between_sprites(self.sprite1, self.enemy2_list[i]):
                        for o in range(0, len(self.enemy2_list)):
                            if o != i:
                                if arcade.check_for_collision(self.enemy2_list[i], self.enemy2_list[o]):
                                    k += 1
                                    if arcade.get_distance_between_sprites(self.enemy2_list[i], self.sprite2) > arcade.get_distance_between_sprites(self.enemy2_list[o], self.sprite2):
                                        l += 1
                                        break
                        if k > 0:
                            if l > 0:
                                self.fart_x = self.endring2_x * delta_time * self.crash_fart
                                self.fart_y = self.endring2_y * delta_time * self.crash_fart
                            else:
                                self.fart_x = self.endring2_x * delta_time
                                self.fart_y = self.endring2_y * delta_time
                        else:
                            self.fart_x = self.endring2_x * delta_time
                            self.fart_y = self.endring2_y * delta_time



                self.sprite5_x = self.enemy2_list[i]._get_center_x() + self.fart_x
                self.sprite5_y = self.enemy2_list[i]._get_center_y() + self.fart_y


                self.enemy2_list[i].set_position(self.sprite5_x, self.sprite5_y)


            if self.seconds >= 10 or len(self.enemy2_list) == 0:
                self.sprite5_x = 800
                self.sprite5_y = 100
                self.round_counter += 1
                while self.enemy2_list:
                    self.enemy2_list.pop()
                self.enemy_list = None
                self.enemy_list = arcade.SpriteList()
                self.total_time = 0.0
                self.sprite5_follow = False
                self.test2 = True

        if self.sprite5_follow:
            if arcade.check_for_collision_with_list(self.sprite2, self.enemy2_list):
                self.poeng2 -= 1
            if arcade.check_for_collision_with_list(self.sprite1, self.enemy2_list):
                self.poeng1 -= 1

        if self.poeng2 <= 0:
            self.sprite2.remove_from_sprite_lists()
            self.sprite2_delete = True
            self.poeng2 = 0
        if self.poeng1 <= 0:
            self.sprite1.remove_from_sprite_lists()
            self.sprite1_delete = True
            self.poeng1 = 0


        """
        Beveger og fjerner bullets
        """

        if self.bullet_fire:

            if self.fire0:
                for i in range(0, len(self.bullet_list_x)):
                    self.bullet_x = self.bullet_list_x[i]._get_center_x() + 10
                    self.bullet_y = self.bullet_list_x[i]._get_center_y()
                    self.bullet_list_x[i].set_position(self.bullet_x, self.bullet_y)

            if self.fire1:
                for i in range(0, len(self.bullet_list_xn)):
                    self.bullet_x = self.bullet_list_xn[i]._get_center_x() - 10
                    self.bullet_y = self.bullet_list_xn[i]._get_center_y()
                    self.bullet_list_xn[i].set_position(self.bullet_x, self.bullet_y)

            if self.fire2:

                for i in range(0, len(self.bullet_list_y)):
                    self.bullet_y = self.bullet_list_y[i]._get_center_y() + 10
                    self.bullet_x = self.bullet_list_y[i]._get_center_x()
                    self.bullet_list_y[i].set_position(self.bullet_x, self.bullet_y)

            if self.fire3:

                for i in range(0, len(self.bullet_list_yn)):
                    self.bullet_y = self.bullet_list_yn[i]._get_center_y() - 10
                    self.bullet_x = self.bullet_list_yn[i]._get_center_x()
                    self.bullet_list_yn[i].set_position(self.bullet_x, self.bullet_y)

            for i in range(0, len(self.bullet_list_x)):
                try:
                    if self.bullet_list_x[i]._get_center_x() > self.width:
                        self.bullet_list_x[i].remove_from_sprite_lists()
                except:
                    pass
                try:
                    for o in range(0, len(self.enemy2_list)):
                        if arcade.check_for_collision(self.bullet_list_x[i], self.enemy2_list[o]):
                            self.enemy2_list[o].remove_from_sprite_lists()
                            self.bullet_list_x[i].remove_from_sprite_lists()
                except:
                    pass
            for i in range(0, len(self.bullet_list_xn)):
                try:
                    if self.bullet_list_xn[i]._get_center_x() < 0:
                        self.bullet_list_xn[i].remove_from_sprite_lists()
                except:
                    pass
                try:
                    for o in range(0, len(self.enemy2_list)):
                        if arcade.check_for_collision(self.bullet_list_xn[i], self.enemy2_list[o]):
                            self.enemy2_list[o].remove_from_sprite_lists()
                            self.bullet_list_xn[i].remove_from_sprite_lists()
                except:
                    pass
            for i in range(0, len(self.bullet_list_y)):
                try:
                    if self.bullet_list_y[i]._get_center_y() > self.height:
                        self.bullet_list_y[i].remove_from_sprite_lists()
                except:
                    pass
                try:
                    for o in range(0, len(self.enemy2_list)):
                        if arcade.check_for_collision(self.bullet_list_y[i], self.enemy2_list[o]):
                            self.enemy2_list[o].remove_from_sprite_lists()
                            self.bullet_list_y[i].remove_from_sprite_lists()
                            #print("i:", i, "o:", o)
                except:
                    pass
            for i in range(0, len(self.bullet_list_yn)):
                try:
                    if self.bullet_list_yn[i]._get_center_y() < 0:
                        self.bullet_list_yn[i].remove_from_sprite_lists()
                except:
                    pass
                try:
                    for o in range(0, len(self.enemy2_list)):
                        if arcade.check_for_collision(self.bullet_list_yn[i], self.enemy2_list[o]):
                            self.enemy2_list[o].remove_from_sprite_lists()
                            self.bullet_list_yn[i].remove_from_sprite_lists()
                except:
                    pass

        if self.sprite5_follow:
            if self.test4 == 0:
                self.test4 = 1
        if self.test4 == 1:
            self.poeng2 = 100
            self.poeng1 = 100
            self.test4 = 2


    def on_key_press(self, symbol, modifiers):

        """
        Keyboard input fra player 1
        """
        if self.sprite1_delete == False:
            if symbol == arcade.key.RIGHT:
                self.right1 = True
                self.player1_retning = 0
            if symbol == arcade.key.LEFT:
                self.left1 = True
                self.player1_retning = 1
            if symbol == arcade.key.UP:
                self.up1 = True
                self.sprite_list.pop()
                self.sprite1 = arcade.Sprite("Sprite/Stan_rygg.png", center_x=100, center_y=100, scale=0.8)
                self.sprite_list.append(self.sprite1)
                self.player1_retning = 2
            if symbol == arcade.key.DOWN:
                self.down1 = True
                self.sprite_list.pop()
                self.sprite1 = arcade.Sprite("Sprite/Stan.png", center_x=100, center_y=100, scale=0.8)
                self.sprite_list.append(self.sprite1)
                self.player1_retning = 3

        """
        Skyter bullets
        """
        if symbol == arcade.key.K:
            self.bullet_make = True
            #self.bullet_fire = True
            self.test3 = True



        if symbol == arcade.key.D:
            self.right2 = True
        if symbol == arcade.key.A:
            self.left2 = True
        if symbol == arcade.key.W:
            self.up2 = True
        if symbol == arcade.key.S:
            self.down2 = True

        if symbol == arcade.key.B:
            self.sprite3_speed = 180
            self.sprite3_Move = True
        if symbol == arcade.key.G:
            self.sprite3_speed = 500
            self.sprite3_Move = True

        if symbol == arcade.key.F:
            self.sprite5_follow = True


    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.RIGHT:
            self.right1 = False
        if symbol == arcade.key.LEFT:
            self.left1 = False
        if symbol == arcade.key.UP:
            self.up1 = False
        if symbol == arcade.key.DOWN:
            self.down1 = False

        if symbol == arcade.key.D:
            self.right2 = False
        if symbol == arcade.key.A:
            self.left2 = False
        if symbol == arcade.key.W:
            self.up2 = False
        if symbol == arcade.key.S:
            self.down2 = False

        if symbol == arcade.key.K:
            self.bullet_make = False


MyGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT, 'My Game window')
arcade.run()
