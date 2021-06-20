board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


def valid(bo, num, pos):
    # check the row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # check the column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # check the box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True


def solve(bo):
    '''
    Solving sudoku boards using backtracking algoritm
    '''
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    # looping thru 1 to 10 and checking if valid at the row and column in the board
    for i in range(1, 10):
        # if valid is adding the number to the board
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            # if the value is good, the algorithm continues with the next one
            if solve(bo):
                return True

            # else it resets the current one and goes back
            bo[row][col] = 0

    # if no number is valid, return False and stop
    return False


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)
    return None


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print(' - - - - - - - - - - - -')
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(' | ', end='')
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + ' ', end='')


if __name__ == '__main__':
    print('Initial board')
    print_board(board)
    solve(board)
    print('')
    print('After solving board')
    print_board(board)
