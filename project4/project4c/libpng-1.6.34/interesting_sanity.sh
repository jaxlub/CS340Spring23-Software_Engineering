#!/bin/bash

# $1 is the "test" file

# we will look for 10.png, 24.png, and 1024.png

ONE=0
TWO=0
THREE=0

for f in $(cat $1)
do
  if [ $(basename $f) = "10.png" ]
  then
    ONE=1
  fi

  if [ $(basename $f) = "24.png" ]
  then
    TWO=1
  fi

  if [ $(basename $f) = "1024.png" ]
  then
    THREE=1
  fi
done

if [ $ONE -eq 1 ] && [ $TWO -eq 1 ] && [ $THREE -eq 1 ]
then
  exit 0 # interesting <= note this is for picire
else
  exit 1
fi