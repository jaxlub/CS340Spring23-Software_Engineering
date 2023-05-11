Project Design and Implementation
My program meets all of the designated requirments. It takes a path to a program and then loops
through the given input files and compares the expected outputs to the actual outputs when the 
inputs are passed through. Initially the biggest problem I came across was how to run the input
files through the given program, mainly due to the formatting needed to pass the output into a 
new file (used later for the comparison). In addition, implementation of the timeout method was
needed to insure that when a failed file input was given the loop would still return the correct
(Fail) output and still iterate over the rest. Another design problem I came across was the file
comparison at the end of the for-loop. Initialy I used diff but diff has addiitonal text outputs
when the two files are not the same (I did not see a silent form in the man) but I used compare 
-s instead. This does the same comparison but with the -s does not print anything to the output,
thus allowing us to display the sole message of test passed/failed. 

Bug Analysis
The test cases that fail fall on leap years, this leads me to belive that the aditional day 
every 4 years was not accounted for in the program. This leads to the year given (if it does
not exceed run time of 3 seconds) to be given as the previous year such as in Test 61 where 
the expected date is 2301 but 2300 is returned. Some of the test outputs return the wrong year
(off by one) while some of the leap years fail the time limit, though why this occurs could be
due to a variety of reasons. 