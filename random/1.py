from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


PATH = "C:\\Program Files (x86)\\chromedriver.exe"
service = Service(executable_path=PATH)
driver = webdriver.Chrome(service=service)



driver.get("https://en.wikipedia.org/wiki/Main_Page")
print(driver.title)


link = driver.find_element(By.LINK_TEXT, "Log in")
link.click()
try:

    element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Join Wikipedia")) 
        )
    element.click()
except:
    driver.quit()



time.sleep(15)
driver.quit()
