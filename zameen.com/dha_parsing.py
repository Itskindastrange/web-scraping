from bs4 import BeautifulSoup
import os
import pandas as pd

d = {'location': [], 'price': [], 'numBeds': [], 'numBaths': [], 'area': []}

for file in os.listdir('zameen.com_data'):
    with open(os.path.join('zameen.com_data', file), 'r', encoding='utf-8') as f:
        html_doc = f.read()
    
    soup = BeautifulSoup(html_doc, 'html.parser')

    loc = soup.find('div', class_='db1aca2f')
    location = loc.get_text().strip() if loc else 'No location found'

    price_tag = soup.find('span', class_='dc381b54')
    price = price_tag.get_text().strip() if price_tag else 'No price found'

    beds = soup.find('span', class_='_6d9b9b83', attrs={'aria-label': 'Beds'})
    numBeds = beds.get_text().strip() if beds else 'No bed info found'

    baths = soup.find('span', class_='_6d9b9b83', attrs={'aria-label': 'Baths'})
    numBaths = baths.get_text().strip() if baths else 'No bath info found'

    area = soup.find('span', class_='_6d9b9b83', attrs={'aria-label': 'Area'})
    area_text = area.get_text().strip() if area else 'No area info found'

    d['location'].append(location)
    d['price'].append(price)
    d['numBeds'].append(numBeds)
    d['numBaths'].append(numBaths)
    d['area'].append(area_text)

    print(f"Location: {location}")
    print(f"Price: {price}")
    print(f"Beds: {numBeds}")
    print(f"Baths: {numBaths}")
    print(f"Area: {area_text}")
    print("-" * 70)

df = pd.DataFrame(data=d)
df.to_csv('zameen_data.csv', index=False)

print("Data has been successfully saved to 'zameen_data.csv'.")
