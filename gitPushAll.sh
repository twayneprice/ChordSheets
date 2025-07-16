git add -A
git commit -m "new songs"
git push
sleep 30

python3 printPDFs.py --sunday-only
# python3 printAll.py

# ./printNextSunday.sh

git add -A
git commit -m "update pdfs"
git push



