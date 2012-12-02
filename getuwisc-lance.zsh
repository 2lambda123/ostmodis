#!/bin/zsh

for X in AERONET_U_of_Wisconsin_SSEC.2012{001..0344}.{aqua,terra}.250m.jpg; do
	if [ -e $X ]; then
		echo already got $X
	else	
        curl "http://lance-modis.eosdis.nasa.gov/imagery/subsets/?subset=$X" -o "$X"
   fi
done