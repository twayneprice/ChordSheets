git add -A
git commit -m "new songs"
git push -u https://twayneprice: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@github.com/twayneprice/ChordSheets.git main
sleep 30

python3 printAll.py

./printNextSunday.sh

git add -A
git commit -m "new songs"
git push -u https://twayneprice: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@github.com/twayneprice/ChordSheets.git main
