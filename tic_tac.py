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

