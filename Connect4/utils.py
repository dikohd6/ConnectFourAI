#author: Dikran Kahiaian
#helper methods for the game


# Constants
ROW_COUNT = 6
COL_COUNT = 7
def get_next_open_row(board, col):
    for row in reversed(range(ROW_COUNT)):
        if board[row][col] == 0:
            return row
    return None  # Column full

def is_valid_column(board, col):
    return board[0][col] == 0


def check_win(board, piece):
    # Horizontal check
    for row in range(ROW_COUNT):
        for col in range(COL_COUNT - 3):
            if all(board[row][col+i] == piece for i in range(4)):
                return True

    # Vertical check
    for col in range(COL_COUNT):
        for row in range(ROW_COUNT - 3):
            if all(board[row+i][col] == piece for i in range(4)):
                return True

    # Positive diagonal (/)
    for row in range(ROW_COUNT - 3):
        for col in range(COL_COUNT - 3):
            if all(board[row+i][col+i] == piece for i in range(4)):
                return True

    # Negative diagonal (\)
    for row in range(3, ROW_COUNT):
        for col in range(COL_COUNT - 3):
            if all(board[row-i][col+i] == piece for i in range(4)):
                return True

    return False