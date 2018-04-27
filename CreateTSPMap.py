# Town distances generator for towns placed randomly on a 2d map

# -------------------------------------------------------
# "BEER-WARE LICENSED":
# As long as you retain this notice, you can do what you
# want with this. If we meet some day, and you think this
# program is worth it, you may buy me a beer in return.
#
# Author: Clint Gamlin
# Email: cdgamlin@gmail.com
# -------------------------------------------------------

import sys
from math import sqrt
from random import random

if len(sys.argv)!=3:
	print "Error!: Incorrect arguments"
	print "Usage: python createmap.py NUMBER_OF_TOWNS MAX_DISTANCE"
	exit()

numTowns=int(sys.argv[1])
maxDist=int(sys.argv[2])

posTown=[(random()+1j*random())*maxDist/sqrt(2) for x in xrange (numTowns)]

print(numTowns)

for i in xrange(1,numTowns):
	for j in xrange(i):
		print int(abs(posTown[i]-posTown[j]))+1,
	print