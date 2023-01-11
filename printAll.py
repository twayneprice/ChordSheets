import urllib.request
import json
import os
import requests
from operator import itemgetter
# import subprocess
import git
from datetime import datetime, timedelta


def printAll(sinceDate):
    g = git.Git(".") 
    files = g.log('--since',sinceDate,'--name-status','--oneline','*.onsong')

    files = files.split('\n')
    files = [x[2:] for x in files if "onSong/" in x]
    files = [*set(files)]
    files.sort()

    for gitFile in files:
        name = gitFile.split('/')[-1].split('.')[0]
        print(name)
        continue
        file = 'https://raw.githubusercontent.com/twayneprice/ChordSheets/main/onSong/'+name+'.onsong'

        dir = './prints/orig/'
        cmd = 'google-chrome --headless --disable-gpu --hide-scrollbars --screenshot="'+dir+name+'.png" -window-size=900,1120 "file:///home/wayne/Downloads/ChordSheets/onSongViewer.html?file='+file+'"'
        os.system(cmd)

        res = requests.get(file, headers={'User-Agent':'Mozilla/5.0'})
        onsong = res.text.replace('\x00','')

        capo = ''
        if 'Capo:' in onsong:
            capoNum = onsong.split('Capo:')[-1].split('\n')[0].strip()
            if capoNum != '0':
                capo = '-Capo-'+capoNum

        dir = './prints/capo/'
        cmd = 'google-chrome --headless --disable-gpu --hide-scrollbars --screenshot="'+dir+name+'.png" -window-size=900,1120 "file:///home/wayne/Downloads/ChordSheets/onSongViewer.html?file='+file+'&transpose='+capoNum+'"'
        os.system(cmd)

    cmd = 'convert "./prints/orig/*.png" -page letter ./prints/Songs.pdf'
    os.system(cmd)

    cmd = 'convert "./prints/capo/*.png" -page letter ./prints/Songs-Capo.pdf'
    os.system(cmd)


def getFileList(inUrl):
    data = {}
    with urllib.request.urlopen(inUrl) as url:
        data = json.load(url)
    
    return sorted(data, key=itemgetter('name'))

if __name__ == "__main__":
    sinceDate = '1/1/2000'
    lastSunday = (datetime.now()
                     -timedelta(days=((datetime.now().isoweekday() + 1) % 7))
                     ).strftime('%m/%d/%Y')

    sinceDate = lastSunday
    printAll(sinceDate)