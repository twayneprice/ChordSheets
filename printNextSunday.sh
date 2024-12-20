file1="O Holy Night"
file2="The Angels Cried"
file3="What Child Is This"
file4="Joy To The World"
file5="Mary Did You Know"
file6=""
file6=""


convert -page letter+0-10 -pointsize 15 -draw "text 150,2 'Wayne Sells'" "./prints/orig/${file1}.png" "./prints/orig/${file2}.png" "./prints/orig/${file3}.png" "./prints/orig/${file4}.png" "./prints/orig/${file5}.png" "./prints/orig/${file6}.png" "./prints/orig/${file7}.png" -format pdf ./Sunday.pdf

convert -page letter+0-10 -pointsize 15 -draw "text 150,2 'Band'" "./prints/capo/${file1}.png" "./prints/capo/${file2}.png" "./prints/capo/${file3}.png" "./prints/capo/${file4}.png" "./prints/capo/${file5}.png" "./prints/capo/${file6}.png" "./prints/capo/${file7}.png" -format pdf ./Sunday-Capo.pdf

# cd /home/wayne//Documents//Chords/ChordSheets && ./gitPushAll.sh
