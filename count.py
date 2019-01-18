#!/usr/bin/env python
import sys
from itertools import islice
total=0

#
mystring="better"
with open(sys.argv[1], 'r') as myfile:
 for line in islice(myfile,1,10000):
   if mystring in line.split():
        total=total+1

#####
print total

