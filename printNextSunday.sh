file1="Ill Fly Away"
file2="Holy Forever"
file3="Less Like Me"
file4="O Come To The Alter"
file5="Gratitude"
file6=""
file6=""


convert -page letter+0-10 -pointsize 15 -draw "text 150,2 'Wayne Sells'" "./prints/orig/${file1}.png" "./prints/orig/${file2}.png" "./prints/orig/${file3}.png" "./prints/orig/${file4}.png" "./prints/orig/${file5}.png" "./prints/orig/${file6}.png" "./prints/orig/${file7}.png" -format pdf ./Sunday.pdf

convert -page letter+0-10 -pointsize 15 -draw "text 150,2 'Band'" "./prints/capo/${file1}.png" "./prints/capo/${file2}.png" "./prints/capo/${file3}.png" "./prints/capo/${file4}.png" "./prints/capo/${file5}.png" "./prints/capo/${file6}.png" "./prints/capo/${file7}.png" -format pdf ./Sunday-Capo.pdf

# cd /home/wayne//Documents//Chords/ChordSheets && ./gitPushAll.sh