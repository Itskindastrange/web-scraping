from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time


PATH = "C:\\Program Files (x86)\\chromedriver.exe"
service = Service(executable_path=PATH)
driver = webdriver.Chrome(service=service)
driver.get("https://orteil.dashnet.org/cookieclicker/")
driver.implicitly_wait(15)
lang = driver.find_element(By.ID,'langSelect-EN')
lang.click()
driver.implicitly_wait(15)


cookie = driver.find_element(By.ID ,"bigCookie")
#cookie_count = driver.find_elements(By.ID,"cookies")

#items = [driver.find_element(By.ID,'productPrice' + str(i)) for i in range(1,-1,-1)]



for i in range(1000):
    actions = ActionChains(driver)
    actions.click(cookie)
    actions.perform()
#     for element in cookie_count:
#         count = int(element.text.split(" ")[0])
#         for item in items:
#             value = int(item.text)
#             if value <= count:
#                 upgrade_action = ActionChains(driver)
#                 upgrade_action.move_to_element(item)
#                 upgrade_action.click()
#                 actions.perform()
    

