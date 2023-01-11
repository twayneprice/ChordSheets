convert -pointsize 20 -draw "text 400,20 '$(date -dnext-sunday +%m-%d-%Y)  Wayne Sells'" "./prints/orig/Forever Reign.png" "./prints/orig/*Fly Away.png" "./prints/orig/Man Of Sorrows.png" "./prints/orig/*Dry Bones.png" -page letter ./prints/$(date -dnext-sunday +%m-%d-%Y).pdf

convert -pointsize 20 -draw "text 400,20 '$(date -dnext-sunday +%m-%d-%Y)'" "./prints/capo/Forever Reign.png" "./prints/capo/*Fly Away.png" "./prints/capo/Man Of Sorrows.png" "./prints/capo/*Dry Bones.png" -page letter ./prints/$(date -dnext-sunday +%m-%d-%Y)-Capo.pdf
