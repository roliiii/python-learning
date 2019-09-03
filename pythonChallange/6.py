import re, zipfile
from urllib.request import urlopen

#http://www.pythonchallenge.com/pc/def/channel.html
#http://www.pythonchallenge.com/pc/def/channel.zip
param=90052
zip = zipfile.ZipFile('pythonChallange/channel.zip')
while param is not None:
    data = zip.read(str(param) + '.txt').decode('utf-8')
    print(zip.getinfo(str(param) + '.txt').comment.decode('utf-8'),end="")
    searcRes = re.search(r"""(?<=Next nothing is )(\d)+""",data)

    if searcRes is None:
        param = None
    else:
        param = int(searcRes.group());
    
#http://www.pythonchallenge.com/pc/def/hockey.html