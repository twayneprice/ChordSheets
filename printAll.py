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

    # files = files.replace('\t','\n')
    files = files.split('\n')
    files = [x[2:] for x in files if "M\tonSong/" in x]
    files = [*set(files)]
    files.sort()

    for gitFile in files:
        name = gitFile.split('/')[-1].split('.')[0]
        print(name)

        file = 'https://raw.githubusercontent.com/twayneprice/ChordSheets/main/onSong/'+name+'.onsong'

        # orig
        dir = './prints/orig/'

        cmd = 'google-chrome --headless=new --force-device-scale-factor=2.0  --window-size=900,1200 --disable-gpu --screenshot="'+dir+name+'.png"  "file:///home/wayne/Downloads/ChordSheets/onSongViewer.html?file='+file+'"'
        os.system(cmd)

        cmd = 'convert -pointsize 20 -draw "text 100,30 \'Last Changed: $(date -r "./onSong/'+name+'.onsong" +%m-%d-%Y)\'" "'+dir+name+'.png" "'+dir+name+'.png"'
        os.system(cmd)


        # # orig cond
        # dir = './prints/condensed/orig/'
        # cmd = 'google-chrome --headless -hide-scrollbars --disable-gpu --hide-scrollbars --screenshot="'+dir+name+'.png" -window-size=900,1200 "file:///home/wayne/Downloads/ChordSheets/onSongViewer.html?condensed=true&file='+file+'" >/dev/null 2>&1'
        # # os.system(cmd)

        # cmd = 'convert -pointsize 20 -draw "text 35,30 \'Last Changed: $(date -r "./onSong/'+name+'.onsong" +%m-%d-%Y)\'" -trim "'+dir+name+'.png" -trim "'+dir+name+'.png" >/dev/null 2>&1'
        # # os.system(cmd)

 
        # Capo
        res = requests.get(file, headers={'User-Agent':'Mozilla/5.0'})
        onsong = res.text.replace('\x00','')

        capo = ''
        capoNum = '0'
        if 'Capo:' in onsong:
            capoNum = onsong.split('Capo:')[-1].split('\n')[0].strip()
            if capoNum != '0':
                capo = '-Capo-'+capoNum

        dir = './prints/capo/'
        cmd = 'google-chrome --headless=new --force-device-scale-factor=2.0  --window-size=900,1200 --disable-gpu --screenshot="'+dir+name+'.png"  "file:///home/wayne/Downloads/ChordSheets/onSongViewer.html?file='+file+'&transpose='+capoNum+'"'
        os.system(cmd)

        cmd = 'convert -pointsize 20 -draw "text 100,30 \'Last Changed: $(date -r "./onSong/'+name+'.onsong" +%m-%d-%Y)\'" "'+dir+name+'.png" "'+dir+name+'.png"'
        os.system(cmd)

        # #capo cond
        # dir = './prints/condensed/capo/'
        # cmd = 'google-chrome --headless -hide-scrollbars --disable-gpu --hide-scrollbars --screenshot="'+dir+name+'.png" -window-size=900,2000 "file:///home/wayne/Downloads/ChordSheets/onSongViewer.html?condensed=true&file='+file+'&transpose='+capoNum+'" >/dev/null 2>&1'
        # # os.system(cmd)
        # cmd = 'convert -pointsize 10 -draw "text 35,30 \'Last Changed: $(date -r "./onSong/'+name+'.onsong" +%m-%d-%Y)\'" "'+dir+name+'.png" -trim "'+dir+name+'.png" >/dev/null 2>&1'
        # # os.system(cmd)

    cmd = 'convert -page letter+0-10 "./prints/orig/*.png" -format pdf ./Songs.pdf >/dev/null 2>&1'
    os.system(cmd)

    cmd = 'convert -page letter+0-10 "./prints/capo/*.png" -format pdf ./Songs-Capo.pdf >/dev/null 2>&1'
    os.system(cmd)


    # cmd = 'convert -page 828x612+0-10 "./prints/condensed/orig/*.png" -resize 800x600 -gravity North -format pdf ./Songs-Condensed.pdf >/dev/null 2>&1'
    # os.system(cmd)

    # cmd = 'convert -page 828x612+0-10 "./prints/condensed/capo/*.png" -resize 800x600 -gravity North -format pdf ./Songs-Capo-Condensed.pdf >/dev/null 2>&1'
    # os.system(cmd)


def getFileList(inUrl):
    data = {}
    with urllib.request.urlopen(inUrl) as url:
        data = json.load(url)
    
    return sorted(data, key=itemgetter('name'))

if __name__ == "__main__":
    sinceDate = '1/1/2000'
    lastSunday = (datetime.now()
                     -timedelta(days=((datetime.now().isoweekday() + 1) % 7)+7)
                     ).strftime('%m/%d/%Y')

    sinceDate = lastSunday
    print(sinceDate)
    printAll(sinceDate)