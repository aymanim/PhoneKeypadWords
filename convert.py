
# convert.py ##########

# Takes the number you supplied and produces possible words for it


import sys
import copy

def getnum(stringform):
	return ord(stringform) - 48

def printtable(table):
	print "xxxxxxxxxxxxxxxxxxxx"
	for t in table:
		print " ===>",t
	print "xxxxxxxxxxxxxxxxxxxx"


def printlen(size):
	for i in range(length):
		if not len(table[i][size]) == 0:
			for s in table[i][size]:
				print "".join(s) 
			

vals = [
		[], # shift indices to make vals[0] to 1 on keypad
		[],
		["a","b","c"],
		["d","e","f"],
		["g","h","i"],
		["j","k","l"],
		["m","n","o"],
		["p","q","r","s"],
		["t","u","v"],
		["w","x","y","z"],
		]


snumber = 0
letters = []
number = []
# get the argument from the command line

if (len(sys.argv)) == 1:
	snumber = 12345
else:
	snumber = sys.argv[1]


# iterate over the string

for c in snumber:
	print getnum(c), vals[getnum(c)]
	a = getnum(c)
	number.append(a)
	letters.append(vals[a])

#print number
print letters

# algorithm: classic dynamic programming problem

# words of one length


# initialize the table
length = len(letters)
table = [ [[] for x in range(length+1)] for y in range(length)]


# iterate over the letters array
for i in range(length):
	#print " <<<<<<<  I IS ", i, 
	# solutions for the i'th letter
	solutioni = []
	#print "solution is ", solutioni
	#print " BEFORE  "

	# for all the letters at the i'th position
	for c in letters[i]:
		#print " C is ", c
		# prepare template
		solution = [""] * length
		# set the i'th letter to that solution
		for j in range(length):
			if j == i:
				solution[j] = c
		# append this to the list of solutions for 
		#print " ----- ", solution
		solutioni.append(solution)
	table[i][1] = solutioni



# fill the rest of the table




for j in range(2, length+1):
	for i in range(length):
		solution = []
		# i,j = merge(  i,j-1   x   j-1, 1 )
		if not j-1 == i:
			for g in table[i][j-1]:
				# look at the elements from one before
				for a in table[j-1][1]:
					#print "=",i,j,"YY", g, a
					x = copy.copy(g)
					x[j-1] = a[j-1] # position, length conversion
					#print " ><", x
					solution.append(x)
			table[i][j] = solution






printlen(2)
printlen(3)
printlen(4)
printlen(5)