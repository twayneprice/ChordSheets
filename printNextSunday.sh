file1="When the Roll*"
file2="Well Done"
file3="Scars"
file4="Mamas"


# convert -page letter+0-10 -pointsize 15 -draw "text 150,2 '04-09-2023  Wayne Sells'" "./prints/orig/${file1}.png" "./prints/orig/${file2}.png" "./prints/orig/${file3}.png" "./prints/orig/${file4}.png" -format pdf ./04-09-2023.pdf
convert -page letter+0-10 -pointsize 15 -draw "text 150,2 '$(date -dnext-sunday +%m-%d-%Y)  Wayne Sells'" "./prints/orig/${file1}.png" "./prints/orig/${file2}.png" "./prints/orig/${file3}.png" "./prints/orig/${file4}.png" -format pdf ./$(date -dnext-sunday +%m-%d-%Y).pdf

# convert -page letter+0-10 -pointsize 15 -draw "text 150,2 '04-09-2023  Band'" "./prints/capo/${file1}.png" "./prints/capo/${file2}.png" "./prints/capo/${file3}.png" "./prints/capo/${file4}.png" -format pdf ./04-09-2023-Capo.pdf
convert -page letter+0-10 -pointsize 15 -draw "text 150,2 '$(date -dnext-sunday +%m-%d-%Y)  Band'" "./prints/capo/${file1}.png" "./prints/capo/${file2}.png" "./prints/capo/${file3}.png" "./prints/capo/${file4}.png" -format pdf ./$(date -dnext-sunday +%m-%d-%Y)-Capo.pdf






# convert -page 828x612+0-10 -pointsize 15 -draw "text 150,2 '$(date -dnext-sunday +%m-%d-%Y)  Wayne Sells'" "./prints/condensed/orig/${file1}.png" "./prints/condensed/orig/${file2}.png" "./prints/condensed/orig/${file3}.png" "./print/condensed/orig/${file4}.png" -resize 800x600 -gravity North -format pdf ./$(date -dnext-sunday +%m-%d-%Y)-Condensed.pdf

# convert -page 828x612+0-10 -pointsize 15 -draw "text 150,2 '$(date -dnext-sunday +%m-%d-%Y)  Band'" "./prints/condensed/capo/${file1}.png" "./prints/condensed/capo/${file2}.png" "./prints/condensed/capo/${file3}.png" "./prints/condensed/capo/${file4}.png" -resize 800x600 -gravity North -format pdf ./$(date -dnext-sunday +%m-%d-%Y)-Capo-Condensed.pdf

