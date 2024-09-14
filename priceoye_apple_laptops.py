from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://priceoye.pk/laptops/apple'

response = requests.get(url)
d = {'title': [], 'price': [], 'discount': []}

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    t = soup.find('h1')
    page_title = t.get_text().strip() if t else 'No page title found'
    print(page_title,"\n")

    products = soup.find_all('div', class_="productBox")

    for product in products:
        discontinued = product.find(class_="ribbon ribbon_discontinued")
        if discontinued:
            continue

        mac_t = product.find(class_="p-title bold h5")
        title = mac_t.get_text().strip() if mac_t else 'No title found'

        p = product.find(class_="price-box p1")
        price = p.get_text().strip() if p else 'No price found'

        disc = product.find(class_="price-diff-saving")
        discount = disc.get_text().strip() if disc else 'No discount found'

        d['title'].append(title)
        d['price'].append(price)
        d['discount'].append(discount)

  
        print(f"Title: {title}")
        print(f"Price: {price}")
        print(f"Discount: {discount}")
        print("-" * 70)

    
    df = pd.DataFrame(data=d)
    df.to_csv('apple_laptops.csv', index=False)

    print("Data has been successfully saved to 'apple_laptops.csv'.")
    
else:
    print("Error! Status code: ", response.status_code)
