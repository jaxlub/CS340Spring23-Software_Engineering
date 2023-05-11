#!/bin/bash

cd /home/jalubk20@stlawu.local/cs340/project4/project4c/libpng-1.6.34
old=4090
echo 1 >> probecount.txt
#echo $compare
rm *.gcda pngout.png
# $1 is the "test" file
#check=$(gcovr -s -e contrib -e intel -e mips -e powerpc --gcov-ignore-errors=no_working_dir_found -r . | grep lines | cut -d "(" -f 2 | cut -d " " -f 1)
cat $1 | while read line
    do
        #echo $line
        ./pngtest $line 2> /dev/null 1> /dev/null
    done
new=$(gcovr -s -e contrib -e intel -e mips -e powerpc --gcov-ignore-errors=no_working_dir_found -r . | grep lines | cut -d "(" -f 2 | cut -d " " -f 1)


if (($new < $old)) 
then
  exit 1 
else
  exit 0 # interesting <= note this is for picire
fi

#reads the file provided by Picire and run these files as inputs to pngtest.
#reads the coverage information provided by gcovr.
#determines if the line coverage has decreased.