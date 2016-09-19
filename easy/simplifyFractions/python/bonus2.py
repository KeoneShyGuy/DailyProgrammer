# https://redd.it/4uhqdb
Bonus = open("bonusSource.txt", "r").readlines()

# first, we need to figure out how many variable there will be.
NumOfVars = int(Bonus[0])

# next, we should grab those variables and make a dictionary out of them
Vars = Bonus[1: NumOfVars + 1]
for idx, item in enumerate(Vars):
    Vars[idx] = item.rstrip("\n").split(" ")

VarDict = {}
for item in Vars:
    TempDict = {item[0]: item[1]}
    VarDict.update(TempDict)
# There's probably a more efficient and less readable way to do this. Whatever
# Now we replace the remaining lines with the variables if they have any
# let's make a list out of the fractions we're supposed to simplify
FractionList = []
for num in range(NumOfVars + 1, len(Bonus)):
    FractionList.append(Bonus[num].rstrip("\n").split(" "))
# sexy. Now we can replace the Fractions with their Equations
# I'll try to make a function so I can just call it when I need to
def replace_variables(Equate, dict__):
	c = 0
	while c < len(dict__):
		# use "c" to get a key from the dict. Then try and find that key in the string
		DictKey = dict__.keys()[c]
		LetterIdx = Equate.find(DictKey)
		# Messy. .find() returns -1 if the ite isn't found.
		# so if not found, move on. If it is found, resest and try again.
		if LetterIdx == -1:
			c += 1
		else:
			Equate = Equate.replace(DictKey, dict__[DictKey] )
			c = 0
	return Equate
# Fuck. Yes. Now I have to factor out the letters. Gross

# modify the FractionList piece by piece
for item in FractionList:
	for idx, fraction in enumerate(item):
		item[idx] = replace_variables(fraction, VarDict)
		# print fraction

print FractionList
