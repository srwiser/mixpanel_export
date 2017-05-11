#!/bin/bash
for filename in *.json; do
	jsonfile=$filename
	csvfile=`ls $filename | cut -d '.' -f 1`.csv
	if [ -f $csvfile ]; then
		echo "CSV already exist for $jsonfile"
	else
		echo "Creating csv for $jsonfile"
		python jsontocsv.py $jsonfile $csvfile
	fi
done
exit 0
