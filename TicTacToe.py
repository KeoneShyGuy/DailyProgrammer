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
    xCheck, yCheck, lenCheck = False, False, False
    print(len(position))
    
    if (len(position) == 2):
        lenCheck = True
        print(lenCheck)
    
    if ((position[0].capitalize() in xKey) and lenCheck):
        x = xKey[position[0].capitalize()]
        xCheck = True        
    
    if (lenCheck):
        y = int(position[1])-1
        if (y >= 0 and y <= 2):
            yCheck = True
        
    if (xCheck and yCheck and lenCheck):
        if (arr[x][y] == '_'):
            arr[x][y] = mark
            return False
        else:
            print("There's already something there.\n")
            return True
    else:
        print('Coordinates not recognized. Please try again.\n')
        return True
    
def checkGrid(arr, bKeepGoing, mark):
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
            print(mark + ' is the WINNNER!')
            bKeepGoing = False
    return bKeepGoing

testGrid = createGrid(3)
turns = 0
bStillPlay = True

while bStillPlay:
    bSpotTaken = True    
    
    if ((turns % 2) == 0):
        playerMark = 'X'
    else:
        playerMark = 'O'    

    while bSpotTaken:
        playerChoice = input("Type a coordinate and press enter.\n" +
                             "Enter the let 'H' to show coordinates.\n")
        #printGrid(testGrid)
        if (playerChoice.capitalize() == 'H'):
            printGrid(helpGrid)
            turns -= 1
            break
        bSpotTaken = placeMark(playerChoice, playerMark, testGrid)
    # turn is still being updated and grid is still being
    # printed when the player enters an error
    printGrid(testGrid)
    bStillPlay = checkGrid(testGrid, bStillPlay, playerMark)
    turns += 1
