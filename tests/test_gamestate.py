import pytest
import imp
gamestate = imp.load_source("gamestate","gamestate.py")


def test_validMove_isValid():
    assert gamestate.validMove(1, [0,0], firstState) == True

def test_validMove_isInvalid():
    assert gamestate.validMove(2, [0,0], firstState) == False

def test_checkVertical_isValid():
    assert gamestate.checkVertical(1, [0,0], firstState) == True

def test_checkVertical_isInvalid():
    assert gamestate.checkVertical(2, [0,0], firstState) == False

def test_checkHorizontal_isValid():
    assert gamestate.checkHorizontal(1, [0,0], firstState) == True

def test_checkHorizontal_isInvalid():
    assert gamestate.checkHorizontal(2, [0,0], firstState) == False

def test_checkSquare_isValid():
    assert gamestate.checkSquare(1, [0,0], firstState) == True

def test_checkSquare_isInvalid():
    assert gamestate.checkSquare(2, [0,0], firstState) == False

def test_add_successful():
    assert gamestate.add(1, [0,0], firstState) == newState

def test_add_fail():
    assert gamestate.add(2, [0,0], firstState) == firstState

firstState = [[None,2,3,4,5,6,7,8,9],[2,3,4,5,6,7,8,9,1],[3,4,5,6,7,8,9,1,2],[4,5,6,7,8,9,1,2,3],[5,6,7,8,9,1,2,3,4],[6,7,8,9,1,2,3,4,5],[7,8,9,1,2,3,4,5,6],[8,9,1,2,3,4,5,6,7],[9,1,2,3,4,5,6,7,8]]
newState = [[1,2,3,4,5,6,7,8,9],[2,3,4,5,6,7,8,9,1],[3,4,5,6,7,8,9,1,2],[4,5,6,7,8,9,1,2,3],[5,6,7,8,9,1,2,3,4],[6,7,8,9,1,2,3,4,5],[7,8,9,1,2,3,4,5,6],[8,9,1,2,3,4,5,6,7],[9,1,2,3,4,5,6,7,8]]
