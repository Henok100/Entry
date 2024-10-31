#Imports
from random import randint

#Board Initialization
BoardCover = '+-------' * 3 + '+'
BoardInside = '|       ' * 3 + '|'
mainBoard = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def findIndex(Board, target):
    for row_index, row in enumerate(Board):
        if target in row:
            col_index = row.index(target)
            return row_index, col_index
    return None

def Display_Board(mainBoard):
    for i in range(3):
        print(BoardCover)
        print(BoardInside)
        for j in range(3):
            print(f'|   {mainBoard[i][j]}   ', end='')
        print('|')
        print(BoardInside)
    print(BoardCover)

def TieCheck(mainBoard):
    for i in range(3):
        for j in range(3):
            if type(mainBoard[i][j]) == 'int':
                return False
    return True

def WinCheck(mainBoard):
    #row check
    for i in range(3):
        if mainBoard[i] == ['X', 'X', 'X']:
            return 'User'
        if mainBoard[i] == ['O', 'O', 'O']:
            return 'Computer'
    #column check
    for i in range(3):
        col = [mainBoard[0][i], mainBoard[1][i], mainBoard[2][i]]
        if col == ['X', 'X', 'X']:
            return 'User'
        if col == ['O', 'O', 'O']:
            return 'Computer' 
    #diagnoal check
    diagonal_1 = [mainBoard[0][0], mainBoard[1][1], mainBoard[2][2]]
    if diagonal_1 == ['X', 'X', 'X']:
        return 'User'
    if diagonal_1 == ['O', 'O', 'O']:
        return 'Computer'
        
    diagonal_2 = [mainBoard[0][2], mainBoard[1][1], mainBoard[2][0]]
    if diagonal_2 == ['X', 'X', 'X']:
        return 'User'
    if diagonal_2 == ['O', 'O', 'O']:
        return 'Computer'  
    return None
   
# Display_Board(mainBoard)
mainBoard[1][1] = 'X'
Display_Board(mainBoard)
while True:
    try:
        UserMove = int(input("Enter your move: "))
    except:
        print("Please Enter a Valid input (integer only)!")
    if UserMove not in range(1, 10):
        print("The number must be between 1 and 9")
    elif findIndex(mainBoard, UserMove) == None:
        print("The chosen place is occupied!")
    else:
        row_index, col_index = findIndex(mainBoard, UserMove)
        mainBoard[row_index][col_index] = 'O'
        Display_Board(mainBoard)
    if WinCheck(mainBoard) == 'User':
        print("You Won!")
        break
    if WinCheck(mainBoard) == 'Computer':
        print("Computer Won!")
        break
    if TieCheck(mainBoard):
        print('It is a Tie!')
        break

    while True:
        ComputerMove = randint(1, 10)
        if findIndex(mainBoard, ComputerMove) != None:
            break
    row_index, col_index = findIndex(mainBoard, ComputerMove)
    mainBoard[row_index][col_index] = ComputerMove

    if WinCheck(mainBoard) == 'User':
        print("You Won!")
        break
    if WinCheck(mainBoard) == 'Computer':
        print("Computer Won!")
        break
    if TieCheck(mainBoard):
        print('It is a Tie!')
        break
