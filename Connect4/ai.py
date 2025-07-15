from main import check_win


def minimax(board, piece, depth, alpha, beta):
    if check_win(board, 1):
        return float('-inf')
    elif check_win(board, 2):
        return float('inf')
