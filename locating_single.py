from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query = 'laptop'
driver.get(f"https://www.amazon.com/s?k={query}&crid=1Z0BK8XIPERB&sprefix=laptop%2Caps%2C480&ref=nb_sb_noss_1")
 
elem = driver.find_element(By.CLASS_NAME,'puis-card-container')
print(elem.text)

time.sleep(10)
driver.close()