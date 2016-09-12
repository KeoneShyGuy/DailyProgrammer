bonus = open("bonusSource.txt", "r")

numOfVariables = 0

# get variables from the file
def getVariables(bonusFile):
	global numOfVariables # changes the value of the variable globally. Didn't want to re-write function
	global bonusLines
	# readlines turns all the lines in a file into a list when left blank
	bonusLines = bonusFile.readlines()
	# the number of variables present is in the first line
	numOfVariables = int(bonusLines[0])
	# use numOfEquestion to convert next lines into dictionary
	count = 1
	variables = []
	while count <= numOfVariables:
		currentVariable = bonusLines[count].split(' ')
		count += 1
		variables.append(currentVariable)
	variables = dict(variables)
	return variables	

# get the equations from the file and turn them into something useful
def getEquations(bonusFile):
	count = numOfVariables + 1
	equations = []
	while count < len(bonusLines):
		currentEquation = bonusLines[count].split(' ')
		equations.append(currentEquation)
		count += 1
	return equations
	
vars = getVariables(bonus)
eqs = getEquations(bonus)
	
# convert the equations if they have variables in them
def convertEquations(bonusFile):	
	variableKeys = []
	for key in vars:
		variableKeys.append(key)	
	for item in eqs:
	#find a smart way to see is a variable is in the string over and over again until nothing is left
		for idx, s in enumerate(item):
			c = 0
			# while c < numOfVariables:
			if s.find(variableKeys[c]) != -1:
				print "Found it!"
				print "Replacing %s with %s" % (variableKeys[c], vars[variableKeys[c]])
				item[idx] = s.replace(variableKeys[c], vars[variableKeys[c]])
				# c += 1
			# else:
				# c += 1
	return eqs
	
print vars
print eqs
print convertEquations(bonus)

bonus.close()