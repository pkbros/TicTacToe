boardData = {
    '0' : ['_','0'],
    '1' : ['_','1'],
    '2' : ['_','2'],
    '3' : ['_','3'],
    '4' : ['_','4'],
    '5' : ['_','5'],
    '6' : ['_','6'],
    '7' : ['_','7'],
    '8' : ['_','8'],
    '9' : ['_','9'],
}

board = [[str(i * 3 + j) for j in range(3)] for i in range(3)]

movesLeft = 9
def getMoves():
    return movesLeft
def setMoves(m):
    global movesLeft
    movesLeft = m

currentPlayer = 'p1'
def getPlayer():
    return currentPlayer
def setPlayer(p):
    global currentPlayer
    currentPlayer = p

def resetBoard():
    global boardData
    global movesLeft
    movesLeft = 9
    boardData = {
    '0' : ['_','0'],
    '1' : ['_','1'],
    '2' : ['_','2'],
    '3' : ['_','3'],
    '4' : ['_','4'],
    '5' : ['_','5'],
    '6' : ['_','6'],
    '7' : ['_','7'],
    '8' : ['_','8'],
    '9' : ['_','9'],
}
    

def checkWin(currentSymbol):
    # print("herasd;fkja", currentSymbol)
    if boardData['0'][0] == currentSymbol  and boardData['1'][0] == currentSymbol and boardData['2'][0] == currentSymbol:
        return True
    elif  boardData['3'][0] == currentSymbol  and boardData['4'][0] == currentSymbol and boardData['5'][0] == currentSymbol:
        return True
    elif  boardData['6'][0] == currentSymbol  and boardData['7'][0] == currentSymbol and boardData['8'][0] == currentSymbol:
        return True
    elif  boardData['0'][0] == currentSymbol  and boardData['3'][0] == currentSymbol and boardData['6'][0] == currentSymbol:
        return True
    elif  boardData['1'][0] == currentSymbol  and boardData['4'][0] == currentSymbol and boardData['7'][0] == currentSymbol:
        return True
    elif  boardData['2'][0] == currentSymbol  and boardData['5'][0] == currentSymbol and boardData['8'][0] == currentSymbol:
        return True
    elif  boardData['0'][0] == currentSymbol  and boardData['4'][0] == currentSymbol and boardData['8'][0] == currentSymbol:
        return True
    elif  boardData['6'][0] == currentSymbol  and boardData['4'][0] == currentSymbol and boardData['2'][0] == currentSymbol:
        return True
    
    return False


