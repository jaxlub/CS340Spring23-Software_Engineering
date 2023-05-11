#!/bin/bash

#download NYT COVID data and print report for given state

#make a temp file to store covid data
temp_file=$(mktemp)


#get data and -k avoids certificate checks and -o allows specification of file
curl -s -k -o $temp_file https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv


# ask user for state
# echo "enter a state:"
# read state

#state=$1 #set paramter for file

# error check something was entered
if [ -z $state ]
then
    echo "Usage: $0 state"
    rm $temp_file
    exit 1
fi

# error check valid state
#exclude header line from this and can use tail to specify
state_check=$(tail +2 "$temp_file" | cut -d , -f 2 | grep -i "$state")
if [ -z "$state_check" ]
then 
    echo "No data for $state"
    rm $temp_file
    exit 2
fi

echo "COVID cases and death for $state"
head -n 1 $temp_file | cut -d , -f 1,4-5


# calculate daily cases/death from cumulative data
# everything is set as string variable so int must be specified
prev_cases=$((0))
prev_deaths=$((0))


#use greb to filter for this state
for entry in $(grep -i "$state" "$temp_file" | cut -d , -f 1,4-5)
do
    #entry is single line for the data
    date=$(echo $entry | cut -d , -f 1)
    cases=$(echo $entry | cut -d , -f 2)
    deaths=$(echo $entry | cut -d , -f 3)
    echo $date,$((cases-prev_cases)),$((deaths-prev_deaths))

    prev_cases=$cases
    prev_deaths=$deaths
done

#remove temp file when done 
rm $temp_file
