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
    print('\n ')
    
#checks the corners of squares and calls fixGrid
#and call fixGrid if all points match up.
def checkGrid(gridArr):
    oCorners = ['O', 'O', 'O', 'O']
    xCorners = ['X', 'X', 'X', 'X']

    length = 0
    #xIdx, yIdx = 0, 0
    allCorners = []

    while (length < arrSize):
        length += 1
        xIdx, yIdx = 0, 0
        while (arrSize and ((xIdx + length) < arrSize)):
            bFoundSquare = False
            
            while ((yIdx +length) < arrSize and (xIdx +length) < arrSize):
                corners = [gridArr[xIdx][yIdx], gridArr[xIdx][yIdx + length],
                           gridArr[xIdx + length][yIdx], gridArr[xIdx + length][yIdx + length]]
                if (corners == oCorners or corners == xCorners):
                    #bFoundSquare = True
                    allCorners.append([xIdx, yIdx])
                    allCorners.append([xIdx, yIdx + length])
                    allCorners.append([xIdx + length, yIdx])
                    allCorners.append([xIdx + length, yIdx + length])
                yIdx += 1            
                if ((yIdx + length) == arrSize):
                    xIdx += 1
                    yIdx = 0
            #print('Full Check Complete')
            if bFoundSquare:
                print('These corners match at length %d bruh:' % length, end='')
                for address in allCOrners:
                    print (address, end=",")

    filteredCorners = []
    for idx in allCorners:
        if (idx not in filteredCorners): filteredCorners.append(idx)
        #else: print('old')

    allCorners = filteredCorners
    #print(allCorners)
    return allCorners

#fixes the grid by switching to another character
#and calling checkGrid. May not be needed.
def fixGrid(gridArr, idxList):
    if (len(idxList) % 2 == 0):
        #print('even')
        for idx in idxList[1::2]:
            if (gridArr[idx[0]][idx[1]] == 'X'): gridArr[idx[0]][idx[1]] = 'O'
            else: gridArr[idx[0]][idx[1]] = 'X'
            if not checkGrid(gridArr):
                #print('break')
                break
    else:
        #print('odd')
        for idx in idxList[::2]:
            if (gridArr[idx[0]][idx[1]] == 'X'): gridArr[idx[0]][idx[1]] = 'O'
            else: gridArr[idx[0]][idx[1]] = 'X'
            if not checkGrid(gridArr):
                #print('break')
                break
            
    return gridArr

arrSize = abs(int(input('Enter the size of the array.\nEnter 0 to exit: ')))

grid = createGrid(arrSize)
printGrid(grid)
attempts = 0
while checkGrid(grid):
    if (attempts % 64== 0):
        grid = createGrid(arrSize)
        print('REDO # ', (attempts // 64))
    attempts += 1
    grid = fixGrid(grid, checkGrid(grid))
    
print('Done in %i attempts!' % attempts)
printGrid(grid)
