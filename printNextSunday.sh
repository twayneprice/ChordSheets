file1="*Passion*"
file2="The Old Rugged Cross"
file3="Man Of Sorrows"
file4="King Of Kings"
# file1="Less Like Me"
# file2="*My Chains*"
# file3="Well Done"
# file4="You Say"


# convert -page letter+0-10 -pointsize 15 -draw "text 150,2 '$(date -dnext-sunday +%m-%d-%Y)  Wayne Sells'" "./prints/orig/${file1}.png" "./prints/orig/${file2}.png" "./prints/orig/${file3}.png" "./prints/orig/${file4}.png" -resize 600x800 -gravity North -format pdf ./$(date -dnext-sunday +%m-%d-%Y).pdf

convert -page letter+0-10 -pointsize 15 -draw "text 150,2 '$(date -dnext-sunday +%m-%d-%Y)  Wayne Sells'" "./prints/orig/${file1}.png" "./prints/orig/${file2}.png" "./prints/orig/${file3}.png" "./prints/orig/${file4}.png" -format pdf ./$(date -dnext-sunday +%m-%d-%Y).pdf

convert -page letter+0-10 -pointsize 15 -draw "text 150,2 '$(date -dnext-sunday +%m-%d-%Y)  Band'" "./prints/capo/${file1}.png" "./prints/capo/${file2}.png" "./prints/capo/${file3}.png" "./prints/capo/${file4}.png" -format pdf ./$(date -dnext-sunday +%m-%d-%Y)-Capo.pdf



# convert -page 828x612+0-10 -pointsize 15 -draw "text 150,2 '$(date -dnext-sunday +%m-%d-%Y)  Wayne Sells'" "./prints/condensed/orig/${file1}.png" "./prints/condensed/orig/${file2}.png" "./prints/condensed/orig/${file3}.png" "./print/condensed/orig/${file4}.png" -resize 800x600 -gravity North -format pdf ./$(date -dnext-sunday +%m-%d-%Y)-Condensed.pdf

# convert -page 828x612+0-10 -pointsize 15 -draw "text 150,2 '$(date -dnext-sunday +%m-%d-%Y)  Band'" "./prints/condensed/capo/${file1}.png" "./prints/condensed/capo/${file2}.png" "./prints/condensed/capo/${file3}.png" "./prints/condensed/capo/${file4}.png" -resize 800x600 -gravity North -format pdf ./$(date -dnext-sunday +%m-%d-%Y)-Capo-Condensed.pdf

