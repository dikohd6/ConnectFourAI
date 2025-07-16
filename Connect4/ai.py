#author: Dikran Kahiaian
#AI logic using minimax and alpha beta pruning
from utils import check_win, is_valid_column, get_next_open_row

ROW_COUNT = 6
COL_COUNT = 7
MAX_DEPTH = 6  #depth of tree

def evaluate_board(board):
    ai_score = 0
    human_score = 0

    # Horizontal lines
    for row in range(ROW_COUNT):
        for col in range(COL_COUNT - 3):
            ai_count = 0
            human_count = 0
            for i in range(4):
                if board[row][col + i] == 2:
                    ai_count += 1
                elif board[row][col + i] == 1:
                    human_count += 1
            if human_count == 0 and ai_count > 0:
                if ai_count == 1:
                    ai_score += 1
                elif ai_count == 2:
                    ai_score += 10
                elif ai_count == 3:
                    ai_score += 90  # Increased to prioritize near-wins
            if ai_count == 0 and human_count > 0:
                if human_count == 1:
                    human_score += 1
                elif human_count == 2:
                    human_score += 10
                elif human_count == 3:
                    human_score += 90  # Increased to prioritize blocking

    # Vertical lines
    for col in range(COL_COUNT):
        for row in range(ROW_COUNT - 3):
            ai_count = 0
            human_count = 0
            for i in range(4):
                if board[row + i][col] == 2:
                    ai_count += 1
                elif board[row + i][col] == 1:
                    human_count += 1
            if human_count == 0 and ai_count > 0:
                if ai_count == 1:
                    ai_score += 1
                elif ai_count == 2:
                    ai_score += 10
                elif ai_count == 3:
                    ai_score += 90
            if ai_count == 0 and human_count > 0:
                if human_count == 1:
                    human_score += 1
                elif human_count == 2:
                    human_score += 10
                elif human_count == 3:
                    human_score += 90

    # Positive diagonal (/)
    for row in range(ROW_COUNT - 3):
        for col in range(COL_COUNT - 3):
            ai_count = 0
            human_count = 0
            for i in range(4):
                if board[row + i][col + i] == 2:
                    ai_count += 1
                elif board[row + i][col + i] == 1:
                    human_count += 1
            if human_count == 0 and ai_count > 0:
                if ai_count == 1:
                    ai_score += 1
                elif ai_count == 2:
                    ai_score += 10
                elif ai_count == 3:
                    ai_score += 90
            if ai_count == 0 and human_count > 0:
                if human_count == 1:
                    human_score += 1
                elif human_count == 2:
                    human_score += 10
                elif human_count == 3:
                    human_score += 90

    # Negative diagonal (\)
    for row in range(3, ROW_COUNT):
        for col in range(COL_COUNT - 3):
            ai_count = 0
            human_count = 0
            for i in range(4):
                if board[row - i][col + i] == 2:
                    ai_count += 1
                elif board[row - i][col + i] == 1:
                    human_count += 1
            if human_count == 0 and ai_count > 0:
                if ai_count == 1:
                    ai_score += 1
                elif ai_count == 2:
                    ai_score += 10
                elif ai_count == 3:
                    ai_score += 90
            if ai_count == 0 and human_count > 0:
                if human_count == 1:
                    human_score += 1
                elif human_count == 2:
                    human_score += 10
                elif human_count == 3:
                    human_score += 90

    return ai_score - human_score

def minimax(board, depth, isMaximizing, alpha, beta):
    if depth == MAX_DEPTH or check_win(board, 1) or check_win(board, 2):
        if check_win(board, 2):
            return 100
        elif check_win(board, 1):
            return -100
        else:
            return evaluate_board(board)
    if isMaximizing:
        value = float('-inf')
        for col in range(COL_COUNT):
            if is_valid_column(board, col):
                row = get_next_open_row(board, col)
                board[row][col] = 2
                score = minimax(board, depth + 1, False, alpha, beta)
                board[row][col] = 0
                value = max(value, score)
                alpha = max(alpha, value)
                if beta <= alpha:
                    break
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
                beta = min(beta, value)
                if beta <= alpha:
                    break
        return value

def best_move(board):
    best_score = float('-inf')
    move = (-1, -1)
    for col in range(COL_COUNT):
        if is_valid_column(board, col):
            row = get_next_open_row(board, col)
            board[row][col] = 2
            score = minimax(board, 0, False, float('-inf'), float('inf'))
            print(f"Column {col}: Score {score}")  # Debug print
            board[row][col] = 0
            if score > best_score:
                best_score = score
                move = (row, col)
    if move != (-1, -1):
        board[move[0]][move[1]] = 2
        return True
    return False