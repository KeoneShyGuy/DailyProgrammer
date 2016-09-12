from fractions import gcd

f = open("inputFractions.txt", "r")

def lineToNums(line):
	nums = line.split(' ')
	return map(int, nums)
	
def simplifyFraction(numList):
	numerator = numList[0]
	denominator = numList[1]
	divisor = gcd(numerator, denominator)
	for idx, num in enumerate(numList):
		numList[idx] = num / divisor
	return numList

for line in f:
	print simplifyFraction(lineToNums(line))	