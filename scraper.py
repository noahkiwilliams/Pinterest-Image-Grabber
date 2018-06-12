from lxml import html
import requests
import urllib
import random

page = requests.get('https://www.pinterest.com/search/pins/?q=style&rs=typed&term_meta[]=style%7Ctyped')
tree = html.fromstring(page.content)
image_list = tree.xpath("//img/@srcset")

for image in image_list:
    image = image.split(" ")
    file_name = random.randrange(1000,9999)
    full_file_name = str(file_name) + '.jpg'
    urllib.request.urlretrieve(image[-2], full_file_name)

'''
Downloads full-size images from pinterest

'''
