TODO:

I probably need to make the menu better - smaller text for tags, for example

Generally make the menu better.

Convert the rst to markdown. (Apparently pandoc can do this, a la `pandoc foo.rst -s -o foo.md`)
then do like
```
for FILE in `ls`; do ./fix.py $FILE; done
```
to fix the resulting markdown files.


get pics for drinks

startup dev server:
`pelican -l -t themes/attila -r`

