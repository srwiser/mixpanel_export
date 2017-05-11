#!/bin/bash
for filename in *.json; do
	jsonfile=$filename
	csvfile=`ls $filename | cut -d '.' -f 1`.csv
	if [ ! -f $csvfile ]; then
		echo "Creating $csvfile"
		python jsontocsv.py $jsonfile $csvfile
	fi
done
