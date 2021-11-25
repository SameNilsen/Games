from selenium import webdriver  # https://selenium-python.readthedocs.io/navigating.html
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

# sett inn sidenr på brettboka mellom knappene

driver = webdriver.Chrome()
driver.get('https://brettboka.no/user/publications/458')
driver.maximize_window()

sleep(1)

#driver.get_screenshot_as_file("ScreenshotTest1.png")
logg_inn = driver.find_element_by_xpath('//*[@id="app"]/div/main/div/div[2]/a')
logg_inn.click()

BrettBokaIkon = driver.find_element_by_xpath('//*[@id="app"]/div/main/section[1]/div/div/div[1]/button')
BrettBokaIkon.click()

username = driver.find_element_by_xpath('//*[@id="username"]')
username.send_keys('mort1.nilsen@gmail.com')

password = driver.find_element_by_xpath('//*[@id="password"]')
password.send_keys('Ssb3t4Ww')

logg_inn2 = driver.find_element_by_xpath('//*[@id="app"]/div/main/section[2]/div/div/form/button')
logg_inn2.click()

sleep(2)

sortereKnapp = driver.find_element_by_xpath('//*[@id="app"]/div/main/div[2]/button[2]')
sortereKnapp.click()

aqua1 = driver.find_element_by_xpath('//*[@id="app"]/div/main/div[1]/div/div[1]/a')
aqua1.click()

try:
    myElem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/main/section/div[1]/div[1]/input')))
    print("Page is ready!")
except TimeoutException:
    print("Loading took too much time!")

sideTall = driver.find_element_by_class_name("pageNumberField---Hrku5")
sideTall.clear()
sideTall.send_keys("1")
sideTall.send_keys(Keys.ENTER)
sleep(1)
driver.get_screenshot_as_file(f"AquaKjemi1/Side1.png")
for i in range(200, 315, 2):
    SideTall = driver.find_element_by_class_name("pageNumberField---Hrku5")
    SideTall.clear()
    SideTall.send_keys(f"{i}")
    SideTall.send_keys(Keys.ENTER)
    sleep(3)
    driver.get_screenshot_as_file(f"AquaKjemi1test/Side{i}-{i+1}.png")

sleep(5)
driver.quit()
print("end...")
