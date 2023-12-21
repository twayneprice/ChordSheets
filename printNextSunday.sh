file1="Little Drummer Boy"
file2="O Holy Night"
file3="What Child Is This"
file4="The Angels Cried"
file5=""
file6=""


convert -page letter+0-10 -pointsize 15 -draw "text 150,2 'Wayne Sells'" "./prints/orig/${file1}.png" "./prints/orig/${file2}.png" "./prints/orig/${file3}.png" "./prints/orig/${file4}.png" "./prints/orig/${file5}.png" "./prints/orig/${file6}.png" -format pdf ./Sunday.pdf

convert -page letter+0-10 -pointsize 15 -draw "text 150,2 'Band'" "./prints/capo/${file1}.png" "./prints/capo/${file2}.png" "./prints/capo/${file3}.png" "./prints/capo/${file4}.png" "./prints/capo/${file5}.png" "./prints/capo/${file6}.png" -format pdf ./Sunday-Capo.pdf

