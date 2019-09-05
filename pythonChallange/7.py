import PIL
from PIL import Image
import urllib.request as req
from io import BytesIO

image = Image.open(BytesIO(req.urlopen('http://www.pythonchallenge.com/pc/def/oxygen.png').read()),'r')

h=48
w=7

rgbImage = image

for i in range(87):
    r,g,b,a = rgbImage.getpixel((i*w, h))
    print(chr(r), end = '')

#smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]

print()
for val in [105, 110, 116, 101, 103, 114, 105, 116, 121]:
    print(chr(val), end = '')

#integrity