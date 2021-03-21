#!/usr/local/bin/python3

## https://docs.python.org/3/
## https://pythonexamples.org/python-basic-examples/
## https://www.digitalocean.com/community/tutorial_series/how-to-code-in-python-3

import sys      # system library
import re       # regular expressions

# Define a dictionary
machines = {
    't2.small'  : { 'cpu':1, 'ram':2 },
    't2.medium' : { 'cpu':2, 'ram':4 },
    't2.large'  : { 'cpu':4, 'ram':8 }
}

if len(sys.argv) > 1:
    sizes = sys.argv[1:]
else:
    size = input("Enter a machine size(s) separated by commas: ")
    sizes = re.split('\s*[,]\s*',size)

# could also use 'for size in sizes.keys():'
for size in sizes:
    print ("Machine size(s) entered: {}".format(size))

# using ' '.join(list) creates a string with ' ' between each element in list
print ("Machine size(s) entered: {}".format(','.join(sizes)))

# test dict.get()
for size in sizes:
    if size in machines.keys():
        print ("Machine Size {} has {} CPU(s) and {} GB RAM.".format(size,machines[size]['cpu'],machines[size]['ram']))
    else:
        print ("Invalid machine size.")
