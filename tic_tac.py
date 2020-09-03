
def myBoard(tiles):
    # "board" is a list of 10 strings representing the board (ignore index 0)
    print(' ' + tiles[7] + ' | ' + tiles[8] + '  | ' + tiles[9])
    print('---+----+---')
    print(' ' + tiles[4] + ' | ' + tiles[5] + '  | ' + tiles[6])
    print('---+----+---')
    print(' ' + tiles[1] + ' | ' + tiles[2] + '  | ' + tiles[3])



def inputPlayerSymbol():
    # Player will decide which symbol he/she prefer

    Symbol = ''

    while not (Symbol == 'X' or Symbol == 'O'):
        print('what are you want to take X or O?')
        Symbol = input().upper()

    # Returns a list with the player’s symbol and the computer's symbol.

    if Symbol == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def Toss():
    # Randomly choose the player who will play first.
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def isSpaceFree(tiles, move):
    # Return true if the passed move is free on the passed board.
    return tiles[move] == ' '


def PlayerMove(tiles):
    # Let the player type in their move.
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(tiles, int(move)):
        try:
            print('What is your next move? (1-9)')
            move = input()
            return int(move)

        except ValueError:

         print('That\'s not a valid number, try again.\n')


def ComputerMove(tiles, computerSymbol):
    # Given a board and the computer's letter, determine where to move and return that move.
    if computerSymbol == 'X':
        playerSymbol = 'O'
    else:
        playerSymbol = 'X'

 # First, check if we can win in the next move
    for i in range(1, 10):
        copy = tilesCopy(tiles)
        if isSpaceFree(copy, i):
            firstMove(copy, computerSymbol, i)
            if isWinner(copy, computerSymbol):
                return i
                # Check if the player could win on their next move, and block them.
    for i in range(1, 10):
         copy = tilesCopy(tiles)
         if isSpaceFree(copy, i):
             firstMove(copy, playerSymbol, i)
             if isWinner(copy, playerSymbol):
                 return i


        # Try to take one of the corners, if they are free.
    move = chooseRandomMoveFromList(tiles, [1, 3, 7, 9])
    if move != None:
        return move
    # Try to take the center space, if it is free.
    if isSpaceFree(tiles, 5):
        return 5
    # if corner and center not free Move on one of the sides.
    return chooseRandomMoveFromList(tiles, [2, 4, 6, 8])



print("Start a fresh game Tic Tac Toe!")


while True:
    # Reset the board
    theBoard = [' '] * 10
    playerSymbol, computerSymbol = inputPlayerSymbol()
    turn = Toss()
    print('The ' + turn + ' will play first.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            # Player’s turn.
            myBoard(theBoard)
            move = PlayerMove(theBoard)
            firstMove(theBoard, playerSymbol, move)
            if isWinner(theBoard, playerSymbol):
                myBoard(theBoard)
                print('Heyyyy! You won the game!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    myBoard(theBoard)
                    print('no win no lose ...tie!')
                    break
                else:
                    turn = 'computer'
        else:
            # Computer’s turn.
            move = ComputerMove(theBoard, computerSymbol)
            firstMove(theBoard, computerSymbol, move)
            if isWinner(theBoard, computerSymbol):
                myBoard(theBoard)
                print('The computer has won the game! You lose.')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    myBoard(theBoard)
                    print('no win no lose ...tie!')
                    break
                else:
                    turn = 'player'


