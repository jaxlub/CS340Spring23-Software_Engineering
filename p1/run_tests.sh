#!/bin/bash

program=$1
for f in $(find tests/inputs -type f| sort -V )
do
    # splice out file number
    file_number=$(echo $f |cut -d "." -f1 | cut -d "_" -f2)

    # run data through desired program and store in text file
    timeout 3s $program $(find tests/inputs/$"test_$file_number.input") > AO_file.txt

    # access correct answer from the output files
    echo $(cut -f1 tests/outputs/$"test_$file_number.output") > EO_file.txt

    # Check if test passes
    if cmp -s $"EO_file.txt" $"AO_file.txt" 
    then
        # Test Passes
        echo "TEST $file_number: PASS"
    else 
        # Tests Fails
        echo "TEST $file_number: FAIL"
    fi
done
rm AO_file.txt
rm EO_file.txt
