import os
import subprocess
import sys
import urllib.request
from PIL import Image

def format(url):
    url=url[url.find('respaper.com')+len('respaper.com')+1:url.find('.html')]
    ans=''
    for i in range(len(url)):
        if url[i]=='/' or url[i]=='-':
            ans=ans+'.'
        else:
            ans=ans+url[i]
    return ans

numPages = int(input("NumPages = "))
# gifFileName = input("gifFileName = ")
gifFileName = format(input("URL = "))
pCachePath = 'pl.respaper.com/icache/'

saveFileName = input("Name = ")
where = 'https://'+pCachePath + gifFileName+'/'
all = []


for i in range(numPages):
    serverPath = where + str(i) + '.gif'
    localPath = '/home/anushi/ResPaper/temp/' + str(i) + '.gif'
    print(serverPath)
    urllib.request.urlretrieve(serverPath, localPath)
    all.append(Image.open(localPath))

fileName = '/home/anushi/Downloads/' + saveFileName + '.pdf'
all[0].save(fileName, resolution=100, save_all=True, append_images=all[1:])
subprocess.call(["xdg-open",fileName])
