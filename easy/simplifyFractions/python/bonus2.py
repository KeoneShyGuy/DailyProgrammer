# https://redd.it/4uhqdb
Bonus = open("bonusSource.txt", "r").readlines()

# first, we need to figure out how many variable there will be.
NumOfVars = int(Bonus[0])

# next, we should grab those variables and make a dictionary out of them
Vars = Bonus[1: NumOfVars + 1]
for idx, item in enumerate(Vars):
    Vars[idx] = item.rstrip("\n").split(" ")


print Vars