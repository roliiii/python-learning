import re
from urllib.request import urlopen


param=12345

while param is not None:
    url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="+str(param)
    page = urlopen(url)
    data = page.read().decode("utf-8")

    searcRes = re.search(r"""(?<=and the next nothing is )(\d)+""",data)

    if(data=='Yes. Divide by two and keep going.'):
        divider=2
        param=int(param)//2
    elif searcRes is None:
        param = None
    else:
        param = int(searcRes.group());
    print(data)
    