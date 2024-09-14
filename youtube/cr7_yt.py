from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import pandas as pd
from bs4 import BeautifulSoup
from scroll_yt import scroll_bottom
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless=new")
#chrome_options.add_argument("--start-maximized")
PATH = "C:\\Program Files (x86)\\chromedriver.exe"
service = Service(executable_path=PATH)
driver = webdriver.Chrome(service=service,options=chrome_options)
driver.get("https://www.youtube.com/@cristiano/videos")
driver.implicitly_wait(7)

scroll_bottom(driver)

# Use BeautifulSoup to parse the page
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Ensure content is available
while len(soup.find_all(id='contents')) == 0:
    time.sleep(1)
    soup = BeautifulSoup(driver.page_source, 'html.parser')

# Extract video information
titles = []
links = []
views = []
comments = []
# Locate the video containers
container = soup.find_all('ytd-rich-grid-media')

for video in container:
    title_tag = video.find('a', {'id': 'video-title-link'})
    if title_tag:
        # Extract title
        title = title_tag.get('title').strip()
        titles.append(title)
        
        # Extract link
        link = 'https://youtube.com' + title_tag.get('href')
        links.append(link)
    
    # Extract view count
    view_count_tag = video.find('span', {'class': 'inline-metadata-item'})
    if view_count_tag:
        views.append(view_count_tag.text.strip())
    else:
        views.append('N/A')

# Initialize list to hold comment counts


# Navigate to each video page and scroll to get the comments count
for link in links:
    driver.get(link)
    time.sleep(5)
    while len(driver.find_elements(By.CSS_SELECTOR,"#count > yt-formatted-string")) == 0:
        driver.execute_script("window.scrollTo(0,500);")
    comments.append(driver.find_element(By.CSS_SELECTOR,"#count > yt-formatted-string").text)

    time.sleep(3)

# Create DataFrame to store video data
df = pd.DataFrame({
    'Title': titles,
    'Views': views,
    'Comments': comments,
    'Link': links
})

# Print and save the DataFrame
print(df)
df.index += 1    
df.to_csv("yt_video_content.csv", index=True)

driver.quit()
