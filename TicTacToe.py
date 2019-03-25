#!/usr/bin/env python3

helpGrid = (('A1', 'A2', 'A3'),
            ('B1', 'B2', 'B3'),
            ('C1', 'C2', 'C3'))

def printGrid(someList):
    for rowB in someList:
        for char in rowB:
            print (char, end=' ')
        print('')
    print('\n')
    
def createGrid(gridSize, defaultFill='_'):
    grid = [[defaultFill] * gridSize for j in range(gridSize)]
    return grid

def placeMark(position, mark, arr):
    xKey = {'A': 0, 'B':1, 'C': 2}
    x =  xKey[position[0].capitalize()]
    y = int(position[1]) - 1
    arr[x][y] = mark
    
def checkGrid(arr, bKeepGoing):
    lineOne = (arr[0][0], arr[0][1], arr[0][2])
    lineTwo = (arr[1][0], arr[1][1], arr[1][2])
    lineThree = (arr[2][0], arr[2][1], arr[2][2])
    lineFour = (arr[0][0], arr[1][0], arr[2][0])
    lineFive = (arr[0][1], arr[1][1], arr[2][1])
    lineSix = (arr[0][2], arr[1][2], arr[2][2])
    lineSeven = (arr[0][0], arr[1][1], arr[2][2])
    lineEight = (arr[0][2], arr[1][1], arr[2][0])    
    allLines = (lineOne, lineTwo, lineThree, lineFour,
               lineFive, lineSix, lineSeven, lineEight)
    
    for line in allLines:
        if ((line[0] == line[1] == line[2]) and line[0] != '_'):
            print('WINNNER!')
            bKeepGoing = 0

testGrid = createGrid(3)
turns = 0
bStillPlay = 1

while bStillPlay:    
    playerChoice = input("Type a coordinate and press enter.\n" +
                         "Enter the let 'H' to show coordinates.\n")
    if (playerChoice.capitalize() == 'H'):
        printGrid(helpGrid)

    printGrid(testGrid)
    print(turns)
    if ((turns % 2) == 0):
        placeMark(playerChoice, 'X', testGrid)
    else:
        placeMark(playerChoice, 'O', testGrid)
    printGrid(testGrid)
    checkGrid(testGrid, bStillPlay)
    turns += 1
