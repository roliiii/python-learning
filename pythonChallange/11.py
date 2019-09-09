from PIL import Image
from io import BytesIO
import requests

# http://www.pythonchallenge.com/pc/return/5808.html


url = r"http://huge:file@www.pythonchallenge.com/pc/return/cave.jpg"

response = requests.get(url)
img = Image.open(BytesIO(response.content))

(w, h) = img.size

even = Image.new("RGB", (w // 2, h // 2))
odd = Image.new("RGB", (w // 2, h // 2))

for i in range(w):
    for j in range(h):
        if (i + j) % 2:
            odd.putpixel((i // 2, j // 2), img.getpixel((i, j)))
        else:
            even.putpixel((i // 2, j // 2), img.getpixel((i, j)))
even.show()
odd.show()
# evil

