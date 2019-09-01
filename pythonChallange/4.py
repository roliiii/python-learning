import re
from urllib.request import urlopen

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=44827"
page = urlopen(url)
data = page.read()
print(data)