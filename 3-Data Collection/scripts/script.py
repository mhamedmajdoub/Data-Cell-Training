import scrapy
import requests
from scrapy import Selector

url="https://www.deezer.com/fr/offers"
html=requests.get(url).content
print(html)
sel=Selector(text=html)
#xpath='/html/head/title/text()'
xpath='//'
titlte1=sel.xpath(xpath).get()
print(titlte1)


