#!/usr/bin/env python3
import argparse
import os

def delta_debugger(list, required, comand):
    if len(list) == 1:
        return list
    
    # split list in half into p1 and p2
    p1 = []
    p2 = []
    p1 = list[:len(list)//2]
    p2 = list[len(list)//2:]

    # make blank string to feed into ./is-intresting.sh
    stringP1R = ""
    stringP2R = ""
    
    # fill strings with necassrary values to run with ./is-intresting.sh and os
    for i in range (len(p1)):
        stringP1R = stringP1R + " " + str(p1[i])

    for x in range (len(p2)):
        stringP2R = stringP2R + " " + str(p2[x])

    for y in range (len(required)):
        stringP1R = stringP1R + " " + str(required[y])
        stringP2R = stringP2R + " " + str(required[y])
    
    print(comand + stringP1R)
    print(comand + stringP2R)
    # get exit code of each command
    if1 = os.waitstatus_to_exitcode(os.system(comand + stringP1R))
    if2 = os.waitstatus_to_exitcode(os.system(comand + stringP2R))

    # go through delta debugging steps depending on exit codes
    if if1 == 1:
        return delta_debugger(p1, required, comand)
    elif if2 == 1:
        return delta_debugger(p2, required, comand)
    else:
        return delta_debugger(p1, (required + p2), comand) + delta_debugger(p2, (required + p1), comand)
    

# create a command line argument parser and add commands
parser = argparse.ArgumentParser()
parser.add_argument("nArgs", help="The size n of the set to be minimized.")
parser.add_argument("intrestingDef", help="A command that determines if a given subset is interesting.")

# parse the command line arguments
args = parser.parse_args()

# make array of numbers up to number provided and set inital required to 0
numbers = []
init_required = []

# fill numbers array with all numbers up to inputed number
for i in range(0,int(args.nArgs),1):
    numbers.append(i)

# paramters now set up to run DD    
print(delta_debugger(numbers, init_required, args.intrestingDef))


