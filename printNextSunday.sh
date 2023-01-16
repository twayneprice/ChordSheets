file1="Forever Reign"
file2="*Fly Away"
file3="Man Of Sorrows"
file4="*Dry Bones"

convert -pointsize 20 -draw "text 400,20 '$(date -dnext-sunday +%m-%d-%Y)  Wayne Sells'" "./prints/orig/${file1}.png" "./prints/orig/${file2}.png" "./prints/orig/${file3}.png" "./prints/orig/${file4}.png" -page letter ./prints/$(date -dnext-sunday +%m-%d-%Y).pdf

convert -pointsize 20 -draw "text 400,20 '$(date -dnext-sunday +%m-%d-%Y)'" "./prints/capo/${file1}.png" "./prints/capo/${file2}.png" "./prints/capo/${file3}.png" "./prints/capo/${file4}.png" -page letter ./prints/$(date -dnext-sunday +%m-%d-%Y)-Capo.pdf
