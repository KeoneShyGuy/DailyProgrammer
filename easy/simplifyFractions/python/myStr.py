# Get the index from a for loop.

myStr = "Say something now bitch!"

myStr = myStr.replace('s', 'lol')
equations = {'y': 'ab\n', 'x': 'cb\n', 'z': 'xa\n'}
variableKeys = []
varList = [['ab', 'cb\n'], ['ab', 'x\n'], ['x', 'y\n'], ['z', 'y\n'], ['z', 'xay']]
for key in equations:
	variableKeys.append(key)

for item in varList:
	for idx, s in enumerate(item):
		c = 0
		g = 0
		numOfChecks = len(variableKeys)
		while s.find(variableKeys[c], equations[variableKeys[c]]) != -1 and g <= numOfChecks:
			print "Found it!"
			item[idx] = s.replace(variableKeys[c], equations[variableKeys[c]])
			if c == numOfChecks:
				g += 1
				c = 0
			else:
				c += 1
			
	
print myStr
print equations['z']
print variableKeys
print varList
