from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
query = 'laptop'

for i in range(1,10):
    driver.get(f"https://www.amazon.com/s?k={query}&page={i}&crid=1Z0BK8XIPERB&sprefix=laptop%2Caps%2C480&ref=nb_sb_noss_1")
 
    elems = driver.find_elements(By.CLASS_NAME,'puis-card-container')
    print(f"{len(elems)} results found")

    print(elems)

    for elem in elems:
        print(elem.text)

    time.sleep(10)
    driver.close()


