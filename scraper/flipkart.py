import requests
from bs4 import BeautifulSoup

def flipkart():
    url = "https://www.flipkart.com/search?q=shoes"

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept-Language": "en-IN,en;q=0.9"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    brands = soup.find_all('div', class_='Fo1I0b')
    selling_price = soup.find_all('div', class_='hZ3P6w')
    discount = soup.find_all('div', class_='HQe8jr')

    image_urls = []
    for img in soup.find_all('img'):
        src = img.get('src')
        if src and "rukminim2.flixcart.com" in src:
            image_urls.append(src)

    min_len = min(len(brands), len(selling_price), len(discount), len(image_urls))

    products_data = []

    for i in range(min_len):
        products_data.append({
            "brand": brands[i].get_text(strip=True),
            "price": selling_price[i].get_text(strip=True),
            "discount": discount[i].get_text(strip=True),
            "image_url": image_urls[i]
        })

    return products_data
