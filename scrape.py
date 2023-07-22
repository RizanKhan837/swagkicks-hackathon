""" import requests
from bs4 import BeautifulSoup

l=[]
o={}
image_list=[]
target_url="https://www.ebay.com/itm/275296794239"

resp = requests.get(target_url)

soup=BeautifulSoup(resp.text,'html.parser')


o["title"]=soup.find("h1",{"class":"x-item-title__mainTitle"}).text
#o["rating"]=soup.find("span",{"class":"ebay-review-start-rating"}).text.strip()
o["actual_price"]=soup.find("span",{"class":"ux-textspans"}).text
box=soup.find("div",{"class":"x-additional-info"})
o["list_price"]=box.find("span",{"class":"ux-textspans--STRIKETHROUGH"}).text
o["date"]=soup.find("span",{"class":"vi-notify-new-bg-dBtm"}).text
#o["date"]=box.find("span",{"class":"ux-textspans--FLAME_ICON"}).text
o["discount"]=box.find("span",{"class":"ux-textspans--EMPHASIS"}).text
o["shipping_price"]=soup.find("div",{"id":"SRPSection"}).find("span",{"class":"ux-textspans--BOLD"}).text
l.append(o)
print(l) """


import requests
from bs4 import BeautifulSoup

url = 'https://www.projectblitz.com/products/air-jordan-11-retro378037-002'

def scrape_product_details(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract product name
    product_name = soup.find('h1', class_='mb-2').text

    # Extract product price
    product_price = soup.find('span', class_='price').text.strip()

    # Extract available sizes
    sizes = soup.find('div', class_='size-buttons').find_all('label')
    available_sizes = [size.text.strip() for size in sizes]

    # Extract product year
    product_year = soup.find('div', class_='product-year').text.strip()

    return {
        'Product Name': product_name,
        'Product Price': product_price,
        'Available Sizes': available_sizes,
        'Product Year': product_year
    }

if __name__ == "__main__":
    product_details = scrape_product_details(url)
    print(product_details)