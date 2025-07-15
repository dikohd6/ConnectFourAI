import pygame
import sys
import random
# Initialize Pygame
pygame.init()

# Constants
ROW_COUNT = 6
COL_COUNT = 7
SQUARESIZE = 100
RADIUS = SQUARESIZE // 2 - 5

width = COL_COUNT * SQUARESIZE
height = (ROW_COUNT + 1) * SQUARESIZE  # Extra space on top for text
size = (width, height)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Connect Four")

# Colors
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Font
text_font = pygame.font.SysFont(None, 60)

# Game board (0 = empty, 1 = human, 2 = AI)
board = [[0 for _ in range(COL_COUNT)] for _ in range(ROW_COUNT)]

TURN = 0  # 0 = human, 1 = AI
game_over = False

# Functions
def draw_board():
    for row in range(ROW_COUNT):
        for col in range(COL_COUNT):
            pygame.draw.rect(screen, BLUE, (col*SQUARESIZE, (row+1)*SQUARESIZE, SQUARESIZE, SQUARESIZE))
            if board[row][col] == 0:
                pygame.draw.circle(screen, BLACK, (col*SQUARESIZE + SQUARESIZE//2, (row+1)*SQUARESIZE + SQUARESIZE//2), RADIUS)
            elif board[row][col] == 1:
                pygame.draw.circle(screen, RED, (col*SQUARESIZE + SQUARESIZE//2, (row+1)*SQUARESIZE + SQUARESIZE//2), RADIUS)
            elif board[row][col] == 2:
                pygame.draw.circle(screen, YELLOW, (col*SQUARESIZE + SQUARESIZE//2, (row+1)*SQUARESIZE + SQUARESIZE//2), RADIUS)

def get_next_open_row(col):
    for row in reversed(range(ROW_COUNT)):
        if board[row][col] == 0:
            return row
    return None  # Column full

def is_valid_column(col):
    return board[0][col] == 0

def draw_text(text, color, x, y):
    img = text_font.render(text, True, color)
    screen.blit(img, (x, y))

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

# Game loop
running = True
while running:
    screen.fill(BLACK)
    draw_board()
    if check_win(board, 1):
        game_over = True
        draw_text("Game Over Human WON!", BLUE, 150, 25)
    elif check_win(board, 2):
        game_over = True
        draw_text("Game Over AI WON!", BLUE, 220, 25)


    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if not game_over:
            # Human turn
            if TURN == 0:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x_pos = event.pos[0]
                    col = x_pos // SQUARESIZE

                    if is_valid_column(col):
                        row = get_next_open_row(col)
                        board[row][col] = 1
                        TURN = 1  # Switch to AI

            # AI turn (simple random AI)
            elif TURN == 1:
                pygame.time.wait(500)  # Small delay to simulate thinking
                valid_cols = [c for c in range(COL_COUNT) if is_valid_column(c)]
                if valid_cols:
                    col = random.choice(valid_cols)
                    row = get_next_open_row(col)
                    board[row][col] = 2
                TURN = 0  # Switch back to human

pygame.quit()
sys.exit()
