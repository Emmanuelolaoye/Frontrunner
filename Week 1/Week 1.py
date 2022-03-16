from bs4 import BeautifulSoup
import requests
import csv

url = "https://www.bbc.com/sport/winter-olympics/60242407"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")


images = []
for img in doc.findAll('img'):
    images.append(img.get('src'))


print(images)

f = open('images.txt', 'w')

for i in images:

    print(i)
    f.write(i + "\n")
f.close()