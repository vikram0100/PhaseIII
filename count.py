#!/usr/bin/env python
import sys
from itertools import islice

count=0.0

mystring="better"
with open(sys.argv[1], 'r') as myfile:
 for line in islice(myfile,1,10000):
   if mystring in line.split():
        count=count+line.count("better")
print float(count) 

