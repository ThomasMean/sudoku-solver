import math

def add(input, position, state):
    if (validMove(input, position, state)):
        state[position[0]][position[1]] = input
    return state

def validMove(input, position, state):
    return checkHorizontal(input, position, state) and checkVertical(input, position, state) and checkSquare(input, position, state)

def checkHorizontal(input, position, state):
    for value in state[position[0]]:
        if (value == input):
            return False
    return True

def checkVertical(input, position, state):
    for x in range(8):
        if (state[x][position[1]]) == input:
            return False
    return True

def checkSquare(input, position, state):
    for xValue in getSquareValues(position[0]):
        for yValue in getSquareValues(position[1]):
            if (state[xValue][yValue]) == input:
                return False
    return True

def getSquareValues(input):
    if (input in range(3)):
        return [0,1,2]
    if (input in range(3,6)):
        return [3,4,5]
    return [6,7,8]

def getMoveCheck(position, state):
    move = []
    for input in range(1,10):
        if validMove(input, position, state):
            move.append(input)
    if (len(move) != 1):
        return None
    return move[0]
