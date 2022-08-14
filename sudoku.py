print('Welcome to sudoku solver!')

def which_square():
    inputt = input('would you like to use the test board? (yes or no)\n')
    if inputt == 'no' or inputt == 'n':
        n = False
    else:
        for i in range(0,82):
            board[i] = test_board[i]
        return board

        
    while not n:
        print('for easier designation, here is a numbered board')
        display_board(board_1)
        num = int(input('Which area would you like to place?(1-81)\n'))


        if num in range(0, 82):
            x = False
            while not x:
                value = int(input('which number is placed here? (1-9)\n'))
                if value in range(0,10):
                    value = str(value)
                    board[num] = value
                    display_board(board)
                    more = input('Place another number? (yes or no)\n')
                    if more == 'yes':
                        x = True
                        n = False
                    else:
                        x = True
                        n = True

                else:
                    print('sorry thats an invalid input(1-9)')


        else:
            print('sorry that is an invalid input (1-81)')
def filled_board():
    z = False
    while not z:
        ans = input('yay! have you filled out your board? yes or no \n')
        if ans == 'no':
            which_square()
        else:
            z = True
            print('great!')
def check(grid):
    x = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            val = grid[i][j]
            if val != 0:
                if logic(grid, val, (i, j)):
                    x += 0
                else:
                    x += 1        
    if x > 0:
        print(grid)
        print('sorry it looks like you didnt fill that out correctly, youll have to start over')
    else:
        print('Great! it looks like you filled it out correctly')

def logic(grid, val , num):

    # num will be tuple

    # check row
    for i in range(len(grid[0])):
        if grid[num[0]][i] == val and num[1] != i:
            return False
    # check col
    for i in range(len(grid)):
        if grid[i][num[1]] == val and num[0] != i:
            return False
    #check box
    box_x = num[1] // 3
    box_y = num[0] //3
    for i in range(box_y*3, box_y*3 +3):
        for j in range(box_x*3, box_x*3 +3):
            if grid[i][j] == val and (i,j) != num:
                return False
    return True
def empty(grid):
    # find empty spot
    z = False
    while not z:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    z = True
                    return (i, j)
        return None



def change(board):
    filled_board()
    grid = change_board(board)
    check(grid)
    return grid
def solve(grid):
    pos = empty(grid)
    if pos == None:

        return True
    else:
        row, col = pos
    for i in range(1,10):
        if logic(grid, i, (row, col)):
            grid[row][col] = i
            if solve(grid):

                return grid
            grid[row][col] = 0
    return False

def change_board(boardd):
    grid = [[int(boardd[1]), int(boardd[2]), int(boardd[3]), int(boardd[4]), int(boardd[5]), int(boardd[6]), int(boardd[7]), int(boardd[8]), int(boardd[9])],
    [int(boardd[10]), int(boardd[11]), int(boardd[12]), int(boardd[13]), int(boardd[14]), int(boardd[15]), int(boardd[16]), int(boardd[17]), int(boardd[18])],
    [int(boardd[19]), int(boardd[20]), int(boardd[21]), int(boardd[22]), int(boardd[23]), int(boardd[24]),int(boardd[25]), int(boardd[26]), int(boardd[27])],
    [int(boardd[28]), int(boardd[29]), int(boardd[30]), int(boardd[31]), int(boardd[32]), int(boardd[33]),int(boardd[34]), int(boardd[35]), int(boardd[36])],
    [int(boardd[37]), int(boardd[38]), int(boardd[39]), int(boardd[40]), int(boardd[41]), int(boardd[42]),int(boardd[43]), int(boardd[44]), int(boardd[45])],
    [int(boardd[46]), int(boardd[47]), int(boardd[48]), int(boardd[49]), int(boardd[50]), int(boardd[51]),int(boardd[52]), int(boardd[53]), int(boardd[54])],
    [int(boardd[55]), int(boardd[56]), int(boardd[57]), int(boardd[58]), int(boardd[59]), int(boardd[60]),int(boardd[61]), int(boardd[62]), int(boardd[63])],
    [int(boardd[64]), int(boardd[65]), int(boardd[66]), int(boardd[67]), int(boardd[68]), int(boardd[69]),int(boardd[70]), int(boardd[71]), int(boardd[72])],
    [int(boardd[73]), int(boardd[74]), int(boardd[75]), int(boardd[76]), int(boardd[77]), int(boardd[78]),int(boardd[79]), int(boardd[80]), int(boardd[81])]
]
    print(grid)
    return grid

def display_board(board):
    print(board[1] + '|' + board[2] + '|' + board[3] + '   ' + board[4] + '|' + board[5] + '|' + board[6] + '   ' + board[7] + '|' + board[8] + '|' + board[9])
    print(board[10] + '|' + board[11] + '|' + board[12] + '   ' + board[13] + '|' + board[14] + '|' + board[15] + '   ' + board[16] + '|' + board[17] + '|' + board[18])
    print(board[19] + '|' + board[20] + '|' + board[21] + '   ' + board[22] + '|' + board[23] + '|' + board[24] + '   ' + board[25] + '|' + board[26] + '|' + board[27])
    print('______________________________')
    print(board[28] + '|' + board[29] + '|' + board[30] + '   ' + board[31] + '|' + board[32] + '|' + board[33] + '   ' + board[34] + '|' + board[35] + '|' + board[36])
    print(board[37] + '|' + board[38] + '|' + board[39] + '   ' + board[40] + '|' + board[41] + '|' + board[42] + '   ' + board[43] + '|' + board[44] + '|' + board[45])
    print(board[46] + '|' + board[47] + '|' + board[48] + '   ' + board[49] + '|' + board[50] + '|' + board[51] + '   ' + board[52] + '|' + board[53] + '|' + board[54])
    print('______________________________')
    print(board[55] + '|' + board[56] + '|' + board[57] + '   ' + board[58] + '|' + board[59] + '|' + board[60] + '   ' + board[61] + '|' + board[62] + '|' + board[63])
    print(board[64] + '|' + board[65] + '|' + board[66] + '   ' + board[67] + '|' + board[68] + '|' + board[69] + '   ' + board[70] + '|' + board[71] + '|' + board[72])
    print(board[73] + '|' + board[74] + '|' + board[75] + '   ' + board[76] + '|' + board[77] + '|' + board[78] + '   ' + board[79] + '|' + board[80] + '|' + board[81])

board =['0'] * 82
board_1 = ['0', '1', '2', '3', '4', '5','6', '7','8', '9', '10', '11', '12', '13', '14', '15', '16', '17','18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30','31','32', '33', '34','35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55','56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81' ]
test_board = ['0', '0', '0', '0', '0', '0', '0', '1', '9', '0', '3', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '8', '0', '5', '0', '0', '0', '4', '5', '1', '0', '0', '0', '6', '0', '0', '0', '2', '0', '0', '0', '0', '0', '0', '0', '8', '0', '0', '0', '9', '0', '0', '0', '4', '3', '7', '0', '0', '0', '3', '0', '2', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '7', '0', '6', '1', '0', '0', '0', '0', '0', '0']



which_square()
grid = change(board)
ans = solve(grid)
print(ans)

