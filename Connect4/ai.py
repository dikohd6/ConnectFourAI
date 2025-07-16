from utils import check_win, is_valid_column, get_next_open_row

ROW_COUNT = 6
COL_COUNT = 7
MAX_DEPTH=4

def minimax(board, depth,isMaximizing, alpha, beta):
    if depth == MAX_DEPTH or check_win(board, 1) or check_win(board, 2):
        if check_win(board, 2):
            return 100
        elif check_win(board, 1):
            return -100
        else:
            return 0
    if isMaximizing:
        value=float('-inf')
        for col in range(COL_COUNT):
            if is_valid_column(board, col):
                row=get_next_open_row(board, col)
                board[row][col] = 2
                score=minimax(board, depth+1, False, alpha, beta)
                board[row][col] = 0
                value= max(value, score)
        return value
    else:
        value = float('inf')
        for col in range(COL_COUNT):
            if is_valid_column(board, col):
                row = get_next_open_row(board, col)
                board[row][col] = 1
                score = minimax(board, depth + 1, True, alpha, beta)
                board[row][col] = 0
                value = min(value, score)
        return value

def best_move(board):
    best_score=float('-inf')
    move=(-1, -1)
    for col in range(COL_COUNT):
        if is_valid_column(board, col):
            row = get_next_open_row(board, col)
            board[row][col] = 2
            score = minimax(board, 0, False, float('-inf') , float('inf'))
            board[row][col] = 0
            if score > best_score:
                best_score = score
                move = (row, col)
    if move != (-1, -1):
        board[move[0]][move[1]] = 2
        return True
    return False

