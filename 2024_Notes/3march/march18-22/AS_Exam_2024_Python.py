import random

Board = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0],
         [0,0,0,0],
         ]
PlayerOneName = ""
PlayerTwoName = ""
XCoord = 0
YCoord = 0
NoOfMoves = 0
ValidMove = False
GameHasBeenWon = False
GameHasBeenDrawn = False
CurrentSymbol = ''
StartSymbol = ''
PlayerOneSymbol = ''
PlayerTwoSymbol = ''
Answer = ''
PlayerOneScore = 0.0
PlayerTwoScore = 0.0
 
def DisplayBoard(Board):
    print('  | 1 2 3 ')
    print('--+-------')
    for Row in range(1,4):
        print(Row, '|', end=' ')
        for Column in range(1,4):
            print(Board[Column][Row], end=' ')
        print()
    print('\n')

def ClearBoard(Board):
    for Row in range(1,4):
        for Column in range(1,4):
            Board[Column][Row] = ' '

def GetMoveCoordinates():
    X = int(input('Enter x coordinate: '))
    Y = int(input('Enter y coordinate: '))
    return X, Y

def CheckValidMove(XCoordinate, YCoordinate, Board):
    ValidMove = True
    # Check x coordinate is valid
    if (XCoordinate < 1) or (XCoordinate > 3):
        ValidMove = False
    return ValidMove

def CheckXOr0HasWon(Board):
    XOrOHasWon = False
    for Column in range(1,4):
        if (Board[Column][1] == Board[Column][2]) and (Board[Column][2] == Board[Column][3]) and (Board[Column][2] != ' '):
            XOrOHasWon = True
    for Row in range(1,4):
        if (Board[1][Row] == Board[2][Row]) and (Board[2][Row] == Board[3][Row]) and (Board[2][Row] != ' '):
            XOrOHasWon = True
    return XOrOHasWon

def GetWhoStarts():
    RandomNo = random.randint(0, 100)
    if (RandomNo % 2) == 0:
        WhoStarts = 'X'
    else:
        WhoStarts = 'O'
    return WhoStarts

if __name__ == "__main__":
    PlayerOneName = input('What is the name of player one? ')
    PlayerTwoName = input('What is the name of player two? ')
    while PlayerOneSymbol not in ['X','O']:
    # Choose player one's symbol
        PlayerOneSymbol = input(PlayerOneName + ' what symbol do you wish to use, X or O? ')
        if PlayerOneSymbol not in ['X','O']:
            print('Symbol to play must be uppercase X or O')
    if PlayerOneSymbol == 'X':
        PlayerTwoSymbol = 'O'
    else:
        PlayerTwoSymbol = 'X'
    StartSymbol = GetWhoStarts()
    while Answer not in ['N','n']: # Play a game
        NoOfMoves = 0;
        GameHasBeenDrawn = False;
        GameHasBeenWon = False;
        ClearBoard(Board);
        print("\n")
        DisplayBoard(Board);
        if StartSymbol == PlayerOneSymbol:
            print(PlayerOneName + " starts playing " + StartSymbol)
        else:
            print(PlayerTwoName + " starts playing " + StartSymbol)
        print("\n")
        CurrentSymbol = StartSymbol
        while (not GameHasBeenWon) and (not GameHasBeenDrawn): # Play until a player wins or the game is drawn
            ValidMove = False;
            while not ValidMove: # Get a valid move
                XCoord,YCoord = GetMoveCoordinates()
                ValidMove = CheckValidMove(XCoord, YCoord, Board)
                if not ValidMove:
                    print("Coordinates invalid, please try again")
            Board[XCoord][YCoord] = CurrentSymbol 
            DisplayBoard(Board)
            GameHasBeenWon = CheckXOr0HasWon(Board)
            NoOfMoves += 1
            if not GameHasBeenWon:
                if NoOfMoves == 9: # Check if maximum number of allowed moves has been reached
                    GameHasBeenDrawn = True
                else:
                    if (CurrentSymbol == 'X'):
                        CurrentSymbol = 'O'
                    else:
                        CurrentSymbol = 'X'
        if GameHasBeenWon:   # Update scores and display result
            if (PlayerOneSymbol == CurrentSymbol):
                print(PlayerOneName + " congratulations you win!")
                PlayerOneScore += 1
            else:
                print(PlayerTwoName + " congratulations you win!")
                PlayerTwoScore += 1
        else:
            print("A draw this time!")
        print("\n")
        print(PlayerOneName + ", your score is: " + str(PlayerOneScore))
        print(PlayerTwoName + ", your score is: " + str(PlayerTwoScore))
        print();
        if (StartSymbol == PlayerOneSymbol):
            StartSymbol = PlayerTwoSymbol
        else:
            StartSymbol = PlayerOneSymbol;
        Answer = input("Another game Y/N? ")


