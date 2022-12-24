if [ -z $1 ]; then file=latin.txt; else file=$1; fi
echo $file
grep -v '^[1-9]' $file | grep '^[a-z]' | wc -l
