from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import time

# Import the helper functions from youtube_scraper_utils
from scroll_yt import scroll_bottom, scroll_comments

# Start the webdriver
PATH = "C:\\Program Files (x86)\\chromedriver.exe"
service = Service(executable_path=PATH)
driver = webdriver.Chrome(service=service)
driver.get('https://www.youtube.com/@cristiano/videos')

time.sleep(5)  # Let the page load completely

# Scroll down to load more videos
scroll_bottom(driver)

# Parse the page content using BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Extract video titles and view counts
video_titles = []
view_counts = []
video_links = []

# Find video sections using BeautifulSoup
videos = soup.find_all('ytd-grid-video-renderer', {'class': 'style-scope ytd-grid-renderer'})

for video in videos:
    title = video.find('a', {'id': 'video-title'}).text.strip()
    views = video.find('span', {'class': 'inline-metadata-item style-scope ytd-video-meta-block'}).text.strip()
    link = "https://www.youtube.com" + video.find('a', {'id': 'video-title'})['href']
    
    video_titles.append(title)
    view_counts.append(views)
    video_links.append(link)

# Now go through each video link and extract comments count
comment_counts = []
for link in video_links:
    driver.get(link)
    time.sleep(3)
    
    # Scroll to load comments
    scroll_comments(driver)
    
    # Use BeautifulSoup or Selenium to extract comment counts
    try:
        comments_count = driver.find_element(By.XPATH, '//*[@id="count"]/yt-formatted-string/span[1]').text.strip()
    except:
        comments_count = '0'
    
    comment_counts.append(comments_count)
    time.sleep(2)

# Create a DataFrame to store the data
df = pd.DataFrame({
    'Video Title': video_titles,
    'View Count': view_counts,
    'Comments Count': comment_counts
})

# Print or save the DataFrame
print(df)

# Optionally, save to CSV
df.to_csv('cristiano_ronaldo_videos.csv', index=False)

# Close the browser
driver.quit()
