from lxml import html
import requests
import urllib
import random
import time
import os

search_term = input("Type your search term here: ")

str1 = "https://www.pinterest.com/search/pins/?q="
str2 = "&rs=typed&term_meta[]="
str3 = "%7Ctyped"

search_url = str1 + search_term + str2 + search_term + str3

page = requests.get(search_url)
tree = html.fromstring(page.content)
image_list = tree.xpath("//img/@srcset")

directory = search_term

if not os.path.exists(directory):
    os.makedirs(directory)

for image in image_list:
    image = image.split(" ")
    file_name = random.randrange(1000,9999)
    full_file_name = os.path.join(directory, str(file_name) + '.jpg')
    urllib.request.urlretrieve(image[-2], full_file_name) # retrieves largest image

print("Images downloaded: Desktop > " search_term)
time.sleep(1.5)
print("Download complete")
