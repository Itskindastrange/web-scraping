from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.youtube.com/@cristiano/videos")

while len(driver.find_elements(By.ID,"contents"))==0:
    pass
container = driver.find_element(By.ID,"contents")
videos = container.find_elements(By.ID,"video-title-link")
links = []
titles = []
views = []
comments = []
for video in videos:
    titles.append(video.get_attribute("title"))
    links.append(video.get_attribute("href"))

for link in links:
    driver.get(link)
    while len(driver.find_elements(By.CSS_SELECTOR,"#info > span:nth-child(1)")) == 0:
        pass
    views.append(driver.find_element(By.CSS_SELECTOR, "#info > span:nth-child(1)").text)
    while len(driver.find_elements(By.CSS_SELECTOR,"#count > yt-formatted-string")) == 0:
        driver.execute_script("window.scrollTo(0,500);")
    comments.append(driver.find_element(By.CSS_SELECTOR,"#count > yt-formatted-string").text)
    print(comments)