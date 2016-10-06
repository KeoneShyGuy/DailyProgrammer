"""
/r/DailyProgrammer
Reverse Factorial
By Keone Robinson
https://redd.it/55nior
"""
# make a factorial function for shits and giggles

ChallengeInput = [3628800, 479001600, 6, 18]

def make_factorial(num__):
    product = 1
    for num in range(num__):
        product *= num+1
    return product
    
# print make_factorial(16)

# alrighty, that works

def reverse_factorial(int__):
    quotient = int(int__)
    count = 2
    temp = 0
    while quotient != 1:
        temp = quotient
        if quotient % count != 0:
            return "NONE"
        quotient = quotient / count
        count += 1 
    else:
        return "{}!".format(temp)
        
for num in ChallengeInput:
    print "{} = {}".format(num, reverse_factorial(num))
