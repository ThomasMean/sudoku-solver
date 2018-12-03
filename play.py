import imp
import time
gamestate = imp.load_source("","gamestate.py")
gamescreen = imp.load_source("","gamescreen.py")

def completeGame(state):
    while not gamestate.gameFinished(state):
        for xValue in range(9):
            for yValue in range(9):
                checkMove(xValue,yValue,state)
    return state

def checkMove(xValue,yValue,state):
    if state[xValue][yValue] is None:
        move = gamestate.getMoveCheck([xValue, yValue], state)
        if move is not None:
            state = gamestate.add(move,[xValue, yValue],state)
    return state
