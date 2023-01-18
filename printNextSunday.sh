file1="Less Like Me"
file2="When the Roll*"
file3="Blessed Redeemer"
file4="Holy Water"

convert -pointsize 20 -draw "text 400,20 '$(date -dnext-sunday +%m-%d-%Y)  Wayne Sells'" "./prints/orig/${file1}.png" "./prints/orig/${file2}.png" "./prints/orig/${file3}.png" "./prints/orig/${file4}.png" -page letter ./prints/$(date -dnext-sunday +%m-%d-%Y).pdf

convert -pointsize 20 -draw "text 400,20 '$(date -dnext-sunday +%m-%d-%Y)'" "./prints/capo/${file1}.png" "./prints/capo/${file2}.png" "./prints/capo/${file3}.png" "./prints/capo/${file4}.png" -page letter ./prints/$(date -dnext-sunday +%m-%d-%Y)-Capo.pdf
