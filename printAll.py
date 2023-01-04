import urllib.request
import json
import os
import requests
from operator import itemgetter

def printAll(inUrl):
    files = getFileList(inUrl)
    files = files#[42:43]
    for fileDict in files:
        name = fileDict['name'].split('.')[0]
        file = fileDict['download_url']
        print(name)

        dir = './prints/orig/'
        cmd = 'google-chrome --headless --disable-gpu --print-to-pdf="'+dir+name+'.pdf" "file:///home/wayne/Downloads/ChordSheets/onSongViewer.html?file='+file+'"'
        # print(cmd)
        os.system(cmd)

        res = requests.get(file, headers={'User-Agent':'Mozilla/5.0'})
        onsong = res.text.replace('\x00','')
        capo = ''
        if 'Capo:' in onsong:
            capoNum = onsong.split('Capo:')[-1].split('\n')[0].strip()
            if capoNum != '0':
                capo = '-Capo-'+capoNum

        dir = './prints/capo/'
        cmd = 'google-chrome --headless --disable-gpu --print-to-pdf="'+dir+name+capo+'.pdf" "file:///home/wayne/Downloads/ChordSheets/onSongViewer.html?file='+file+'&transpose='+capoNum+'"'
        # print(cmd)
        os.system(cmd)

def getFileList(inUrl):
    data = {}
    with urllib.request.urlopen(inUrl) as url:
        data = json.load(url)
    
    return sorted(data, key=itemgetter('name'))

if __name__ == "__main__":
    printAll("https://api.github.com/repos/twayneprice/ChordSheets/contents/onSong")