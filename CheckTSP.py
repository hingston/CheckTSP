# Brute force the best distance for a given map

# -------------------------------------------------------
# "BEER-WARE LICENSED":
# As long as you retain this notice, you can do what you
# want with this. If we meet some day, and you think this
# program is worth it, you may buy me a beer in return.
#
# Author: Clint Gamlin
# Email: cdgamlin@gmail.com
# -------------------------------------------------------

from sys import argv

class Map:
	# read and store distance map, checking for correct file structure
	def __init__(self,filename):
		#read in file in one hit
		filename=argv[1]
		file=open(filename)
		data=file.read()
		file.close()

		# split data into list of lists
		data=data.split("\n")
		data=[x.split() for x in data]
		data=[[int(y) for y in x] for x in data]

		# remove trailing blank lines
		while data[-1]==[]:
			data=data[:-1]

		#get number of towns, making sure the first line is structured correctly
		if len(data[0])!=1:
			print "Error! Map file line 1 must have exactly 1 integer"
			exit()
		self.numTowns=data[0][0]

		# check that the size of the file is correct
		if len(data)!=self.numTowns:
			print "Error!: Map file must have the same number of input lines as the number of towns"
			exit()

		error=False

		# check structure of distances between towns
		for i in xrange(1,self.numTowns):
			if len(data[i])!=i:
				print "Error! Map file line "+str(i+1)+" must have exactly "+str(i)+" integer"+("s" if i!=1 else "")
				error=True
			for j in xrange(i):
				if data[i][j]<1:
					print "Error! Map file line "+str(i+1)+" integer "+str(j+1)+" is not an integer greater than zero"
					error=True

		if error:
			exit()

		# store distance map
		self.distance=data[1:]

	# return distance between two towns
	def getDist(self,i,j):
		return self.distance[max(i,j)-1][min(i,j)]

	# find best path from current town through all left2visit towns using recursion
	def bestPath(self,currentTown,left2visit):
		# base case
		if len(left2visit)==1:
			return self.getDist(currentTown,left2visit[0])

		# general case
		bestDist=float('inf') # infinite!
		for i in xrange(len(left2visit)):
			goingTo=left2visit[i]
			thenLeft2visit=left2visit[:i]+left2visit[i+1:]
			dist=self.getDist(currentTown,goingTo)+self.bestPath(goingTo,thenLeft2visit)
			if dist<bestDist:
				bestDist=dist
		return bestDist

### MAIN STARTS HERE ###

if len(argv)!=2:
	print "Error!: Incorrect arguments"
	print "Usage: python checkTSP.py MAP_FILE_NAME"
	exit()

filename=argv[1]
map=Map(filename)
currentTown=0
left2visit=range(1,map.numTowns)
print(map.bestPath(currentTown,left2visit))