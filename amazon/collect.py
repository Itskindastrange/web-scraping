from bs4 import BeautifulSoup
import os
import pandas as pd

# Dictionary to store the scraped data
d = {'title': [], 'price': [], 'link': []}

# Loop through the files in the 'data' directory
for file in os.listdir('data'):
    try:
        if file.endswith('.html'):
            # Open and read the HTML file
            with open('data/' + file, 'r', encoding='utf-8') as f:
                html_doc = f.read()
            soup = BeautifulSoup(html_doc, 'html.parser')
            
            # Find the title
            t = soup.find('h2')
            if t:
                title = t.get_text().strip()  # Strip to remove extra whitespace
            else:
                title = 'No title found'

            # Find the link
            l = t.find('a') if t else None
            if l and 'href' in l.attrs:
                link = 'https://www.amazon.com' + l['href']
            else:
                link = 'No link found'

            # Find the price
            p = soup.find('span', attrs={'class': 'a-price-whole'})
            if p:
                price = p.get_text().strip()
            else:
                price = 'No price found'

            # Append the data to the dictionary
            d['title'].append(title)
            d['price'].append(price)
            d['link'].append(link)

    except Exception as e:
        print(f"Error processing file {file}: {e}")

# Create a DataFrame and save it to a CSV file
df = pd.DataFrame(data=d)
df.to_csv('data.csv', index=False)  # index=False to avoid saving the DataFrame index

print("Data has been successfully saved to 'data.csv'.")
