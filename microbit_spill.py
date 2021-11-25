# Add your Python code here. E.g.
from microbit import *
import random

dot_string = "00900:00000:00000:00000:00009"
bottom_list = ["90000", "09000", "00900", "00090", "00009"]
random_start = bottom_list
dot = Image(dot_string)
current_dot = 0
current_position = 4
score = -1
speed = 500
game_over = False

while True:
    if game_over is False:
        display.show(dot)
        sleep(speed)
        
        dot_string = dot_string.split(":")
        
        if current_dot == 3:
            if dot_string[3] != bottom_list[current_position]:
                game_over = True
        
        if button_a.was_pressed():
            dot_string = dot_string[:-1]
            if current_position > 0:
                current_position -= 1
                dot_string.append(bottom_list[current_position])
            else:
                current_position = 4
                dot_string.append(bottom_list[current_position])
        if button_b.was_pressed():
            dot_string = dot_string[:-1]
            if current_position < 4:
                current_position += 1
                dot_string.append(bottom_list[current_position])
            else:
                current_position = 0
                dot_string.append(bottom_list[current_position])
        
        if current_dot == 3:
            dot_string[0] = random_start[random.randint(0, 4)]
            dot_string[3] = dot_string[2]
            current_dot = 0
            score += 1
            speed -= 10
        else:
            dot_string[current_dot+1] = dot_string[current_dot]
            dot_string[current_dot] = "00000"
            current_dot += 1
        dot_string = str(dot_string[0]+":"+dot_string[1]+":"+dot_string[2]+":"+dot_string[3]+":"+dot_string[4])
        dot = Image(dot_string)
    else:
        display.scroll("GAME OVER! SCORE:")
        display.scroll(score)
        while True:
            display.show("A")
            if button_a.is_pressed():
                current_dot = 0
                current_position = 4
                score = -1
                speed = 500
                dot_string = "00900:00000:00000:00000:00009"
                dot = Image(dot_string)
                game_over = False
                break

