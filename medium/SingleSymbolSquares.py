#!/usr/bin/env python3
#https://www.reddit.com/r/dailyprogrammer/comments/9z3mjk/20181121_challenge_368_intermediate_singlesymbol/
from random import choice
from math import floor
   
def createGrid(gridSize):
    gridOG = [['U'] * gridSize for j in range(gridSize)]
    
    for j in range(len(gridOG)):
        columnTemp = []
        countA = 0
        while (countA < gridSize):
            columnTemp.insert(len(columnTemp), choice(['X','O']))
            countA += 1
        gridOG[j] = columnTemp
    return gridOG

def printGrid(someList):
    for rowB in someList:
        for char in rowB:
            print (char, end=' ')
        print('')
        
#checks the corners of squares and calls fixGrid
#and call fixGrid if all points match up.
#def checkGrid(gridArray):

#fixes the grid by switching to another character
#and calling checkGrid. May not be needed.
#def fixGrid(gridArr):

arrSize = abs(int(input('Enter the size of the array.\nEnter 0 to exit:')))

grid = createGrid(arrSize)
printGrid(grid)
#print(len(grid))    

oCorners = ['O', 'O', 'O', 'O']
xCorners = ['X', 'X', 'X', 'X']

length = 1
xIdx, yIdx = 0, 0

while (arrSize and ((xIdx + length) < arrSize)):
    
    while ((yIdx +length) < arrSize and (xIdx +length)):
        print('(%i, %i)' % (xIdx, yIdx))
        corners = [grid[xIdx][yIdx], grid[xIdx][yIdx + length],
                   grid[xIdx + length][yIdx], grid[xIdx + length][yIdx + length]]
        #print(corners)
    #for xIdx, row in enumerate(grid):
        #print(xIdx)
        #for 
        #corners = [grid[xIdx][xIdx], grid[xIdx][xIdx+length],
               #grid[xIdx+length][xIdx], grid[xIdx+length][xIdx+length]]
        #print(corners)
        if (corners == oCorners or corners == xCorners):
            print('These corners match bruh')
        yIdx += 1            
        #arrSize = abs(int(input('Enter the size of the array.\nEnter 0 to exit:')))
        #grid = createGrid(arrSize)
        #printGrid(grid)
        if ((yIdx + length) == arrSize):
            print('End of Row!')
            xIdx += 1
            yIdx = 0
     
#if (grid[0][0] == grid[0][1]):
#    print ('True')    