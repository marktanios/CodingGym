def isValidSudoku(board):
    #Check rows
    for i in range(9):
        Rows = [0] * 9
        for j in range(9):
            if board[i][j] != ".":
                Rows[int(board[i][j])-1] += 1
                if Rows[int(board[i][j])-1] > 1:
                    return False
    # Check columns
    for i in range(9):
        Columns = [0] * 9
        for j in range(9):
            if board[j][i] != ".":
                Columns[int(board[j][i])-1] += 1
                if Columns[int(board[j][i])-1] > 1:
                    return False

    #Check Blocks
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            Blocks = [0] * 9
            iEnd = i + 3
            jEnd = j + 3
            for ii in range(i, iEnd):
                for jj in range(j, jEnd):
                    if board[ii][jj] != ".":
                        Blocks[int(board[ii][jj])-1] += 1
                        if Blocks[int(board[ii][jj])-1] > 1:
                            return False
    return True


if __name__ == '__main__':
    board = [["8", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

    print(isValidSudoku(board))
