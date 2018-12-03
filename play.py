import imp
import time
gamestate = imp.load_source("","gamestate.py")
gamescreen = imp.load_source("","gamescreen.py")

def completeGame(state):
    moveCount = 0
    while not gamestate.gameFinished(state):
        for xValue in range(9):
            for yValue in range(9):
                if state[xValue][yValue] is None:
                    move = gamestate.getMoveCheck([xValue, yValue], state)
                    if move is not None:
                        state = gamestate.add(move,[xValue, yValue],state)
                        moveCount += 1
    return state
