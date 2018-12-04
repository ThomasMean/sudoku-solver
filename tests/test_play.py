import imp
play = imp.load_source("play","play.py")

def test_loadEmpty_complete():
    assert play.loadEmpty(completeState) == []

def test_loadEmpty():
    assert play.loadEmpty(firstState) == [[0,0]]

def test_gameFinished_true():
    assert play.gameFinished(completeState) == True

def test_gameFinished_false():
    assert play.gameFinished(firstState) == False

def test_checkMove_successful():
    assert play.checkMove(0,0,firstState) == 1

def test_checkMove_fail():
    assert play.checkMove(0,1,firstState) == None

def test_makeMove_successful():
    assert play.makeMove(1,0,0,firstState) == completeState

def test_makeMove_fail():
    assert play.makeMove(1,0,1,firstState) == firstState

def test_CompleteGame():
    assert play.completeGame(firstState) == completeState

def test_CompleteHarderGame():
    assert play.completeGame(testState) == testCompleteState

def test_CompleteEvenHarderGame():
    assert play.completeGame(testHardState) == testHardCompleteState

def test_CompleteGame_isCompleted():
    assert play.completeGame(completeState) == completeState



firstState = [[None,2,3,4,5,6,7,8,9],[4,5,6,7,8,9,1,2,3],[7,8,9,1,2,3,4,5,6],[2,3,4,5,6,7,8,9,1],[5,6,7,8,9,1,2,3,4],[8,9,1,2,3,4,5,6,7],[3,4,5,6,7,8,9,1,2],[6,7,8,9,1,2,3,4,5],[9,1,2,3,4,5,6,7,8]]
completeState = [[1,2,3,4,5,6,7,8,9],[4,5,6,7,8,9,1,2,3],[7,8,9,1,2,3,4,5,6],[2,3,4,5,6,7,8,9,1],[5,6,7,8,9,1,2,3,4],[8,9,1,2,3,4,5,6,7],[3,4,5,6,7,8,9,1,2],[6,7,8,9,1,2,3,4,5],[9,1,2,3,4,5,6,7,8]]
testState = [[None,None,None,2,6,None,7,None,1],[6,8,None,None,7,None,None,9,None],[1,9,None,None,None,4,5,None,None],[8,2,None,1,None,None,None,4,None],[None,None,4,6,None,2,9,None,None],[None,5,None,None,None,3,None,2,8],[None,None,9,3,None,None,None,7,4],[None,4,None,None,5,None,None,3,6],[7,None,3,None,1,8,None,None,None]]
testCompleteState = [[4,3,5,2,6,9,7,8,1],[6,8,2,5,7,1,4,9,3],[1,9,7,8,3,4,5,6,2],[8,2,6,1,9,5,3,4,7],[3,7,4,6,8,2,9,1,5],[9,5,1,7,4,3,6,2,8],[5,1,9,3,2,6,8,7,4],[2,4,8,9,5,7,1,3,6],[7,6,3,4,1,8,2,5,9]]
testHardState = [[None,None,None,None,None,1,2,3,None],[1,2,3,None,None,8,None,4,None],[8,None,4,None,None,7,6,5,None],[7,6,5,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,1,2,3],[None,1,2,3,None,None,8,None,4],[None,8,None,4,None,None,7,6,5],[None,7,6,5,None,None,None,None,None]]
testHardCompleteState = [[6,5,7,9,4,1,2,3,8],[1,2,3,6,5,8,9,4,7],[8,9,4,2,3,7,6,5,1],[7,6,5,1,2,3,4,8,9],[2,3,1,8,9,4,5,7,6],[9,4,8,7,6,5,1,2,3],[5,1,2,3,7,6,8,9,4],[3,8,9,4,1,2,7,6,5],[4,7,6,5,8,9,3,1,2]]
