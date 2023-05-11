#!/bin/bash

Ftemp=$1
Ftemp=$(echo Ftemp-"32" | bc -l)
echo $Ftemp
temp=$(echo 5/9 | bc -l)

Ctemp=$(echo $($temp*$Ftemp | bc -l))
