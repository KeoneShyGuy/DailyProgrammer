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

print FractionList
