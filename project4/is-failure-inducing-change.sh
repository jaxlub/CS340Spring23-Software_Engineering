#!/bin/bash
cd wireworld-example
cat wireworld-original.c > temp.c  # store the original to revert back to later
for i in $* # $* is a list of all the patch file numbers
do
  #apply the patchs
  applying=$(echo patch.$i)
  echo $applying
  cat $applying | patch -p0 wireworld-original.c 
done

# see if it compiles and store exit code
gcc wireworld-original.c
result=$(echo $?)

# revert back to original and remove temp file
rm wireworld-original.c
cat temp.c > wireworld-original.c
rm temp.c

# if exit code is 1 then set of patches is intresting
if [ $result -eq 1 ]
then
  exit 1 # interesting
fi
exit 0 # not intresting