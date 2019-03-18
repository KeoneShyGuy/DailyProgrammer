# cython: language_level=3
#https://www.reddit.com/r/dailyprogrammer/comments/9z3mjk/20181121_challenge_368_intermediate_singlesymbol/
#compiled with python 3.5.3
from random import choice
from time import clock
   
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
    
def checkGrid(gridArr):
    oCorners = ['O', 'O', 'O', 'O']
    xCorners = ['X', 'X', 'X', 'X']

    length = 0
    allCorners = []

    while (length < arrSize):
        length += 1
        xIdx, yIdx = 0, 0
        while (arrSize and ((xIdx + length) < arrSize)):            
            while ((yIdx +length) < arrSize and (xIdx +length) < arrSize):
                corners = [gridArr[xIdx][yIdx], gridArr[xIdx][yIdx + length],
                           gridArr[xIdx + length][yIdx], gridArr[xIdx + length][yIdx + length]]
                if (corners == oCorners or corners == xCorners):
                    allCorners.append([xIdx, yIdx])
                    allCorners.append([xIdx, yIdx + length])
                    allCorners.append([xIdx + length, yIdx])
                    allCorners.append([xIdx + length, yIdx + length])
                yIdx += 1            
                if ((yIdx + length) == arrSize):
                    xIdx += 1
                    yIdx = 0
    filteredCorners = []
    for idx in allCorners:
        if (idx not in filteredCorners): filteredCorners.append(idx)

    allCorners = filteredCorners
    return allCorners

def fixGrid(gridArr, idxList):
    if (len(idxList) % 2 == 0):
        for idx in idxList[1::2]:
            if (gridArr[idx[0]][idx[1]] == 'X'): gridArr[idx[0]][idx[1]] = 'O'
            else: gridArr[idx[0]][idx[1]] = 'X'
            if not checkGrid(gridArr):
                break
    else:
        for idx in idxList[::2]:
            if (gridArr[idx[0]][idx[1]] == 'X'): gridArr[idx[0]][idx[1]] = 'O'
            else: gridArr[idx[0]][idx[1]] = 'X'
            if not checkGrid(gridArr):
                break            
    return gridArr

arrSize = abs(int(input('Enter the size of the array.\nEnter 0 to exit: ')))
startTime = clock()
grid = createGrid(arrSize)
attempts = 0
while arrSize:
    while checkGrid(grid):        
        if (attempts % (arrSize**2)== 0):
            grid = createGrid(arrSize)
        attempts += 1
        grid = fixGrid(grid, checkGrid(grid))
        if ((clock() - startTime) > 600):
            print("This taking too long! We out!")
            break
        
    print('Done in %i attempts and %.2f seconds!' % (attempts, clock() - startTime))
    printGrid(grid)
    arrSize = abs(int(input('Enter the size of the array.\nEnter 0 to exit: ')))
    startTime = clock()
    grid = createGrid(arrSize)
    attempts = 0
