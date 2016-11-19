from lxml import html
import requests
from io import BytesIO
from PIL import Image
import profile

#Person images
count = 0
for num in range(1,131):
    page = requests.get('http://openimages.oldjpg.com/word_id/m01g317?page=' + str(num))
    tree = html.fromstring(page.content)
    links = tree.xpath('//img[@class="img-responsive"]/@src')

    for link in links:
        image_name = str(count) + '.jpg'
        r = requests.get(link)
        i = Image.open(BytesIO(r.content))
        i.save('../People/' + image_name)
        count+=1


#Machine images
count = 0
for num in range(1,30):
    page = requests.get('http://openimages.oldjpg.com/word_id/m0dkw5?page=' + str(num))
    tree = html.fromstring(page.content)
    links = tree.xpath('//img[@class="img-responsive"]/@src')

    for link in links:
        image_name = str(count) + '.jpg'
        r = requests.get(link)
        i = Image.open(BytesIO(r.content))
        i.save('../Machines/' + image_name)
        count+=1
