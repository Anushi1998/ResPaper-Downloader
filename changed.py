import os
import urllib.request
from PIL import Image


numPages = int(input("NumPages = "))
pCachePath = 'pl.respaper.com/icache/'
gifFileName = input("gifFileName = ")
where = 'https://'+pCachePath + gifFileName+'/'
all = []
for i in range(numPages):
    serverPath = where + str(i) + '.gif'
    localPath = os.getcwd() + '/Downloads/' + str(i) + '.gif'
    print(serverPath)
    urllib.request.urlretrieve(serverPath, localPath)
    all.append(Image.open(localPath))
fileName = os.getcwd() + '/Downloads/' + gifFileName + '.pdf'
all[0].save(fileName, resolution=100, save_all=True, append_images=all[1:])

