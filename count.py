#!/usr/bin/env python
import sys
from itertools import islice
count=0

#
mystring="better"
with open(sys.argv[1], 'r') as myfile:
 for line in islice(myfile,1,10000):
   if mystring in line.split():
#<<<<<<< HEAD
        count=count+line.count("better")
print float(count) 
#=======
#        total=total+1

#####
#print total
#>>>>>>> 7fe08254a8e3e7ca85d1cea88476b00415d469fd

