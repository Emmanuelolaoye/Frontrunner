from bs4 import BeautifulSoup
from selenium import webdriver
import requests

url = "https://www.motorsport.com/f1/news"


def getdata(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup


def nextpagegetter(soup):
    nextbttn = soup.find('a', {'class': 'ms-pager_btn ms-pager_button'}).get('href')
    return "https://www.motorsport.com" + str(nextbttn)


def mainlinks(soup):
    pages = soup.find_all('a', {'class': 'ms-item_link ms-item_link--text'})
    return ["https://www.motorsport.com" + str(page.get('href')) for page in pages]


def imagegetter(list):  # TODO:  make sure soup url is from the list
    img = []
    for links in list:
        print(links)
        soup = getdata(links)
        list = soup.find_all('img')
        img.append([src.get('src') for src in list])
    return img



while True:
    data = getdata(url)
    url = nextpagegetter(data)
    print(url)
    if url == nextpagegetter(getdata(url)):
        break
    print(imagegetter(mainlinks(data)))

