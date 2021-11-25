import arcade
import random
import math
import ctypes

user32 = ctypes.windll.user32
print(user32.GetSystemMetrics(0), user32.GetSystemMetrics(1))

SCREEN_WIDTH = user32.GetSystemMetrics(0)
SCREEN_HEIGHT = user32.GetSystemMetrics(1) - 63

class MyGameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title, fullscreen=True)

        print(self.width, self.height)

        self.sprite_list = None
        self.sprite_list = arcade.SpriteList()

        self.shape_list = None
        self.shape_list = arcade.ShapeElementList()

        self.sprite = arcade.Sprite("Sprite/NakenRotte2.png", center_x=100, center_y=100, scale=0.25)      #(self.width*self.height)/12000000)
        self.player_x = 200
        self.player_y = 100
        self.player_speed = 4
        self.sprite.set_position(self.player_x, self.player_y)

        self.sprite_list.append(self.sprite)
        #self.sprite.scale = 1 / (25600 / (self.width))
        print(self.sprite.width, self.sprite.height, self.sprite.scale)

        self.up = False
        self.down = False
        self.right = False
        self.left = False
        self.faktisk_up = False
        self.faktisk_down = False
        self.faktisk_right = False
        self.faktisk_left = False
        self.retning = 0

        self.sprite2 = arcade.Sprite("Sprite/PacMan.png", center_x=100, center_y=100, scale=1/3.45)      #(self.width*self.height)/12000000)
        self.x = self.player_x
        self.y = self.player_y
        self.end_x = self.x
        self.end_y = self.y
        self.sprite2.set_position(self.x, self.y)
        print(23232, self.sprite2.width, self.sprite2.height)
        self.bombe_list = None
        self.bombe_list = arcade.SpriteList()

        for i in range(0, 20):
            bombe = arcade.Sprite("Sprite/Bombe.png", center_x=random.randint(0, self.width), center_y=random.uniform(0, self.height * (557/657)), scale=0.25)
            self.bombe_list.append(bombe)

        self.good_shit_liste = None
        self.good_shit_liste = arcade.SpriteList()
        self.skatt = arcade.Sprite("Sprite/Skatt.png", center_x=random.randint(0, self.width), center_y=random.uniform(0, self.height * (557/657)), scale=0.25)
        self.good_shit_liste.append(self.skatt)

        self.game_over = False
        self.win = False

        self.spider_sense = arcade.Sprite("Sprite/Spider_sense.png", center_x=self.player_x, center_y=self.player_y + 50, scale=0.25)

        self.AI_x = self.player_x
        self.AI_y = self.player_y

        self.beregn_vei = False
        self.tegn_vei = False
        self.points_list = []
        self.points_list_riktig_vei = []
        self.endepunkt_liste = []
        self.ytterpunkt_liste = []

        self.beregn = False
        self.run = False
        self.a = 0
        self.override = False

        self.pixel_list = []
        self.go = False
        self.b = 0

        self.pause = False

    """
    def on_resize(self, width, height):

        # Call the parent. Failing to do this will mess up the coordinates, and default to 0,0 at the center and the
        # edges being -1 to 1.
        super().on_resize(width, height)

        self.width = width
        self.height = height

        self.sprite.scale = 1/(25600/(self.width))
        print(self.sprite.width, self.sprite.height, self.sprite.scale)

        #900 886 1
        #1280/45 = 28.444
        #657/44.3 = 14.8

        print(self.width, self.height)
    """

    def on_draw(self):
        arcade.start_render()

        self.background = arcade.load_texture("Sprite/Muldvarp_bakgrunn.png")
        #self.background.draw(0, 0, self.width, self.height)
        arcade.draw_texture_rectangle(self.width // 2, self.height // 2, self.width, self.height, self.background)

        self.shape_list.draw()

        self.sprite_list.draw()

        self.sprite2.draw()
        #self.pixel_test_list.draw()

        for i in range(0, len(self.bombe_list)):
            if arcade.get_distance_between_sprites(self.sprite, self.bombe_list[i]) < 50:
                self.spider_sense.draw()

        arcade.draw_text(f"{self.target_x}, {self.target_y}", 50, self.height - 100, arcade.color.DARK_RED, 20)
        arcade.draw_text(f"{self.player_x}, {self.player_y}", 50, self.height - 120, arcade.color.DARK_RED, 20)
        arcade.draw_text(f"{self.x}, {self.y}", 50, self.height - 140, arcade.color.DARK_RED, 20)

        if self.game_over:
            arcade.draw_text("GAME OVER", self.width/2 - 50, self.height/2, arcade.color.RED, 40)
            self.bombe_list.draw()
            self.good_shit_liste.draw()
        if self.win:
            arcade.draw_text("DU VANT", self.width / 2 - 50, self.height / 2, arcade.color.RED, 40)
            self.bombe_list.draw()
            self.good_shit_liste.draw()

        if self.tegn_vei:
            #print(self.test, "test")
            #print(len((self.test)), "lengde av test")
            for i in range(0, len(self.ytterpunkt_liste), 2):
                #print(i)
                arcade.draw_point(self.ytterpunkt_liste[i], self.ytterpunkt_liste[i+1], arcade.color.RED, 5)

            for i in range(0, len(self.points_list), 2):
                #arcade.draw_point(self.points_list[i], self.points_list[i+1], arcade.color.RED, 5)
                pass
            #arcade.draw_point(self.points_list_riktig_vei[0], self.points_list_riktig_vei[1], arcade.color.RED, 5)
            #print(self.points_list_riktig_vei[0], self.points_list_riktig_vei[1])
            #arcade.draw_point(self.points_list_riktig_vei[-2], self.points_list_riktig_vei[-1], arcade.color.RED, 5)
            #print(self.points_list_riktig_vei[-1], self.points_list_riktig_vei[-2])
            #arcade.draw_point(self.retnings_punkt_x, self.retnings_punkt_y, arcade.color.RED, 5)
    def on_update(self, delta_time):

        if self.game_over == False:

            if self.right:
                self.player_x += self.player_speed
                shape = arcade.create_ellipse_filled_with_colors(self.player_x, self.player_y, 15, 15, arcade.color.BROWN, arcade.color.BROWN)
                self.shape_list.append(shape)
                self.retning = 0
            if self.left:
                self.player_x -= self.player_speed
                shape = arcade.create_ellipse_filled_with_colors(self.player_x, self.player_y, 15, 15, arcade.color.BROWN, arcade.color.BROWN)
                self.shape_list.append(shape)
                self.retning = 1
            if self.up:
                self.player_y += self.player_speed
                shape = arcade.create_ellipse_filled_with_colors(self.player_x, self.player_y, 15, 15, arcade.color.BROWN, arcade.color.BROWN)
                self.shape_list.append(shape)
                self.retning = 2
            if self.down:
                self.player_y -= self.player_speed
                shape = arcade.create_ellipse_filled_with_colors(self.player_x, self.player_y, 15, 15, arcade.color.BROWN, arcade.color.BROWN)
                self.shape_list.append(shape)
                self.retning = 3

            self.sprite.set_position(self.player_x, self.player_y)
            self.position = [round(self.player_x), round(self.player_y)]
            self.position_3 = [self.player_x, self.player_y+4]
            #print(3030, self.position_3)
            if len(self.pixel_list) == 0:
                self.pixel_list.append(self.position)
            else:
                nei = 0
                neinei = 0
                for i in range(0, len(self.pixel_list)):
                    #print(3030, self.player_x, self.player_y + 4)
                    if self.position == self.pixel_list[i]:
                        nei += 1
                        if len(self.pixel_list) > 1:
                            if self.retning == 0:
                                #print(44)
                                if [self.player_x-5, self.player_y] == self.pixel_list[i]:
                                    print(0000, self.player_x, self.player_y)
                                    neinei += 1
                            if self.retning == 1:
                                if [self.player_x+4, self.player_y] == self.pixel_list[i]:
                                    neinei += 1
                            if self.retning == 2:
                                if [self.player_x, self.player_y-4] == self.pixel_list[i]:
                                    neinei += 1
                            if self.retning == 3:
                                #print(3030, self.player_x, self.player_y+4)
                                if [self.player_x, self.player_y+4] == self.pixel_list[i]:
                                    print(3333, self.position_3)
                                    neinei += 1
                if nei == 0:
                    o = 3
                    #print(8989)
                    while o >= 0:
                        if self.retning == 0:
                            self.pixel_list.append([self.player_x-o, self.player_y])
                        if self.retning == 1:
                            self.pixel_list.append([self.player_x+o, self.player_y])
                        if self.retning == 2:
                            self.pixel_list.append([self.player_x, self.player_y-o])
                        if self.retning == 3:
                            self.pixel_list.append([self.player_x, self.player_y+o])
                        o -= 1
                if neinei > 0 and nei > 0:
                    o = 3
                    print(212211212121212)
                    while o >= 1:
                        if self.retning == 0:
                            self.pixel_list.append([self.player_x - o, self.player_y])
                        if self.retning == 1:
                            self.pixel_list.append([self.player_x + o, self.player_y])
                        if self.retning == 2:
                            self.pixel_list.append([self.player_x, self.player_y - o])
                        if self.retning == 3:
                            self.pixel_list.append([self.player_x, self.player_y + o])
                        o -= 1
            self.spider_sense.set_position(self.player_x, self.player_y + 50)

            if self.player_y > self.height-100:
                self.player_y = self.height-100
            if self.player_y < 0:
                self.player_y = 0
            if self.player_x > self.width:
                self.player_x = self.width
            if self.player_x < 0:
                self.player_x = 0

        for i in range(0, len(self.bombe_list)):
            if arcade.get_distance_between_sprites(self.sprite, self.bombe_list[i]) < 25:
                #self.game_over = True
                pass
        if arcade.get_distance_between_sprites(self.sprite, self.skatt) < 25:
            self.win = True


        if arcade.get_pixel(self.AI_x, self.AI_y) == arcade.color.BROWN:
            pass

        if self.beregn_vei:
            x = self.AI_x
            while x <= self.AI_x+16:
                y_pluss = self.AI_y + math.sqrt(256 - (x - self.AI_x)**2)
                print("y:", y_pluss, "x=", x)
                self.points_list.append(x)
                self.points_list.append(y_pluss)
                x += 0.1
            x = self.AI_x + 16
            while x >= self.AI_x:
                y_minus = self.AI_y - math.sqrt(256 - (x - self.AI_x) ** 2)
                print("y:", y_minus, "x=", x)
                self.points_list.append(x)
                self.points_list.append(y_minus)
                x -= 0.1
            x = self.AI_x
            while x >= self.AI_x-16:
                y_minus = self.AI_y - math.sqrt(256 - (x - self.AI_x) ** 2)
                print("y:", y_minus, "x=", x)
                self.points_list.append(x)
                self.points_list.append(y_minus)
                x -= 0.1
            x = self.AI_x - 16
            while x <= self.AI_x:
                y_pluss = self.AI_y + math.sqrt(256 - (x - self.AI_x)**2)
                print("y:", y_pluss, "x=", x)
                self.points_list.append(x)
                self.points_list.append(y_pluss)
                x += 0.1

            """
            for x in range(self.AI_x-50, self.AI_x+1):
                y_minus = self.AI_y - math.sqrt(2500 - (x - self.AI_x)**2)
                print("y:", y_minus, "x=", x)
                self.points_list.append(x)
                self.points_list.append(y_minus)
            """
            print("pointslist", self.points_list)
            print("Lengde av pointslist", len(self.points_list))
            for punkt in range(0, len(self.points_list), 2):
                #print(punkt, "ok")
                x = round(self.points_list[punkt])
                y = round(self.points_list[punkt+1])
                #print("uu", x, y)
                if arcade.get_pixel(x, y) == arcade.color.BROWN:
                    print(x, y, "BROWN")
                    self.points_list_riktig_vei.append(x)
                    self.points_list_riktig_vei.append(y)
                    self.endepunkt_liste.append(1)
                else:
                    print(x, y, "IKKE BRUN")
                    self.endepunkt_liste.append(0)

            print("endepunkt", self.endepunkt_liste)
            print("lengde av endepunkt", len(self.endepunkt_liste))
            print("rikitg vei liste", self.points_list_riktig_vei)
            print("lengde av riktig vei liste", len(self.points_list_riktig_vei))
            print("rikitg:", self.points_list_riktig_vei[0], self.points_list_riktig_vei[1], self.points_list_riktig_vei[-2], self.points_list_riktig_vei[-1])

            for i in range(0, len(self.endepunkt_liste)):
                if self.endepunkt_liste[i] == 1:
                    if i == len(self.endepunkt_liste)-1:
                        if self.endepunkt_liste[0] == 0:
                            print("ytterpunkt start eller slutt", self.points_list[i * 2], self.points_list[i * 2 + 1])
                            #if len(self.ytterpunkt_liste) == 0:
                            self.ytterpunkt_liste.append(self.points_list[i * 2])
                            self.ytterpunkt_liste.append(self.points_list[i * 2 + 1])
                    elif i == 0:
                        if self.endepunkt_liste[-1] == 0:
                            print("ytterpunkt start eller slutt", self.points_list[i * 2], self.points_list[i * 2 + 1])
                            self.ytterpunkt_liste.append(self.points_list[i * 2])
                            self.ytterpunkt_liste.append(self.points_list[i * 2 + 1])
                    else:
                        #print("i ikke 2004:", i)
                        if self.endepunkt_liste[i-1] == 0:
                            print("ytterpunkt 1", self.points_list[i*2], self.points_list[i*2 + 1])
                            #self.ytterpunkt_liste[0:0] = [self.points_list[i * 2 + 1]]
                            #self.ytterpunkt_liste[0:0] = [self.points_list[i*2]]
                            self.ytterpunkt_liste.append(self.points_list[i*2])
                            self.ytterpunkt_liste.append(self.points_list[i*2 + 1])
                        if self.endepunkt_liste[i + 1] == 0:
                            print("ytterpunkt 2", self.points_list[i * 2], self.points_list[i * 2 + 1])
                            #self.ytterpunkt_liste[2:2] = [self.points_list[i * 2 + 1]]
                            #self.ytterpunkt_liste[2:2] = [self.points_list[i * 2]]
                            if len(self.ytterpunkt_liste) == 0:
                                self.ytterpunkt_liste[0:0] = [self.points_list[i * 2 + 1]]
                                self.ytterpunkt_liste[0:0] = [self.points_list[i * 2]]
                            self.ytterpunkt_liste.append(self.points_list[i * 2])
                            self.ytterpunkt_liste.append(self.points_list[i * 2 + 1])

            print(self.ytterpunkt_liste)

            self.retnings_punkt_x = ((self.points_list_riktig_vei[0]-self.points_list_riktig_vei[-2])/2) + self.points_list_riktig_vei[-2]
            self.retnings_punkt_y = ((self.points_list_riktig_vei[1]-self.points_list_riktig_vei[-1])/2) + self.points_list_riktig_vei[-1]
            #self.AI_x = self.retnings_punkt_x
            #self.AI_y = self.retnings_punkt_y
            self.tegn_vei = True
            self.beregn_vei = False

        if self.pause == False:
            if self.beregn:
                #self.x = self.sprite2._get_center_x()
                #self.y = self.sprite2._get_center_y()
                mulige_veier = []
                #print(0, mulige_veier, self.a)
                #print(00, self.sprite2._get_center_x(), self.sprite2._get_center_y())
                #print(3232, arcade.get_pixel(self.x, self.y - 16), arcade.get_pixel(self.x, self.y + 16), arcade.color.BROWN)

                if arcade.get_pixel((self.x + 16), self.y) == arcade.color.BROWN:
                    if arcade.get_pixel((self.x + 16), (self.y + 14)) == arcade.color.BROWN and arcade.get_pixel((self.x + 16), (self.y - 14)) == arcade.color.BROWN:
                        mulige_veier.append(1)
                if arcade.get_pixel((self.x - 16), self.y) == arcade.color.BROWN:
                    if arcade.get_pixel((self.x - 16), (self.y + 14)) == arcade.color.BROWN and arcade.get_pixel((self.x - 16), (self.y - 14)) == arcade.color.BROWN:
                        mulige_veier.append(2)
                if arcade.get_pixel(self.x, (self.y + 16)) == arcade.color.BROWN:
                    if arcade.get_pixel((self.x + 14), (self.y + 16)) == arcade.color.BROWN and arcade.get_pixel((self.x - 14), (self.y + 16)) == arcade.color.BROWN:
                        mulige_veier.append(3)
                if arcade.get_pixel(self.x, (self.y - 16)) == arcade.color.BROWN:
                    if arcade.get_pixel((self.x + 14), (self.y - 16)) == arcade.color.BROWN and arcade.get_pixel((self.x - 14), (self.y - 16)) == arcade.color.BROWN:
                        mulige_veier.append(4)
                #print(1, mulige_veier, self.a)
                try:
                    if len(mulige_veier) != 1:
                        if self.a == 1:
                            mulige_veier.remove(2)
                        if self.a == 2:
                            mulige_veier.remove(1)
                        if self.a == 3:
                            mulige_veier.remove(4)
                        if self.a == 4:
                            mulige_veier.remove(3)
                except:
                    pass
                print(2, mulige_veier, self.a)
                print(self.x, self.y, arcade.color.BROWN, arcade.get_pixel(self.x + 16, self.y + 14))
                print(self.x, self.y, arcade.color.BROWN, arcade.get_pixel(self.x + 14, self.y + 16))
                self.a = random.choice(mulige_veier)
                print(3, mulige_veier, self.a)
                if self.a == 1:
                    self.end_x += 16
                    self.sprite2.angle = 0
                elif self.a == 2:
                    self.sprite2.angle = 180
                    self.end_x -= 16
                elif self.a == 3:
                    self.end_y += 16
                elif self.a == 4:
                    self.end_y -= 16
                #self.sprite2.set_position(self.x, self.y)
                #print(11, self.end_x, self.end_y)

                self.run = True
                self.beregn = False

            if self.run:
                """
                self.endring1_x = self.end_x - self.x
                self.endring1_y = self.end_y - self.y
    
                d = math.sqrt(((2 * 2) + 15) / (self.endring1_x ** 2 + self.endring1_y ** 2))
    
                self.fart_x = self.endring1_x * d
                self.fart_y = self.endring1_y * d
    
                self.x = self.x + self.fart_x
                self.y = self.y + self.fart_y
                """
                self.override = False

                if self.a == 1:
                    if arcade.get_pixel((self.x + 15), self.y) == arcade.color.BROWN:
                        self.x += 1
                    else:
                        self.override = True
                if self.a == 2:
                    if arcade.get_pixel((self.x - 15), self.y) == arcade.color.BROWN:
                        self.x -= 1
                    else:
                        self.override = True
                if self.a == 3:
                    if arcade.get_pixel(self.x, (self.y + 15)) == arcade.color.BROWN:
                        self.y += 1
                    else:
                        self.override = True
                if self.a == 4:
                    if arcade.get_pixel(self.x, (self.y - 15)) == arcade.color.BROWN:
                        self.y -= 1
                    else:
                        self.override = True
                #print(22, self.x, self.y)
                self.sprite2.set_position(self.x, self.y)
                if self.end_x == self.x and self.end_y == self.y:
                    #print("kjørr")
                    self.beregn = True
                    self.run = False
                if self.override:
                    #print("OVERRIDE")
                    self.end_x = self.x
                    self.end_y = self.y
                    self.beregn = True
                    self.run = False

                if arcade.get_distance_between_sprites(self.sprite, self.sprite2) < 50:
                    self.game_over = True
                    self.run = False
                    self.beregn = False

            if self.go:
                #print(self.x, self.y)
                self.new_x = [self.x+1, self.y]
                self.new_xn = [self.x-1, self.y]
                self.new_y = [self.x, self.y+1]
                self.new_yn = [self.x, self.y-1]
                mulige_veier2 = []
                for i in range(0, len(self.pixel_list)):
                    #print(self.pixel_list)
                    if self.new_x == self.pixel_list[i]:
                        #print(1)
                        mulige_veier2.append(1)
                    if self.new_xn == self.pixel_list[i]:
                        #print(2)
                        mulige_veier2.append(2)
                    if self.new_y == self.pixel_list[i]:
                        #print(3)
                        mulige_veier2.append(3)
                    if self.new_yn == self.pixel_list[i]:
                        #print(4)
                        mulige_veier2.append(4)
                #if len(mulige_veier2) > 2:
                #    print(000, mulige_veier2, self.b)

                try:
                    if len(mulige_veier2) != 1:
                        if self.b == 1:
                            mulige_veier2.remove(2)
                        if self.b == 2:
                            mulige_veier2.remove(1)
                        if self.b == 3:
                            mulige_veier2.remove(4)
                        if self.b == 4:
                            mulige_veier2.remove(3)
                except:
                    pass
                self.b = random.choice(mulige_veier2)
                if len(mulige_veier2) > 1:
                    print(111, mulige_veier2, self.b)

                if self.b == 1:
                    self.x += 1
                if self.b == 2:
                    self.x -= 1
                if self.b == 3:
                    self.y += 1
                if self.b == 4:
                    self.y -= 1

                self.sprite2.set_position(self.x, self.y)


    def on_mouse_motion(self, x, y, dx, dy):
        self.target_x = x
        self.target_y = y
        # print(x, y)

    def on_key_press(self, symbol, modifiers):  # 224 144 245 122 test 143.86342439892263 226 test 119.59591794226543 248
        if symbol == arcade.key.RIGHT:
            if self.up == False and self.left == False and self.down == False:
                print("Right")
                self.right = True
        if symbol == arcade.key.LEFT:
            if self.right == False and self.up == False and self.down == False:
                print("left")
                self.left = True
        if symbol == arcade.key.UP:
            if self.right == False and self.left == False and self.down == False:
                print("up")
                self.up = True
        if symbol == arcade.key.DOWN:
            if self.right == False and self.left == False and self.up == False:
                print("down")
                self.down = True

        if symbol == arcade.key.ESCAPE:
            arcade.close_window()

        if symbol == arcade.key.ENTER:
            #self.beregn_vei = True
            self.player_x = 200
            self.player_y = 100
            self.sprite2.set_position(self.player_x, self.player_y)
            self.sprite.set_position(self.player_x, self.player_y)
            self.shape_list = None
            self.shape_list = arcade.ShapeElementList()
            self.x = self.player_x
            self.y = self.player_y
            self.end_x = self.x
            self.end_y = self.y
            self.run = False
            self.beregn = False
            self.game_over = False
            self.win = False

        if symbol == arcade.key.SPACE:
            self.beregn = True

        if symbol == arcade.key.P:
            if self.pause == False:
                self.pause = True
                print("PAUSE")
            elif self.pause:
                self.pause = False
                print("IKKE PAUSE")

        if symbol == arcade.key.TAB:
            self.go = True

        if symbol == arcade.key.O:
            print(self.pixel_list)

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
