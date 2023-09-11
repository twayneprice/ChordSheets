file1="This Is Amazing Grace"
file2="Me On Your Mind"
file3="*Dry Bones*"
file4="Well Done"


convert -page letter+0-10 -pointsize 15 -draw "text 150,2 'Wayne Sells'" "./prints/orig/${file1}.png" "./prints/orig/${file2}.png" "./prints/orig/${file3}.png" "./prints/orig/${file4}.png" -format pdf ./Sunday.pdf

convert -page letter+0-10 -pointsize 15 -draw "text 150,2 'Band'" "./prints/capo/${file1}.png" "./prints/capo/${file2}.png" "./prints/capo/${file3}.png" "./prints/capo/${file4}.png" -format pdf ./Sunday-Capo.pdf






