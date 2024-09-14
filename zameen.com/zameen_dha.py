import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


os.makedirs("zameen.com_data", exist_ok=True)
driver = webdriver.Chrome()

fileNo = 0 

try:
    for i in range(1, 6):
        driver.get(f"https://www.zameen.com/Houses_Property/Lahore_DHA_Defence-9-1.html")
     
        elems = driver.find_elements(By.CLASS_NAME, '_5b98ebdf')
        print(f"{len(elems)} results found on page {i}")

        for elem in elems:
            data = elem.get_attribute('outerHTML')
            if data: 
                with open(f"zameen.com_data/zameen_{fileNo}.html", 'w', encoding='utf-8') as f:
                    f.write(data)
                    fileNo += 1

        time.sleep(10) 
finally:
    driver.quit()  