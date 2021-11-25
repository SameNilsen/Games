from selenium import webdriver  # https://selenium-python.readthedocs.io/navigating.html
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

data = open("Export_Minesweeper.txt", 'r')
check = data.readline()

print(check)

bomb_list = []

check2 = data.readline()
print(check2)
bomb_list.append(check2.split('o'))
print(bomb_list)
for i in range(0, len(bomb_list[0])):
    bomb_list[0][i] = bomb_list[0][i].split(',')
    #print(bomb_list)
    bomb_list[0][i][0] = int(bomb_list[0][i][0])
    bomb_list[0][i][1] = int(bomb_list[0][i][1])
bomb_list = bomb_list[0]
print(bomb_list)


driver = webdriver.Chrome()
driver.get('https://minesweeperonline.com/')
#actionChains = ActionChains(driver)
#driver.maximize_window()

sleep(1)

start = driver.find_element_by_id(f'import-link')
start.click()

Import = driver.find_element_by_xpath('//*[@id="import"]/tbody/tr[2]/td/textarea')
Import.send_keys(check)

load_game = driver.find_element_by_xpath('//*[@id="import"]/tbody/tr[3]/td/input')
load_game.click()

for i in range(0, len(bomb_list)):
    y1 = bomb_list[i][0]
    x1 = bomb_list[i][1]
    check3 = driver.find_element_by_id(f'{y1}_{x1}')
    actionChains = ActionChains(driver)
    actionChains.context_click(check3)
    actionChains.perform()

for i in range(1, 17):
    for o in range(1, 31):
        check4 = driver.find_element_by_id(f'{i}_{o}')
        check4.click()
        #print(i, o)

#start = driver.find_element_by_id(f'{y}_{x}')
#start.click()

game_over = driver.find_element_by_id('face')
actionChains = ActionChains(driver)
