from email import message


def solveSudoku(board):

    verifier = verifier(board)
    if verifier["result"] == False:
        return verifier

    [row, col] = getNext(0, 0, board)
    if not checker(row, col, board):
        return {"result":False,"message":"No solution found"}
    return {"result":board,"message":"Solution found"}


def checker(row, col, board):
    # Break if we have reached the end of the board
    if row == 9:
        return True

    i = 1

    while i <= 9:
        verticals = getVerticals(col, board)
        horizontals = getHorizontals(row, board)
        grid = getGrid(row, col, board)

        if i in verticals or i in horizontals or i in grid:
            i += 1
            continue

        board[row][col] = i
        [nextRow, nextCol] = getNext(row, col, board)

        if checker(nextRow, nextCol, board) == True:
            return True
        else:
            i += 1

    board[row][col] = 0

    return False


def getVerticals(col, board):
    nums = []
    for i in range(9):
        nums.append(board[i][col])
    return nums


def getHorizontals(row, board):
    nums = []
    for i in range(9):
        nums.append(board[row][i])
    return nums


def getGrid(row, col, board):
    # Get the starting row
    if row <= 2:
        row = 0
    elif row > 2 and row <= 5:
        row = 3
    else:
        row = 6
    # Get the starting col
    if col <= 2:
        col = 0
    elif col > 2 and col <= 5:
        col = 3
    else:
        col = 6

    nums = []

    for r in range(row, row+3):
        for c in range(col, col+3):
            nums.append(board[r][c])

    return nums


def getNext(row, col, board):
    while True:
        if row == 9:
            return [row, col]
        if board[row][col] == 0:
            return [row, col]
        else:
            if col + 1 == 9:
                row += 1
                col = 0
            else:
                col += 1


def verifier(board):

    #Check board is an array of arrays
    if not isinstance(board, list):
        return {"result":False,"message":"Board is not an array"}
    for row in board:
        if not isinstance(row, list):
            return {"result":False,"message":"Board is not an array"}
        for col in row:
            if not isinstance(col, int):
                return {"result":False,"message":"Only integers are allowed"}
            if col < 0 or col > 9:
                return {"result":False,"message":"Only integers between 0 and 9 are allowed"}

    # Check if this is a 9x9 board
    if len(board) != 9:
        return {"result":False,"message":"Board is not a 9x9 array"}
    for row in board:
        if len(row) != 9:
            return {"result":False,"message":"Board is not a 9x9 array"}

    # Check if there are no negative or decimal numbers
    for row in board:
        for col in row:
            if col != int(col) or col < 0 or col > 9:
                return {"result":False,"message":"Only integers between 0 and 9 are allowed"}

    return {"result":True,"message":"Board is valid"}
