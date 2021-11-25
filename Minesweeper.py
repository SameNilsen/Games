from selenium import webdriver  # https://selenium-python.readthedocs.io/navigating.html
from time import sleep
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

game_over = driver.find_element_by_id('face')

while True:
    for y in range(1, 4):
        for x in range(1, 4):
            start = driver.find_element_by_id(f'{y*4}_{x*8}')
            start.click()

    if game_over.get_attribute('class') == 'facesmile':
        break
    else:
        game_over.click()

#print(start.get_attribute('class'))

bomb_1 = driver.find_element_by_id('mines_ones')
bomb_10 = driver.find_element_by_id('mines_tens')
bomb_100 = driver.find_element_by_id('mines_hundreds')
total_mines = int(bomb_1.get_attribute('class')[-1] + bomb_10.get_attribute('class')[-1] + bomb_100.get_attribute('class')[-1])

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

bomb_list = []
koordinater = []

# legg alle tall i liste med antall bomber i paralell liste. Avanserte løsninger

sleep(5)
driver.quit()
print("end...")
