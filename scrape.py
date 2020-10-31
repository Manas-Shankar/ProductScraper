from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome('C:\Path\to\chromedriver.exe')
products = []
prices = []
ratings = []
driver.get("https://www.flipkart.com/search?q=gaming+laptop&sid=6bo%2Cb5g&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_7_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_7_na_na_na&as-pos=1&as-type=RECENT&suggestionId=gaming+laptop%7CLaptops&requestId=70289f50-36cb-4a2c-8ff4-87a099bd81d2&as-backfill=on&p%5B%5D=facets.ram_type%255B%255D%3DDDR4&p%5B%5D=facets.price_range.from%3D40000&p%5B%5D=facets.price_range.to%3DMax&p%5B%5D=facets.processor%255B%255D%3DCore%2Bi5&p%5B%5D=facets.processor%255B%255D%3DRyzen%2B5%2BQuad%2BCore&p%5B%5D=facets.processor%255B%255D%3DRyzen%2B7%2BQuad%2BCore&p%5B%5D=facets.processor%255B%255D%3DRyzen%2B9%2BOcta%2BCore&p%5B%5D=facets.processor%255B%255D%3DRyzen%2B7%2BOcta%2BCore&p%5B%5D=facets.processor%255B%255D%3DRyzen%2B5%2BHexa%2BCore&p%5B%5D=facets.screen_size%255B%255D%3D15%2Binch%2B-%2B15.9%2Binch")
content = driver.page_source
sp = BeautifulSoup(content,features="html.parser")
for i in sp.findAll('a',href=True, attrs={'class':'_31qSD5'}):
    name = i.find('div',attrs={'class':'_3wU53n'})
    price=i.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
    rating=i.find('div', attrs={'class':'hGSR34'})
    products.append(name.text)
    prices.append(price.text)
    ratings.append(rating.text)


print(products)
print(prices)
print(ratings)

df = pd.DataFrame({'Product Name':products,'price':prices,'rating':ratings})
# df.to_csv('products.csv',index=False,encoding='utf-8')
df.to_excel('output.xlsx')





















