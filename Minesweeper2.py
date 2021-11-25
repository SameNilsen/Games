from selenium import webdriver  # https://selenium-python.readthedocs.io/navigating.html
from time import sleep
import random
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.get('https://minesweeperonline.com/')
#actionChains = ActionChains(driver)
#driver.maximize_window()

sleep(1)

bomb_list = []
koordinater = []

for y in range(1, 17):
    bomb_list.append([])
    koordinater.append([])
    for x in range(1, 31):
        bomb_list[y-1].append(f'none')
        koordinater[y-1].append([y, x])

print(bomb_list)
print(koordinater)

start = driver.find_element_by_id('8_15')
start.click()

print(start.get_attribute('class'))

bomb_1 = driver.find_element_by_id('mines_ones')
bomb_10 = driver.find_element_by_id('mines_tens')
bomb_100 = driver.find_element_by_id('mines_hundreds')
total_mines = int(bomb_1.get_attribute('class')[-1] + bomb_10.get_attribute('class')[-1] + bomb_100.get_attribute('class')[-1])

current_x = 15
current_y = 8
retning = 'right'
last_move = 'right'
retning_list_x = ['right', 'left']
retning_list_y = ['down', 'up']
sleep(5)
while total_mines > 1:
    #sleep(2)
    print(current_y, current_x)
    check1 = driver.find_element_by_id(f'{current_y}_{current_x}')
    bomb_list[current_y-1][current_x-1] = check1.get_attribute('class')

    if check1.get_attribute('class')[0:-1] == 'square open' and check1.get_attribute('class')[-1] != '0':
        print("---")
        #print('y x:', y, x, 'bombnumber:', check1.get_attribute('class')[-1])
        number_of_possible = 0
        flagged = 0
        for y1 in range(current_y - 1, current_y + 2):
            for x1 in range(current_x - 1, current_x + 2):
                check2 = driver.find_element_by_id(f'{y1}_{x1}')
                if y1 != 0 and y1 != 17 and x1 != 0 and x1 != 31:
                    if check2.get_attribute('class') == 'square blank':
                        number_of_possible += 1
                    elif check2.get_attribute('class') == 'square bombflagged':
                        flagged += 1
        print('pos:', number_of_possible, 'flag:', flagged)
        print("::::", int(check1.get_attribute('class')[-1]), "vs number of possible:", number_of_possible)
        if number_of_possible <= int(check1.get_attribute('class')[-1]) - flagged:
            for y1 in range(current_y - 1, current_y + 2):
                for x1 in range(current_x - 1, current_x + 2):
                    check2 = driver.find_element_by_id(f'{y1}_{x1}')
                    if y1 != 0 and y1 != 17 and x1 != 0 and x1 != 31:
                        if check2.get_attribute('class') == 'square blank':
                            print("y1 x1:", y1, x1)
                            actionChains = ActionChains(driver)
                            actionChains.context_click(check2)
                            actionChains.perform()
                            flagged += 1
                            print("flag")
        if flagged >= int(check1.get_attribute('class')[-1]):
            print(2)
            for y1 in range(current_y - 1, current_y + 2):
                for x1 in range(current_x - 1, current_x + 2):
                    check2 = driver.find_element_by_id(f'{y1}_{x1}')
                    if y1 != 0 and y1 != 17 and x1 != 0 and x1 != 31:
                        if check2.get_attribute('class') == 'square blank':
                            print("y1 x1:", y1, x1)
                            check2.click()
                            print("clear")

    check_right = driver.find_element_by_id(f'{current_y}_{current_x+1}')
    check_down = driver.find_element_by_id(f'{current_y+1}_{current_x}')
    check_left = driver.find_element_by_id(f'{current_y}_{current_x-1}')
    check_up = driver.find_element_by_id(f'{current_y-1}_{current_x}')
    loop_counter = 0
    while True:
        if loop_counter > 5:
            current_x += 1
            break
        if retning == 'right':
            if current_x != 1 and current_x != 30 and current_y != 1 and current_y != 16:
                if check_right.get_attribute('class')[0:-1] == 'square open' and check_right.get_attribute('class')[-1] != '0':
                    last_move = 'right'
                    current_x += 1
                    break
                else:
                    if last_move == 'up':
                        retning = random.choice(retning_list_x)
                    else:
                        #retning = 'down'
                        retning = random.choice(retning_list_y)
            else:
                if check_right.get_attribute('class')[0:-1] == 'square open':
                    current_x += 1
                    break
                else:
                    if last_move == 'up':
                        retning = random.choice(retning_list_x)
                    else:
                        retning = random.choice(retning_list_y)
        if retning == 'down':
            if current_x != 1 and current_x != 30 and current_y != 1 and current_y != 16:
                if check_down.get_attribute('class')[0:-1] == 'square open' and check_down.get_attribute('class')[-1] != '0':
                    last_move = 'down'
                    current_y += 1
                    break
                else:
                    if last_move == 'right':
                        print("RANDOM")
                        retning = random.choice(retning_list_y)
                    else:
                        #retning = 'left'
                        retning = random.choice(retning_list_x)
            else:
                if check_down.get_attribute('class')[0:-1] == 'square open':
                    current_y += 1
                    break
                else:
                    if last_move == 'right':
                        retning = random.choice(retning_list_y)
                    else:
                        retning = random.choice(retning_list_x)
        if retning == 'left':
            if current_x != 1 and current_x != 30 and current_y != 1 and current_y != 16:
                if check_left.get_attribute('class')[0:-1] == 'square open' and check_left.get_attribute('class')[-1] != '0':
                    last_move = 'left'
                    current_x -= 1
                    break
                else:
                    if last_move == 'down':
                        retning = random.choice(retning_list_x)
                    else:
                        #retning = 'up'
                        retning = random.choice(retning_list_y)
            else:
                if check_left.get_attribute('class')[0:-1] == 'square open':
                    current_x -= 1
                    break
                else:
                    if last_move == 'down':
                        retning = random.choice(retning_list_x)
                    else:
                        retning = random.choice(retning_list_y)
        if retning == 'up':
            if current_x != 1 and current_x != 30 and current_y != 1 and current_y != 16:
                if check_up.get_attribute('class')[0:-1] == 'square open' and check_up.get_attribute('class')[-1] != '0':
                    last_move = 'up'
                    current_y -= 1
                    break
                else:
                    if last_move == 'left':
                        retning = random.choice(retning_list_y)
                    else:
                        #retning = 'right'
                        retning = random.choice(retning_list_x)
            else:
                if check_up.get_attribute('class')[0:-1] == 'square open':
                    current_y -= 1
                    break
                else:
                    if last_move == 'left':
                        retning = random.choice(retning_list_y)
                    else:
                        retning = random.choice(retning_list_x)
        loop_counter += 1

"""
while total_mines > 1:
    for y in range(1, 17):
        for x in range(1, 31):
            print(y, x)
            #actionChains = ActionChains(driver)
            check1 = driver.find_element_by_id(f'{y}_{x}')
            #actionChains.move_to_element(check1)
            #actionChains.send_keys(Keys.SPACE)
            #actionChains.context_click(check1)
            #actionChains.perform()
            #actionChains.reset_actions()
            #check1.send_keys(Keys.SPACE)
            #actionChains.release(check1)
            if check1.get_attribute('class')[0:-1] == 'square open' and check1.get_attribute('class')[-1] != '0':
                print("---")
                print('y x:', y, x, 'bombnumber:', check1.get_attribute('class')[-1])
                number_of_possible = 0
                flagged = 0
                for y1 in range(y - 1, y + 2):
                    for x1 in range(x - 1, x + 2):
                        check2 = driver.find_element_by_id(f'{y1}_{x1}')
                        if y1 != 0 and y1 != 17 and x1 != 0 and x1 != 31:
                            if check2.get_attribute('class') == 'square blank':
                                number_of_possible += 1
                            elif check2.get_attribute('class') == 'square bombflagged':
                                flagged += 1
                print('pos:', number_of_possible, 'flag:', flagged)
                print("::::", int(check1.get_attribute('class')[-1]), "vs number of possible:", number_of_possible)
                if number_of_possible <= int(check1.get_attribute('class')[-1]) - flagged:
                    for y1 in range(y - 1, y + 2):
                        for x1 in range(x - 1, x + 2):
                            check2 = driver.find_element_by_id(f'{y1}_{x1}')
                            if y1 != 0 and y1 != 17 and x1 != 0 and x1 != 31:
                                if check2.get_attribute('class') == 'square blank':
                                    print("y1 x1:", y1, x1)
                                    actionChains = ActionChains(driver)
                                    actionChains.context_click(check2)
                                    actionChains.perform()
                                    flagged += 1
                                    print("flag")
                if flagged >= int(check1.get_attribute('class')[-1]):
                    print(2)
                    for y1 in range(y - 1, y + 2):
                        for x1 in range(x - 1, x + 2):
                            check2 = driver.find_element_by_id(f'{y1}_{x1}')
                            if y1 != 0 and y1 != 17 and x1 != 0 and x1 != 31:
                                if check2.get_attribute('class') == 'square blank':
                                    print("y1 x1:", y1, x1)
                                    check2.click()
                                    print("clear")
                print("---")

# legg alle tall i liste med antall bomber i paralell liste. Avanserte løsninger

sleep(5)
driver.quit()
print("end...")
"""
