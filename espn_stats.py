from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

d=[]
cols = ['Player','Span', 'Mat', 'Inns', 'Overs', 'Mdns', 'Runs', 'Wkts', 'BBI', 'Ave', 'Econ', 'SR', '4', '5', '10']

PATH = "C:\\Program Files (x86)\\chromedriver.exe"
service = Service(executable_path=PATH)
driver = webdriver.Chrome(service=service)
driver.get('https://www.google.com/')

search_box = driver.find_element(By.ID,"APjFqb")
search_box.send_keys("Best economy rates for Pakistan in Tests")
search_box.send_keys(Keys.ENTER)
time.sleep(3)

select_search_result = driver.find_element(By.XPATH, '(//h3)[1]')
select_search_result.click()
time.sleep(5)
driver.implicitly_wait(3)


table = driver.find_element(By.XPATH, "//table[contains(@class, 'ds-table')]")
rows = table.find_elements(By.TAG_NAME, "tr")

for row in rows[1:]:
    cells = row.find_elements(By.TAG_NAME, "td")
    if len(cells) > 1:  
        d.append([cell.text for cell in cells])

max_columns = max(len(row) for row in d)
if max_columns > len(cols):
    print(f"Data has {max_columns} columns, but only {len(cols)} column names were defined.")
    cols = cols + [f"Column {i+1}" for i in range(max_columns - len(cols))]

df = pd.DataFrame(d,columns=cols)
df.index += 1
df.to_csv('test_stats.csv',index=True)
#print(df)

driver.quit()
