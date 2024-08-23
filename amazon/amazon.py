import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Ensure the data directory exists
os.makedirs("data", exist_ok=True)


driver = webdriver.Firefox()

query = 'laptop'
fileNo = 0 

try:
    for i in range(1, 10):
        driver.get(f"https://www.amazon.com/s?k={query}&page={i}&crid=1Z0BK8XIPERB&sprefix=laptop%2Caps%2C480&ref=nb_sb_noss_1")
     
        elems = driver.find_elements(By.CLASS_NAME, 'puis-card-container')
        print(f"{len(elems)} results found on page {i}")

        for elem in elems:
            data = elem.get_attribute('outerHTML')
            if data: 
                with open(f"data/{query}_{fileNo}.html", 'w', encoding='utf-8') as f:
                    f.write(data)
                    fileNo += 1

        time.sleep(10) 
finally:
    driver.quit()  
