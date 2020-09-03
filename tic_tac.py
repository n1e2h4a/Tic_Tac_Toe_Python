
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


print("Start a fresh game Tic Tac Toe!")

