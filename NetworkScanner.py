from selenium import webdriver  # https://selenium-python.readthedocs.io/navigating.html
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('http://178.128.160.242:31908/')
window_before = driver.window_handles[0]
string = driver.find_element_by_xpath('/html/body/h3').text
print(string)
driver.execute_script("window.open('about:blank', 'tab2');")
driver.switch_to.window("tab2")
driver.get('http://www.md5.cz/')

a = driver.find_element_by_xpath('//*[@id="what"]')
a.send_keys(string)
b = driver.find_element_by_xpath('//*[@id="frm"]/p[2]/input')
b.click()
sleep(0.05)
c = driver.find_element_by_id('checksum').get_attribute('value')
print(c)
driver.switch_to.window(driver.window_handles[0])

d = driver.find_element_by_xpath('/html/body/center/form/input[1]')
d.send_keys(c)

e = driver.find_element_by_xpath('/html/body/center/form/input[2]')
e.click()

"""
import requests
import hashlib
import re



url="http://docker.hackthebox.eu:33205/"

r=requests.session()
out=r.get(url)
out=re.search("<h3 align='center'>+.*?</h3>",out.text)
out=re.search("'>.*<",out[0])
out=re.search("[^|'|>|<]...................",out[0])

out=hashlib.md5(out[0].encode('utf-8')).hexdigest()

print("sending md5 :-{}".format(out))

data={'hash': out}
out = r.post(url = url, data = data)

print(out.text)
"""

