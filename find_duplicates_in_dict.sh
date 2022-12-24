if [ -z $1 ]; then file=latin.txt; else file=$1; fi
grep '^[a-z]' $file | sort | uniq -c | grep -v '1'
