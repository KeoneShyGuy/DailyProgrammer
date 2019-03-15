#https://www.reddit.com/r/dailyprogrammer/comments/akv6z4/20190128_challenge_374_easy_additive_persistence/
import math

iterations = 1

print('Enter an integer: ')
startingInt = int(input())

while (startingInt < 10):
    print('Please enter a number larger than 10. I probably should have said that. My bad: ')
    startingInt = int(input())
    
powerOfTen = int(math.log10(startingInt))    
    
def getDigits(someInt):
    digits = []
    tempInt = someInt
    tenthPower = int(math.log10(tempInt))
    
    while (tenthPower >=0):
        minuend = pow(10, tenthPower) * (int(tempInt / math.pow(10, tenthPower)))
        tempInt -= minuend
        digits.append(int(minuend / math.pow(10, tenthPower)))
 
#        print("Tenth Power:", tenthPower, end=', ')
#        print("Minuend:", minuend, end=', ')
#        print("Current Int:", tempInt, end=', ')
#        print("Current Digits:", digits, end=".\n")
        tenthPower = tenthPower - 1
        
    return digits

def addDigits(intList):
    listSum = 0
    for digit in intList:
        listSum = listSum + digit
    return listSum

#print(addDigits(getDigits(startingInt)))
iteratedInput = (addDigits(getDigits(startingInt)))

while (iteratedInput >= 10):
    iteratedInput = (addDigits(getDigits(iteratedInput)))
    iterations = iterations + 1
    print ("Number of Iterations: ", iterations)
    print ("Final Sum: ", iteratedInput)

