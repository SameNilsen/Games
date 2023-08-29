import arcade
import math
import random

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
VIEWPORT_MARGIN = 40


class MyGameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title, resizable=False)

        self.sprite_list = None
        self.sprite_list = arcade.SpriteList()

        self.pause_tiles_sprite_list = None
        self.pause_tiles_sprite_list = arcade.SpriteList()

        self.shape_list = None
        self.shape_list = arcade.ShapeElementList()

        # self.sprite = arcade.Sprite("Sprite/ShrekIMG5.png", center_x=100, center_y=100, scale=0.1)
        # self.x = 0
        # self.y = 0
        # self.sprite.set_position(self.x, self.y)

        # self.sprite_list.append(self.sprite)

        self.sprite2 = arcade.Sprite("Sprite/BaseTile.png", center_x=100, center_y=100, scale=0.7)
        self.player2_x = 200
        self.player2_y = 100
        self.player2_speed = 100
        self.sprite2.set_position(self.player2_x, self.player2_y)

        # self.sprite_list.append(self.sprite2)

        # random.shuffle(self.sprite_list)
        #u = 0
        #for tile in self.sprite_list:
        #    u += 1
        #    print(tile, u)

        self.up = False
        self.down = False
        self.right = False
        self.left = False

        self.view_bottom = 0
        self.view_left = 0

        self.total_time = 0.0

        self.border_x = self.width / 10
        self.border_y = self.height / 20

        for x in range(1, 6):
            line = arcade.create_line(self.width / 5 * x - self.border_x, self.border_y, self.width / 5 * x - self.border_x, self.height - self.border_y, arcade.color.DARK_RED, 2)
            self.shape_list.append(line)

        for y in range(1, 10):
            line = arcade.create_line(self.border_x, self.height / 9 * y - self.border_y, self.width - self.border_x, self.height / 9 * y - self.border_y, arcade.color.DARK_RED, 2)
            self.shape_list.append(line)

        data = open("Number_data.txt", 'r')
        #check = data.read()
        l = []
        check = data.read()
        print(len(check))
        if len(check) > 0:
            a = 0
            for x in range(0, len(check)):
                if check[x] != 'o':
                    if a == 0:
                        if check[x+1] != 'o':
                            l.append(int(check[x] + check[x+1]))
                        else:
                            if check[x] == '-':
                                l.append(check[x])
                            else:
                                l.append(int(check[x]))
                        a = 1
                else:
                    a = 0
            print(l, len(l))
        data.close()

        self.number_list = []
        self.number_index = 0
        self.blank_x = 1
        self.blank_y = 1
        for i in range(1, 32):
            self.number_list.append(i)
        self.number_list.append('-')
        random.shuffle(self.number_list)
        print(self.number_list)
        """
        for i in range(0, len(self.number_list)):
            n = self.number_list[i]
            if n == '-':
                tile = arcade.Sprite("Sprite/Tiles/Tile32.png", center_x=100, center_y=100, scale=0.7)
            else:
                tile = arcade.Sprite(f"Sprite/Tiles/Tile{n}.png", center_x=100, center_y=100, scale=0.7)
            self.sprite_list.append(tile)
        """
        for i in range(1, 33):
            tile = arcade.Sprite(f"Sprite/Tiles/Tile{i}.png", center_x=100, center_y=100, scale=0.7)
            self.sprite_list.append(tile)

        self.number_matrix = []
        a = 0
        for i in range(0, len(self.number_list), 4):
            self.number_matrix.append([])
            for o in range(0, 4):
                if len(check) > 0:
                    self.number_matrix[a].append(l[o+i])
                else:
                    self.number_matrix[a].append(self.number_list[o + i])
            a += 1
        print(self.number_matrix)

        self.square_x = self.width / 5 - self.border_x
        self.square_y = self.height / 9 - self.border_y

        self.slot_number_list = []
        for i in range(0, 32):
            self.slot_number_list.append(i)
        print(self.slot_number_list)

        self.move_up = False
        self.move_down = False
        self.move_right = False
        self.move_left = False

        self.current_slot_x = 1
        self.current_slot_y = 1
        self.current_slot_index = 0
        self.csax = 0
        self.csay = 0
        self.show_tiles = True

        self.pause = True

        # ( 400   ÷   2 )   -   ( 100   ×   0,7 )
        self.border_width = (self.width/2) - ((100*0.7)*2) + ((100*0.7)/2)
        self.standard_avstand = 100*0.7

        self.border_height = (self.height/2) - ((100*0.7)*4) + ((100*0.7)/2)

        for i in range(0, len(self.number_matrix)):
            for o in range(0, len(self.number_matrix[i])):
                # print("i:", i, "o:", o, ":::", (i*4)+o)
                c = self.number_matrix[i][o]
                #print(c)
                if c == '-':
                    self.sprite_list[-1].set_position(self.border_width + (self.standard_avstand*o), self.border_height + (self.standard_avstand*i))
                else:
                    self.sprite_list[c-1].set_position(self.border_width + (self.standard_avstand*o), self.border_height + (self.standard_avstand*i))

        #for i in range(0, 33):
            #self.sprite_list[self.number_matrix[i]-1].set_positon(self.width/5, self.height/9)
        if len(check) > 0:
            tile1 = arcade.Sprite(f"Sprite/New_button_tile.png", center_x=self.width/2, center_y=(self.height/2) + (100*0.7/2), scale=0.7)
            self.pause_tiles_sprite_list.append(tile1)
            tile2 = arcade.Sprite(f"Sprite/Continue_button_tile.png", center_x=self.width/2, center_y=(self.height/2) - (100*0.7/2), scale=0.7)
            self.pause_tiles_sprite_list.append(tile2)
        else:
            self.pause = False

    def on_resize(self, width, height):

        # Call the parent. Failing to do this will mess up the coordinates, and default to 0,0 at the center and the
        # edges being -1 to 1.
        super().on_resize(width, height)

        self.width = width
        self.height = height

        print(self.width, self.height)

    def on_draw(self):
        arcade.start_render()

        # arcade.draw_text(f"{self.target_x}, {self.target_y}", 50, self.height - 100, arcade.color.DARK_RED, 20)

        #self.shape_list.draw()

        #arcade.draw_point(self.width / 2, self.height / 2, arcade.color.RED, 5)

        # arcade.draw_text(f"{self.player2_x, self.player2_y}", 0, self.height-50, arcade.color.DARK_RED)
        #arcade.draw_text(f"{self.x, self.y}", 0, self.height - 100, arcade.color.DARK_RED)
        # arcade.draw_text(f"view_bottom:{self.view_bottom}", 0, self.height - 150, arcade.color.DARK_RED)
        # arcade.draw_text(f"top_bndry{self.top_bndry}", 0, self.height - 200, arcade.color.DARK_RED)

        """
        for i in range(1, 9):
            for o in range(1, 5):
                #arcade.draw_text(f"{self.number_list[self.number_index]}", self.width/5 * o, self.height/9 * i, arcade.color.GOLD)
                if self.number_index < 31:
                    self.number_index += 1
        self.number_index = 0
        """
        if self.show_tiles:
            self.sprite_list.draw()
        else:
            arcade.draw_xywh_rectangle_filled(self.square_x, self.square_y, self.width / 5, self.height / 9, arcade.color.DARK_CYAN)
            for i in range(0, len(self.number_matrix)):
                for o in range(0, len(self.number_matrix[i])):
                    arcade.draw_text(f"{self.number_matrix[i][o]}", self.width/5 * (o+1), self.height/9 * (i+1), arcade.color.GOLD)

        if self.pause:
            if len(self.pause_tiles_sprite_list) < 2:
                tile1 = arcade.Sprite(f"Sprite/New_button_tile.png", center_x=self.width / 2, center_y=(self.height / 2) + (100 * 0.7 / 2), scale=0.7)
                self.pause_tiles_sprite_list.append(tile1)
                tile2 = arcade.Sprite(f"Sprite/Continue_button_tile.png", center_x=self.width / 2, center_y=(self.height / 2) - (100 * 0.7 / 2), scale=0.7)
                self.pause_tiles_sprite_list.append(tile2)
            self.pause_tiles_sprite_list.draw()

    def on_update(self, delta_time):

        if self.right:
            self.player2_x += self.player2_speed * delta_time
        if self.left:
            self.player2_x -= self.player2_speed * delta_time
        if self.up:
            self.player2_y += self.player2_speed * delta_time
        if self.down:
            self.player2_y -= self.player2_speed * delta_time

        self.sprite2.set_position(self.width / 5 * 3, self.height / 9 * 4)

        if self.pause:
            for i in range(0, 32):
                self.sprite_list[i].alpha = 100
        else:
            for i in range(0, 32):
                self.sprite_list[i].alpha = 255

        if self.move_up:
            print(self.square_x / (self.width / 5 - self.border_x), self.square_y / (self.height / 9 - self.border_y))
            #self.current_slot_x = int(self.square_x / (self.width / 5 - self.border_x) - self.csax)
            #self.current_slot_y = round(self.square_y / (self.height / 9 - self.border_y) - self.csay)
            print("x:", self.current_slot_x, "y:", self.current_slot_y)
            self.current_slot_index = self.current_slot_x * self.current_slot_y
            print("self.current_slot_index:", self.current_slot_index, ",", self.number_list[self.current_slot_index])

            # for i in range(1, 9-self.current_slot_y):
            # print(self.number_list[(self.current_slot_y+3)*i])

            # for i in range(7, self.current_slot_y-1, -1):
            # print(self.number_matrix[i][self.current_slot_x-1])
            # I tillegg til å bytte ut i number matrix, endrer man posisjon på tiles i spritelist
            # hvis flytte 28, set position på index nummer 28
            for i in range(0, 8 - self.current_slot_y):
                print(self.number_matrix[self.current_slot_y + i][self.current_slot_x - 1])
                if (self.number_matrix[self.current_slot_y + i][self.current_slot_x - 1]) == "-":
                    blank_y = self.current_slot_y + i + 1
                    blank_x = self.current_slot_x
                    print("blank_y:", blank_y, "blank_x:", blank_x)
                    print("ålø")

                    #a = ((blank_y-1)*4)+(blank_x-1)
                    #self.sprite_list[a].set_position(self.width/5 * self.current_slot_x, self.height/9 * self.current_slot_y)
                    # bytt plass på blank og current slot x og y :) B) BD :D :P BP
                    for o in range(0, blank_y - self.current_slot_y):
                        d = self.number_matrix[blank_y - 2 - o][self.current_slot_x - 1]
                        print("d:", d)
                        self.sprite_list[d - 1].set_position(self.border_width + (self.standard_avstand * (self.current_slot_x-1)), self.border_height + (self.standard_avstand * (blank_y - o-1)))
                        #b = ((self.current_slot_y - 1 + o) * 4) + (self.current_slot_x - 1)
                        #print("-------", b, self.width/5 * self.current_slot_x, self.height/9 * self.current_slot_y * (o+1))
                        #self.sprite_list[b].set_position(self.width/5 * self.current_slot_x, self.height/9 * (self.current_slot_y+o+1))
                        self.number_matrix[self.current_slot_y + i - o][self.current_slot_x - 1] = self.number_matrix[self.current_slot_y + i - o - 1][self.current_slot_x - 1]
                    self.number_matrix[self.current_slot_y - 1][self.current_slot_x - 1] = "-"
                    self.sprite_list[-1].set_position(self.border_width + (self.standard_avstand * (self.current_slot_x-1)), self.border_height + (self.standard_avstand * (self.current_slot_y-1)))
                    break

            self.move_up = False

        if self.move_down:
            print(self.square_x / (self.width / 5 - self.border_x), self.square_y / (self.height / 9 - self.border_y))
            #self.current_slot_x = int(self.square_x / (self.width / 5 - self.border_x) - self.csax)
            #self.current_slot_y = round(self.square_y / (self.height / 9 - self.border_y) - self.csay)
            print("x:", self.current_slot_x, "y:", self.current_slot_y)
            self.current_slot_index = self.current_slot_x * self.current_slot_y
            # print("self.current_slot_index:", self.current_slot_index, ",", self.number_list[self.current_slot_index])

            # for i in range(1, 9-self.current_slot_y):
            # print(self.number_list[(self.current_slot_y+3)*i])

            # for i in range(7, self.current_slot_y-1, -1):
            # print(self.number_matrix[i][self.current_slot_x-1])

            for i in range(0, self.current_slot_y):
                # print("i:", i, "self.currentsloty:", self.current_slot_y)
                print(self.number_matrix[self.current_slot_y - 1 - i][self.current_slot_x - 1])
                if (self.number_matrix[self.current_slot_y - 1 - i][self.current_slot_x - 1]) == "-":
                    blank_y = self.current_slot_y - i
                    blank_x = self.current_slot_x
                    print("blank_y:", blank_y)
                    print("ålø")
                    # bytt plass på blank og current slot x og y :) B) BD :D :P BP
                    for o in range(blank_y, self.current_slot_y):
                        d = self.number_matrix[o][self.current_slot_x - 1]
                        print("d:", d)
                        self.sprite_list[d - 1].set_position(self.border_width + (self.standard_avstand * (self.current_slot_x-1)), self.border_height + (self.standard_avstand * (o-1)))
                        self.number_matrix[o - 1][self.current_slot_x - 1] = self.number_matrix[o][self.current_slot_x - 1]
                    self.number_matrix[self.current_slot_y - 1][self.current_slot_x - 1] = "-"
                    self.sprite_list[-1].set_position(self.border_width + (self.standard_avstand * (self.current_slot_x-1)), self.border_height + (self.standard_avstand * (self.current_slot_y-1)))
                    break

            self.move_down = False

        if self.move_right:
            print(self.square_x / (self.width / 5 - self.border_x), self.square_y / (self.height / 9 - self.border_y))
            #self.current_slot_x = int(self.square_x / (self.width / 5 - self.border_x) - self.csax)
            #self.current_slot_y = round(self.square_y / (self.height / 9 - self.border_y) - self.csay)
            print("x:", self.current_slot_x, "y:", self.current_slot_y)
            self.current_slot_index = self.current_slot_x * self.current_slot_y
            # print("self.current_slot_index:", self.current_slot_index, ",", self.number_list[self.current_slot_index])

            # for i in range(1, 9-self.current_slot_y):
            # print(self.number_list[(self.current_slot_y+3)*i])

            # for i in range(7, self.current_slot_y-1, -1):
            # print(self.number_matrix[i][self.current_slot_x-1])

            for i in range(0, 4 - self.current_slot_x):
                # print("i:", i, "self.currentsloty:", self.current_slot_y)
                print(self.number_matrix[self.current_slot_y - 1][self.current_slot_x + i])
                if (self.number_matrix[self.current_slot_y - 1][self.current_slot_x + i]) == "-":
                    blank_x = self.current_slot_x + i + 1
                    print("blank_x:", blank_x)
                    print("ålø")
                    # bytt plass på blank og current slot x og y :) B) BD :D :P BP
                    for o in range(0, blank_x - self.current_slot_x):
                        d = self.number_matrix[self.current_slot_y-1][blank_x-2-o]
                        print("d:", d)
                        self.sprite_list[d - 1].set_position(self.border_width + (self.standard_avstand * (blank_x - o-1)), self.border_height + (self.standard_avstand * (self.current_slot_y - 1)))
                        self.number_matrix[self.current_slot_y - 1][self.current_slot_x + i - o] = self.number_matrix[self.current_slot_y - 1][self.current_slot_x + i - o - 1]
                    self.number_matrix[self.current_slot_y - 1][self.current_slot_x - 1] = "-"
                    self.sprite_list[-1].set_position(self.border_width + (self.standard_avstand * (self.current_slot_x - 1)), self.border_height + (self.standard_avstand * (self.current_slot_y - 1)))
                    break

            self.move_right = False

        if self.move_left:
            print(self.square_x / (self.width / 5 - self.border_x), self.square_y / (self.height / 9 - self.border_y))
            #self.current_slot_x = int(self.square_x / (self.width / 5 - self.border_x) - self.csax)
            #self.current_slot_y = round(self.square_y / (self.height / 9 - self.border_y) - self.csay)
            print("x:", self.current_slot_x, "y:", self.current_slot_y)
            self.current_slot_index = self.current_slot_x * self.current_slot_y
            # print("self.current_slot_index:", self.current_slot_index, ",", self.number_list[self.current_slot_index])

            # for i in range(1, 9-self.current_slot_y):
            # print(self.number_list[(self.current_slot_y+3)*i])

            # for i in range(7, self.current_slot_y-1, -1):
            # print(self.number_matrix[i][self.current_slot_x-1])

            for i in range(0, self.current_slot_x):
                # print("i:", i, "self.currentsloty:", self.current_slot_y)
                print(self.number_matrix[self.current_slot_y - 1][self.current_slot_x - 1 - i])
                if (self.number_matrix[self.current_slot_y - 1][self.current_slot_x - 1 - i]) == "-":
                    blank_x = self.current_slot_x - i
                    print("blank_x:", blank_x)
                    print("ålø")
                    # bytt plass på blank og current slot x og y :) B) BD :D :P BP
                    for o in range(blank_x, self.current_slot_x):
                        d = self.number_matrix[self.current_slot_y - 1][o]
                        print("d:", d)
                        self.sprite_list[d - 1].set_position(self.border_width + (self.standard_avstand * (o-1)), self.border_height + (self.standard_avstand * (self.current_slot_y - 1)))
                        self.number_matrix[self.current_slot_y - 1][o - 1] = self.number_matrix[self.current_slot_y - 1][o]
                    self.number_matrix[self.current_slot_y - 1][self.current_slot_x - 1] = "-"
                    self.sprite_list[-1].set_position(self.border_width + (self.standard_avstand * (self.current_slot_x - 1)), self.border_height + (self.standard_avstand * (self.current_slot_y - 1)))
                    break

            self.move_left = False

        #self.sprite_list_test[(i*4)+o].set_position(self.width/5 * (o+1), self.height/9 * (i+1))
        # Lag for de tre andre retningene også :D
        # Tegn og lag hvite/røde firkanter for hvert tall (sprites)

        # 1.81818181818

        # Sjekk om vunnet: self.number_matrix == self.vinnerliste:
        changed = False

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

        # Scroll up
        self.top_bndry = self.view_bottom + self.height - VIEWPORT_MARGIN
        if self.sprite2.top > self.top_bndry:
            self.view_bottom += self.sprite2.top - self.top_bndry
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

        if self.pause is False:
            print(self.y)
            mus_y = (self.y-20)//70 + 1
            print("a:", mus_y)

            mus_x = (self.x-60)//70 + 1
            print("b", mus_x)

            blank_x = (self.sprite_list[-1]._get_center_x()-60)//70 + 1
            blank_y = (self.sprite_list[-1]._get_center_y()-20)//70 + 1

            self.current_slot_x = mus_x
            self.current_slot_y = mus_y

            print("blank x og y:", blank_x, blank_y)

            if 1 <= mus_x <= 4 and 1 <= mus_y <= 8:
                if mus_x == blank_x:
                    if mus_y - blank_y > 0:
                        print("NED")
                        self.move_down = True
                    elif mus_y - blank_y < 0:
                        print("OPP")
                        self.move_up = True
                elif mus_y == blank_y:
                    if mus_x - blank_x > 0:
                        print("VENSTRE")
                        self.move_left = True
                    elif mus_x - blank_x < 0:
                        print("HØYRE")
                        self.move_right = True
            else:
                if len(self.pause_tiles_sprite_list) < 3:
                    tile3 = arcade.Sprite(f"Sprite/Save_button_tile.png", center_x=self.width / 2, center_y=(self.height / 2) - ((100 * 0.7 / 2)*3), scale=0.7)
                    self.pause_tiles_sprite_list.append(tile3)
                self.pause = True
        else:
            print(self.y)
            mus_y = (self.y - 20) // 70 + 1
            print("a:", mus_y)
            mus_x = (self.x - 60) // 70 + 1
            print("b", mus_x)

            if mus_y == 4:
                if mus_x == 2 or mus_x == 3:
                    print("Load")
                    self.pause = False
            elif mus_y == 5:
                if mus_x == 2 or mus_x == 3:
                    print("NEW")
                    random.shuffle(self.number_list)
                    self.number_matrix = []
                    a = 0
                    for i in range(0, len(self.number_list), 4):
                        self.number_matrix.append([])
                        for o in range(0, 4):
                            self.number_matrix[a].append(self.number_list[o + i])
                        a += 1
                    print(self.number_matrix)
                    for i in range(0, len(self.number_matrix)):
                        for o in range(0, len(self.number_matrix[i])):
                            c = self.number_matrix[i][o]
                            if c == '-':
                                self.sprite_list[-1].set_position(self.border_width + (self.standard_avstand * o), self.border_height + (self.standard_avstand * i))
                            else:
                                self.sprite_list[c - 1].set_position(self.border_width + (self.standard_avstand * o), self.border_height + (self.standard_avstand * i))
                    self.pause = False
            elif mus_y == 3:
                if mus_x == 2 or mus_x == 3:
                    print("Save")
                    data = open("Number_data.txt", 'w')
                    for i in range(0, 8):
                        for o in range(0, 4):
                            data.write(str(self.number_matrix[i][o]) + 'o')
                    data.close()


    def on_key_press(self, symbol, modifiers):

        if self.pause is False:
            if symbol == arcade.key.D:
                if self.square_x < self.width / 5 * 4 - self.border_x:
                    self.square_x += self.width / 5
                    self.csax += 1
            if symbol == arcade.key.A:
                if self.square_x > self.width / 5 - self.border_x:
                    self.square_x -= self.width / 5
                    self.csax -= 1
            if symbol == arcade.key.W:
                if self.square_y < self.height / 9 * 8 - self.border_y:
                    self.square_y += self.height / 9
                    self.csay += 0.818181818181818
            if symbol == arcade.key.S:
                if self.square_y > self.height / 9 - self.border_y:
                    self.square_y -= self.height / 9
                    self.csay -= 0.818181818181818

            if symbol == arcade.key.UP:
                self.current_slot_x = int(self.square_x / (self.width / 5 - self.border_x) - self.csax)
                self.current_slot_y = round(self.square_y / (self.height / 9 - self.border_y) - self.csay)
                self.move_up = True
            if symbol == arcade.key.DOWN:
                self.current_slot_x = int(self.square_x / (self.width / 5 - self.border_x) - self.csax)
                self.current_slot_y = round(self.square_y / (self.height / 9 - self.border_y) - self.csay)
                self.move_down = True
            if symbol == arcade.key.RIGHT:
                self.current_slot_x = int(self.square_x / (self.width / 5 - self.border_x) - self.csax)
                self.current_slot_y = round(self.square_y / (self.height / 9 - self.border_y) - self.csay)
                self.move_right = True
            if symbol == arcade.key.LEFT:
                self.current_slot_x = int(self.square_x / (self.width / 5 - self.border_x) - self.csax)
                self.current_slot_y = round(self.square_y / (self.height / 9 - self.border_y) - self.csay)
                self.move_left = True

        if symbol == arcade.key.SPACE:
            # print(self.square_x, self.square_y)
            if self.show_tiles == False:
                self.show_tiles = True
            elif self.show_tiles:
                self.show_tiles = False

        if symbol == arcade.key.P:
            #self.sprite_list[-1].remove_from_sprite_lists()
            data = open("Number_data.txt", 'w')
            for i in range(0, 8):
                for o in range(0, 4):
                    data.write(str(self.number_matrix[i][o]) + 'o')
            data.close()

        if symbol == arcade.key.ENTER or symbol == arcade.key.ESCAPE:
            if self.pause is False:
                if len(self.pause_tiles_sprite_list) < 3:
                    tile3 = arcade.Sprite(f"Sprite/Save_button_tile.png", center_x=self.width / 2, center_y=(self.height / 2) - ((100 * 0.7 / 2)*3), scale=0.7)
                    self.pause_tiles_sprite_list.append(tile3)
                self.pause = True
            elif self.pause:
                self.pause = False

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
