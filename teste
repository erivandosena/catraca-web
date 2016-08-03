#!/bin/bash
for i in arquivo{1..3}.txt
do
 if [[ -e $i ]]; then
 n=$(echo $i | sed 's/.txt/.csv/g')
 cat "$i" | sed 's/;/,/g' > "$n"
 fi
done
