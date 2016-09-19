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


def replace_variables(equate, dict__):
    c = 0
    while c < len(dict__):
        # use "c" to get a key from the dict. Then try and find that key in the string
        dict_key = dict__.keys()[c]
        letter_idx = equate.find(dict_key)
        # Messy. .find() returns -1 if the ite isn't found.
        # so if not found, move on. If it is found, reset and try again.
        if letter_idx == -1:
            c += 1
        else:
            equate = equate.replace(dict_key, dict__[dict_key])
            c = 0
    return equate


# Fuck. Yes. Now I have to factor out the letters. Gross
def factor_letters(numerator, denominator):
    # shorter_var = numerator if (len(numerator) < len(denominator)) else denominator
    # print shorter_var
    c = 0
    while c < len(denominator):
        current_var = denominator[c]
        var_idx = numerator.find(current_var)
        if var_idx == -1:
            c += 1
        else:
            numerator = numerator.replace(current_var, "", 1)
            denominator = denominator.replace(current_var, "", 1)
            c = 0
    if len(numerator) == 0:
        numerator = "1"
    if len(denominator) == 0:
        denominator = "1"
    return numerator, denominator


# modify the FractionList piece by piece
for item in FractionList:
    for idx, fraction in enumerate(item):
        item[idx] = replace_variables(fraction, VarDict)
    item[0], item[1] = factor_letters(item[0], item[1])

print "Input"

for line in Bonus:
    print line.rstrip("\n")

print "\n\nOutput"

for item in FractionList:
    print item[0] + " " + item[1]