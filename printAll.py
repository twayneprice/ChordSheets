import urllib.request
import json
import os
import requests
from operator import itemgetter

def printAll(inUrl):
    files = getFileList(inUrl)
    files = files#[5:6]
    for fileDict in files:
        # print(fileDict)

        name = fileDict['name'].split('.')[0]
        file = fileDict['download_url']

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


        # break


def getFileList(inUrl):
    data = {}
    with urllib.request.urlopen(inUrl) as url:
        data = json.load(url)
    
    return sorted(data, key=itemgetter('name'))


# google-chrome --headless --disable-gpu --print-to-pdf=out.pdf "file:///home/wayne/Downloads/ChordSheets/onSongViewer.html?fontAdjust=12&transpose=2"

# google-chrome --headless --disable-gpu --print-to-pdf=out.pdf "file:///home/wayne/Downloads/ChordSheets/onSongViewer.html?file=https://twayneprice.github.io/ChordSheets/onSong/10,000%20Reasons.onsong&transpose=4"


# https://twayneprice.github.io/ChordSheets/songs.html?v=0.6646505201266948


if __name__ == "__main__":
    printAll("https://api.github.com/repos/twayneprice/ChordSheets/contents/onSong")