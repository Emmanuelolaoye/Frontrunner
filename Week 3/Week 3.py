import io

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from PIL import Image
import requests

wd = webdriver.Chrome(ChromeDriverManager().install())
url = "https://www.motorsport.com/f1/news"

img_bin = []  # srcs links that faild to download
img1 = []  # for selinumimageagetter 1 funtion


def getdata(url):  # beautiful soup header
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup


def nextpagegetter(soup):  # finds the nextpage button class name
    nextbttn = soup.find('a', {'class': 'ms-pager_btn ms-pager_button'}).get('href')
    return "https://www.motorsport.com" + str(nextbttn)  # concatenates the url domain


def mainlinks(soup): # finds the link to the article
    pages = soup.find_all('a', {'class': 'ms-item_link ms-item_link--text'})
    return ["https://www.motorsport.com" + str(page.get('href')) for page in pages] # concatenates the url domain


def imagegetter(list):  # TODO:  make sure soup url is from the list
    img = []
    for links in list:
        print(links)
        soup = getdata(links)
        list = soup.find_all('img')
        nest = [(src.get('alt'), src.get('src')) for src in list]
        img.append(nest)
        for i in nest:
            try:
                imgdownload(i[0], i[1])
            except:  # catch all exceptions and add to a list to work on later
                img_bin.append(i)
                continue


def imgdownload(filename, url):
    download_path = 'C:/Users/Manny/OneDrive - University of Essex/A000 - Frontrunner/Week 3/images/'

    img_content = requests.get(url).content
    img_file = io.BytesIO(img_content)
    img = Image.open(img_file)
    file_path = download_path + filename

    with open(file_path + ".jpg", "wb") as f:
        f.write(img_content)


def seleniumimagegetter(list):
    for link in list:
        print(link)
        wd.get(link)
        images = wd.find_elements(By.TAG_NAME, 'img')
        for image in images:
            img1.append(image.get_attribute('src'))


while True:
    data = getdata(url)
    url = nextpagegetter(data)
    print(url)
    if url == nextpagegetter(getdata(url)):
        break
    imagegetter(mainlinks(data))
    # print(seleniumimagegetter(mainlinks(data)))
