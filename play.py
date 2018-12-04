import imp
import time
gamestate = imp.load_source("","gamestate.py")
gamescreen = imp.load_source("","gamescreen.py")

def completeGame(state):
    emptySquares = loadEmpty(state)
    while not gameFinished(state):
        for position in emptySquares:
            xValue = position[0]
            yValue = position[1]
            move = checkMove(xValue,yValue,state)
            if move is not None:
                state = makeMove(move, xValue, yValue, state)
    return state

def checkMove(xValue,yValue,state):
    if state[xValue][yValue] is None:
        return gamestate.getMoveCheck([xValue, yValue], state)
    return None

def makeMove(move,xValue,yValue,state):
    state = gamestate.add(move,[xValue, yValue],state)
    return state

def loadEmpty(state):
    nonEmpty = []
    for xValue in range(9):
        for yValue in range(9):
            if state[xValue][yValue] is None:
                nonEmpty.append([xValue,yValue])
    return nonEmpty

def gameFinished(state):
    if loadEmpty(state) == []:
        return True
    return False
