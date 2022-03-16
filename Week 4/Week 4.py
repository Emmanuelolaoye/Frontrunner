import io
import os.path

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from PIL import Image
import requests
# todo os and cv2 are the 2 libraries I use for download

# wd = webdriver.Chrome(ChromeDriverManager().install())
url = "https://www.motorsport.com/f1/news"

img_bin = []  # srcs links that faild to download
img1 = []  # for selinumimageagetter 1 funtion


def getdata(url):  # beautiful soup header
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup


def nextpagegetter(soup):  # finds the nextpage button class name
    nextbttn = soup.find('a', {'class': 'ms-pager_btn ms-pager_button'}).get('href')
    print(img_bin)
    return "https://www.motorsport.com" + str(nextbttn)  # concatenates the url domain


def mainlinks(soup):  # finds the link to the article
    pages = soup.find_all('a', {'class': 'ms-item_link ms-item_link--text'})
    return ["https://www.motorsport.com" + str(page.get('href')) for page in pages]  # concatenates the url domain


def imagegetter(list):  # TODO:  make sure soup url is from the list
    img = []
    for links in list:  # searches through find all list
        print(links)  # just to see progress in terminal
        soup = getdata(links)  # BS4 header file
        list = soup.find_all('img')  # list of all images found
        nest = [(src.get('alt'), src.get('src')) for src in list]  # nested tuple in img list
        img.append(nest)
        for i in nest:  # the found images
            try:
                imgdownload(i[0], i[1])  # sends to image download function

            except:  # catch all exceptions and add to a list to work on later
                img_bin.append(i)
                continue


def imgdownload(filename, url):
    download_path = 'C:/Users/Manny/OneDrive - University of Essex/A000 - Frontrunner/Week 4/'

    img_content = requests.get(url).content  # gets the img as it is
    img_file = io.BytesIO(img_content)
    img = Image.open(img_file)
    # file_path = download_path + filename

    if "Mercedes" in filename or "Hamilton" in filename or "Russell" in filename:  # Manual  filters
        # can use any keyword i like and adds it to a pre-defined folder

        file_path = download_path + "Mercedes/" + filename

    elif "Red Bull" in filename or "Verstappen" in filename or "Perez" in filename:
        file_path = download_path + "Red Bull Racing/" + filename

    elif "Ferrari" in filename or "Leclerc" in filename or "Sainz" in filename:
        file_path = download_path + "Mercedes/" + filename

    elif "Mclaren" in filename or "Norris" in filename or "Ricciardo" in filename:
        file_path = download_path + "Mclaren/" + filename

    elif "Aston Martin" in filename or "Stroll" in filename or "Vettel" in filename:
        file_path = download_path + "Aston Martin/" + filename

    elif "Alpine" in filename or "Ocon" in filename or "Alonso" in filename:
        file_path = download_path + "Alpine/" + filename

    elif "Haas" in filename or "Magnussen" in filename or "Schumacher" in filename:
        file_path = download_path + "Haas F1/" + filename

    elif "Alfa Romeo" in filename or "Bottas" in filename or "Zhou" in filename:
        file_path = download_path + "Alfa Romeo/" + filename

    elif "Williams" in filename or "Albon" in filename or "Latifi" in filename:
        file_path = download_path + "Williams/" + filename

    elif "AlphaTauri" in filename or "Gasly" in filename or "Tsunoda" in filename:
        file_path = download_path + "Alpha Tauri/" + filename

    else:
        file_path = download_path + "00 - Others/" + filename

    with open(file_path + ".jpg", "wb") as f:
        if os.path.exists(file_path + ".jpg"):
            pass
        else:
            f.write(img_content)


# def seleniumimagegetter(list):
#     for link in list:
#         print(link)
#         wd.get(link)
#         images = wd.find_elements(By.TAG_NAME, 'img')
#         for image in images:
#             img1.append(image.get_attribute('src'))
#

while True:
    data = getdata(url)
    url = nextpagegetter(data)
    print(url)
    if url == nextpagegetter(getdata(url)):
        break
    imagegetter(mainlinks(data))
    # print(seleniumimagegetter(mainlinks(data)))
