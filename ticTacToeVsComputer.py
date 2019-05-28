import random
def printBoard(board):
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('---------')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('---------')
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])

def makeMoveComputer(board, move):
    board[move]= 'O'
def makeMovePlayer(board, move):
    board[move]='X'

def getRandInt():
    return random.randint(1,5)

def whoGoesFirst():
    if random.randint(0,1) ==0:
        return 'computer'
    else:
        return 'player'


def isWinner(bo, le):
    return ((bo[1]==le and bo[2]==le and bo[3]==le) or  #checks top row
            (bo[4]==le and bo[5]==le and bo[6]==le) or  #checks middle row
            (bo[7]==le and bo[8]==le and bo[9]==le) or  #checks bottom row
            (bo[1]==le and bo[4]==le and bo[7]==le) or  #checks left column
            (bo[2]==le and bo[5]==le and bo[8]==le) or  #checks middle column
            (bo[3]==le and bo[6]==le and bo[9]==le) or  #checks right column
            (bo[1]==le and bo[5]==le and bo[9]==le) or  #checks diagonal from top left
            (bo[3]==le and bo[5]==le and bo[7]==le))    #checks diagonal from top right

def getCopy(board):
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)

    return dupeBoard

def isSpaceFree(board, move):
    return board[move]==' '

def getPlayerMove(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move (1-9)')
        move = input()
    return int(move)

def chooseRandMove(board, moveList):
    possibleMoves = []
    for i in moveList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None
    
def getComputerMove(board):
    for i in range(1,10):
        copy = getCopy(board)
        if isSpaceFree(copy, i):
            makeMoveComputer(copy, i)
            if isWinner(copy, 'O'):
                return i

    for i in range(1,10):
        copy = getCopy(board)
        if isSpaceFree(copy, i):
            makeMovePlayer(copy, i)
            if isWinner(copy, 'X'):
                return i

    move = chooseRandMove(board, [1,3,5,7,9])
    if move != None:
        return move

    return chooseRandMove(board, [2,4,6,8])


def isBoardFull(board):
    for i in range(1,10):
        if isSpaceFree(board, i):
            return False
    return True

def percStarts(pstart, total):
    print("\n\n\n\n")


    
print('Welcome to Tic tac toe')
print('The spaces are numbered from top to bottom in this style:')
print(' 1 | 2 | 3 \n --------- \n 4 | 5 | 6 \n --------- \n 7 | 8 | 9')
wins=0
loss=0
draw=0
playerFirst = 0
totalGames = 0
while True:

    theBoard = [' '] * 10
    turn = whoGoesFirst()
    print("The " + turn + ' will go first.')
    totalGames +=1
    if turn == 'player':
        playerFirst +=1
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            printBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMovePlayer(theBoard, move)

            if isWinner(theBoard, 'X'):
                printBoard(theBoard)
                print("YOU WIN!!")
                wins +=1
                print('Total Stats: \n W: '+str(wins)+' %'+str(int(100*(wins/(wins+loss+draw))))+' \t \
                        L: ' +str(loss)+' %'+str(int(100*(loss/(wins+loss+draw))))+' \t \
                        D: ' +str(draw)+' %'+str(int(100*(draw/(wins+loss+draw))))+' \t')
                percStarts(playerFirst, totalGames)
                gameIsPlaying=False
            else:
                if isBoardFull(theBoard):
                    print("DRAW!")
                    draw +=1
                    print('Total Stats: \n W: '+str(wins)+' %'+str(int(100*(wins/(wins+loss+draw))))+' \t \
                        L: ' +str(loss)+' %'+str(int(100*(loss/(wins+loss+draw))))+' \t \
                        D: ' +str(draw)+' %'+str(int(100*(draw/(wins+loss+draw))))+' \t')
                    percStarts(playerFirst, totalGames)
                    gameIsPlaying=False
                    break
                else:
                    turn = 'computer'

        else:
            move = getComputerMove(theBoard)
            makeMoveComputer(theBoard, move)

            if isWinner(theBoard, 'O'):
                printBoard(theBoard)
                print("YOU LOST...")
                loss +=1
                print('Total Stats: \n W: '+str(wins)+' %'+str(int(100*(wins/(wins+loss+draw))))+' \t \
                        L: ' +str(loss)+' %'+str(int(100*(loss/(wins+loss+draw))))+' \t \
                        D: ' +str(draw)+' %'+str(int(100*(draw/(wins+loss+draw))))+' \t')
                percStarts(playerFirst, totalGames)
                gameIsPlaying=False
                gameIsPlaying=False
            else:
                if isBoardFull(theBoard):
                    print("DRAW!")
                    draw+=1
                    print('Total Stats: \n W: '+str(wins)+' %'+str(int(100*(wins/(wins+loss+draw))))+' \t \
                        L: ' +str(loss)+' %'+str(int(100*(loss/(wins+loss+draw))))+' \t \
                        D: ' +str(draw)+' %'+str(int(100*(draw/(wins+loss+draw))))+' \t')
                    percStarts(playerFirst, totalGames)
                    gameIsPlaying=False
                    break
                else:
                    turn = 'player'
