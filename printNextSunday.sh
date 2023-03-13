file1="Amazing Grace"
file2="Me On Your Mind"
file3="I Am Not Alone"
file4="Man Of Sorrows"

# file1="Battle Belongs"
# file2="Battle Belongs"
# file3="Battle Belongs"
# file4="Battle Belongs"


google-chrome --headless -hide-scrollbars --disable-gpu --hide-scrollbars --screenshot="./prints/capo/${file1}.png" --force-device-scale-factor=2.0 --window-size=900,1200 "file:///home/wayne/Downloads/ChordSheets/onSongViewer.html?file=https://raw.githubusercontent.com/twayneprice/ChordSheets/main/onSong/${file1}.onsong&transpose=0"



# convert -page letter+0-10 -pointsize 15 -draw "text 150,2 '$(date -dnext-sunday +%m-%d-%Y)  Wayne Sells'" "./prints/orig/${file1}.png" "./prints/orig/${file2}.png" "./prints/orig/${file3}.png" "./prints/orig/${file4}.png" -resize 600x800 -gravity North -format pdf ./$(date -dnext-sunday +%m-%d-%Y).pdf

# convert -page letter+0-10 -pointsize 15 -draw "text 150,2 '$(date -dnext-sunday +%m-%d-%Y)  Band'" "./prints/capo/${file1}.png" "./prints/capo/${file2}.png" "./prints/capo/${file3}.png" "./prints/capo/${file4}.png" -resize 600x800 -gravity North -format pdf ./$(date -dnext-sunday +%m-%d-%Y)-Capo.pdf

# convert  -rotate 180  "./prints/capo/${file1}.png" -format pdf ./$(date -dnext-sunday +%m-%d-%Y)-Capo.pdf
# pdftk ./$(date -dnext-sunday +%m-%d-%Y)-Capo.pdf cat 1-endsouth output ./$(date -dnext-sunday +%m-%d-%Y)-Capo2.pdf

# montage "./prints/capo/${file1}.png" -tile 1x -geometry +10+10  -page letter  -format pdf ./$(date -dnext-sunday +%m-%d-%Y)-Capo.pdf

# montage "./prints/capo/${file1}.png" -tile 1x -geometry +10+10 -gravity Center -format pdf ./$(date -dnext-sunday +%m-%d-%Y)-Capo.pdf



# convert -page letter  -pointsize 40 -draw "text 150,2 '$(date -dnext-sunday +%m-%d-%Y)  Band'" "./prints/capo/${file1}.png" "./prints/capo/${file2}.png" "./prints/capo/${file3}.png" "./prints/capo/${file4}.png" -format pdf ./$(date -dnext-sunday +%m-%d-%Y)-Capo.pdf

# convert -page 828x612+0-10 -pointsize 15 -draw "text 150,2 '$(date -dnext-sunday +%m-%d-%Y)  Wayne Sells'" "./prints/condensed/orig/${file1}.png" "./prints/condensed/orig/${file2}.png" "./prints/condensed/orig/${file3}.png" "./print/condensed/orig/${file4}.png" -resize 800x600 -gravity North -format pdf ./$(date -dnext-sunday +%m-%d-%Y)-Condensed.pdf

# convert -page 828x612+0-10 -pointsize 15 -draw "text 150,2 '$(date -dnext-sunday +%m-%d-%Y)  Band'" "./prints/condensed/capo/${file1}.png" "./prints/condensed/capo/${file2}.png" "./prints/condensed/capo/${file3}.png" "./prints/condensed/capo/${file4}.png" -resize 800x600 -gravity North -format pdf ./$(date -dnext-sunday +%m-%d-%Y)-Capo-Condensed.pdf

