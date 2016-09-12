"""
simplifyFractions.py
Created by: Keone Robinson
Date: 08/08/2016
"""
# read a file, take 2 numbers from each line, make simple fraction

fractions = open("inputFractions.txt", "r")

def simplifyFractions(strLine):
	line = strLine
	# split() returns a list that's splice and the given parameter
	nums = line.split(' ')
	# map() changed the items in a list into another type
	nums = map(int, nums)
	numerator =nums[0]
	denominator = nums[1]
	# divide between 2 and the numerator and add the even divisibles to a list
	numerDivisibles = []
	denomDivisibles = []
	for x in range(2, (numerator + 1)):
		if numerator % x == 0:
			numerDivisibles.append(x)
			numerDivisibles.sort()
			numerDivisibles.reverse()
	for y in range(2, (denominator + 1)):
		if denominator % y == 0:
			denomDivisibles.append(y)
			denomDivisibles.sort()
			denomDivisibles.reverse()
	# figure out which number is gonna divide which
	if numerator < denominator:
		isProperFraction = True
	else:
		isProperFraction = False
	# find the GCF
	if isProperFraction:
		for bigFactor in denomDivisibles:
			for smallFactor in numerDivisibles:
				if bigFactor == smallFactor:
					gcf = smallFactor
					return ((numerator / gcf), (denominator / gcf))
	else:
		for bigFactor in numerDivisibles:
			for smallFactor in denomDivisibles:
				if bigFactor == smallFactor:
					gcf = smallFactor
					return ((numerator / gcf), (denominator / gcf))
	return (numerator, denominator)

for line in fractions:		
	print simplifyFractions(line)
		
fractions.close()