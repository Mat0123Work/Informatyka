

def count_empty_cols(board_array: list) -> int:
    col_count = 0
    for i in range(0, len(board_array)):
        col_check = True
        for j in range(0, len(board_array[i])):
            if(board_array[j][i] != "."):
                col_check = False
                break
        if(col_check):
            col_count += 1
    return col_count
        

###
#  [[ 1, 2, 3, 4], 
#   [ 1, 2, 3, 4], 
#   [ 1, 2, 3, 4]]
###            

def zad1_1():
    current_board = []
    max_board_empty_cols = 0
    boards_with_empty_cols = 0
    lines_til_now = 0
    with open("szachy_przyklad.txt", mode='r', encoding='utf-8') as openedFile:
        for line in openedFile:
            lines_til_now = (lines_til_now + 1 ) % 9
            line = line.strip('\n\r')
            if(lines_til_now == 0):
                ## count stuff
                result = count_empty_cols(current_board)
                if(result != 0):
                    if(result > max_board_empty_cols):
                        max_board_empty_cols = result
                    boards_with_empty_cols += 1
                current_board.clear()
            else:
                current_board.append([char for char in line])
        ## count stuff
        result = count_empty_cols(current_board)
        if(result != 0):
            if(result > max_board_empty_cols):
                max_board_empty_cols = result
            boards_with_empty_cols += 1
    return (boards_with_empty_cols, max_board_empty_cols)

print(zad1_1())

### --- Zad1_2

## Is board equaled and how many figures are there on board
def equality_of_colors_and_figures(array_board: list):
    figures_white = {key : 0 for key in "KWSHGP"}
    figures_black = {key : 0 for key in "kwshgp"}
    
    how_many_figures = 0
    for i in range(0, len(array_board)):
        for j in range(0, len(array_board[i])):
            if((array_board[i][j]) == '.'):
                continue
            ### IF IT IS WHITE FIGURE
            if(array_board[i][j] in "KWSHGP"):
                figures_white[array_board[i][j]] += 1
            else:
                figures_black[array_board[i][j]] += 1
    for char in "KWSHGP":
        if(figures_white[char] != figures_black[char.lower()]):
            return (False, 0)
        else:
            how_many_figures += 2*figures_white[char]
    return (True, how_many_figures)

def zad1_2():
    current_board = []
    lines_til_now = 0
    equality_boards = 0
    minimum_equality_boards_figures = 100
    with open("szachy.txt", mode='r', encoding='utf-8') as openedFile:
        for line in openedFile:
            lines_til_now = (lines_til_now + 1 ) % 9
            line = line.strip('\n\r')
            if(lines_til_now == 0):
                ## count stuff
                if(current_board == []):
                    continue
                result = equality_of_colors_and_figures(current_board)
                if(result[0] != False):
                    if(result[1] < minimum_equality_boards_figures):
                        minimum_equality_boards_figures = result[1]
                    equality_boards += 1
                current_board.clear()
            else:
                current_board.append([char for char in line])
        ## count stuff
        result = equality_of_colors_and_figures(current_board)
        if(result[0] != False):
            if(result[1] < minimum_equality_boards_figures):
                minimum_equality_boards_figures = result[1]
            equality_boards += 1
    return (equality_boards, minimum_equality_boards_figures)

print(zad1_2())

### --- Zad 1_3

def is_king_checked(array_board: list):
    white_towers = []
    black_towers = []
    white_checked, black_checked = False, False
    ## white Tower and black king
    for i in range(0, len(array_board)):
        for j in range(0, len(array_board[i])):
            if(array_board[i][j] == 'W'):
                white_towers.append((i,j))
            elif(array_board[i][j] == 'w'):
                black_towers.append((i,j))
    
    # white towers, black king
    for (y,x) in white_towers:
        for y_temp in range(y-1, -1, -1):
            if(array_board[y_temp][x] == "k"):
                black_checked = True
                break
            elif(array_board[y_temp][x] != '.'):
                break
        for y_temp in range(y+1, 8):
            if(array_board[y_temp][x] == 'k'):
                black_checked = True
            elif(array_board[y_temp][x] != '.'):
                break
        for x_temp in range(x-1, -1, -1):
            if(array_board[y][x_temp] == "k"):
                black_checked = True
                break
            elif(array_board[y][x_temp] != '.'):
                break
        for x_temp in range(x+1, 8):
            if(array_board[y][x_temp] == "k"):
                black_checked = True
                break
            elif(array_board[y][x_temp] != '.'):
                break   
    
    # black towers, white king
    for (y,x) in black_towers:
        for y_temp in range(y-1, -1, -1):
            if(array_board[y_temp][x] == "K"):
                white_checked = True
                break
            elif(array_board[y_temp][x] != '.'):
                break
        for y_temp in range(y+1, 8):
            if(array_board[y_temp][x] == 'K'):
                white_checked = True
            elif(array_board[y_temp][x] != '.'):
                break
        for x_temp in range(x-1, -1, -1):
            if(array_board[y][x_temp] == "K"):
                white_checked = True
                break
            elif(array_board[y][x_temp] != '.'):
                break
        for x_temp in range(x+1, 8):
            if(array_board[y][x_temp] == "K"):
                white_checked = True
                break
            elif(array_board[y][x_temp] != '.'):
                break   

    return (black_checked, white_checked)

    ## black Tower and white king
    

def zad1_3():
    current_board = []
    lines_til_now = 0
    white_checks = 0
    black_checks = 0
    with open("szachy.txt", mode='r', encoding='utf-8') as openedFile:
        for line in openedFile:
            lines_til_now = (lines_til_now + 1 ) % 9
            line = line.strip('\n\r')
            if(lines_til_now == 0):
                ## count stuff
                if(current_board == []):
                    continue
                result = is_king_checked(current_board)
                black_checks += int(result[0])
                white_checks += int(result[1])
                current_board.clear()
            else:
                current_board.append([char for char in line])
        ## count stuff
        result = is_king_checked(current_board)
        black_checks += int(result[0])
        white_checks += int(result[1])
    return (black_checks, white_checks)

print(zad1_3())