import sys
import pygame
import numpy as np
from title import draw_title_screen
from result import draw_result_screen
from sound import init_audio, play_bgm

pygame.init()
init_audio()

# colors used in the game
white = (255, 255, 255)
gray = (200, 200, 200)
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)

# game window size and board settings
width = 300
height = 300
line_width = 5
board_rows = 3
board_cols = 3
square_size = width // board_cols
circle_radius = square_size // 3
circle_width = 15
cross_width = 25

# sound file paths
TITLE_BGM = "assets/bgm_title.wav"
GAME_BGM = "assets/bgm_game.wav"

# create the game window
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('tic tac toe')
screen.fill(black)

# create a 3x3 board filled with zeros
# 0 = empty, 1 = player, 2 = ai
board = np.zeros((board_rows, board_cols))

# game states
game_state = "title"
result_message = ""

# button holders
start_button = None
yes_button = None
no_button = None

# start title bgm
play_bgm(TITLE_BGM)


# draw the grid lines for the tic tac toe board
def draw_lines(color=white):
    for i in range(1, board_rows):
        pygame.draw.line(screen, color, (0, square_size * i), (width, square_size * i), line_width)
        pygame.draw.line(screen, color, (square_size * i, 0), (square_size * i, height), line_width)


# draw x and o figures based on the board values
def draw_figures(circle_color=green, cross_color=red):
    for row in range(board_rows):
        for col in range(board_cols):
            if board[row][col] == 1:
                pygame.draw.circle(
                    screen,
                    circle_color,
                    (int(col * square_size + square_size // 2), int(row * square_size + square_size // 2)),
                    circle_radius,
                    circle_width
                )
            elif board[row][col] == 2:
                pygame.draw.line(
                    screen,
                    cross_color,
                    (col * square_size + square_size // 4, row * square_size + square_size // 4),
                    (col * square_size + 3 * square_size // 4, row * square_size + 3 * square_size // 4),
                    cross_width
                )
                pygame.draw.line(
                    screen,
                    cross_color,
                    (col * square_size + square_size // 4, row * square_size + 3 * square_size // 4),
                    (col * square_size + 3 * square_size // 4, row * square_size + square_size // 4),
                    cross_width
                )


# place a player's mark on the board
def mark_square(row, col, player):
    board[row][col] = player


# check if a square is empty
def available_square(row, col):
    return board[row][col] == 0


# check if the board is full
def is_board_full(check_board=board):
    for row in range(board_rows):
        for col in range(board_cols):
            if check_board[row][col] == 0:
                return False
    return True


# check if the given player has won
def check_win(player, check_board=board):
    # check vertical wins
    for col in range(board_cols):
        if check_board[0][col] == player and check_board[1][col] == player and check_board[2][col] == player:
            return True

    # check horizontal wins
    for row in range(board_rows):
        if check_board[row][0] == player and check_board[row][1] == player and check_board[row][2] == player:
            return True

    # check main diagonal
    if check_board[0][0] == player and check_board[1][1] == player and check_board[2][2] == player:
        return True

    # check opposite diagonal
    if check_board[0][2] == player and check_board[1][1] == player and check_board[2][0] == player:
        return True

    return False


# minimax algorithm to choose the best move for the ai
def minimax(minimax_board, depth, is_maximizing):
    if check_win(2, minimax_board):
        return float('inf')
    elif check_win(1, minimax_board):
        return -float('inf')
    elif is_board_full(minimax_board):
        return 0

    if is_maximizing:
        best_score = -1000
        for row in range(board_rows):
            for col in range(board_cols):
                if minimax_board[row][col] == 0:
                    minimax_board[row][col] = 2
                    score = minimax(minimax_board, depth + 1, False)
                    minimax_board[row][col] = 0
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = 1000
        for row in range(board_rows):
            for col in range(board_cols):
                if minimax_board[row][col] == 0:
                    minimax_board[row][col] = 1
                    score = minimax(minimax_board, depth + 1, True)
                    minimax_board[row][col] = 0
                    best_score = min(score, best_score)
        return best_score


# find and make the best move for the ai
def best_move():
    best_score = -1000
    move = None

    for row in range(board_rows):
        for col in range(board_cols):
            if board[row][col] == 0:
                board[row][col] = 2
                score = minimax(board, 0, False)
                board[row][col] = 0

                if score > best_score:
                    best_score = score
                    move = (row, col)

    if move:
        mark_square(move[0], move[1], 2)
        return True

    return False


# reset the board
def restart_game():
    for row in range(board_rows):
        for col in range(board_cols):
            board[row][col] = 0


# player 1 goes first
player = 1

# main game loop
while True:
    for event in pygame.event.get():

        # close the game window
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # handle mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:

            # title screen click
            if game_state == "title":
                if start_button and start_button.collidepoint(event.pos):
                    restart_game()
                    player = 1
                    result_message = ""
                    game_state = "playing"
                    play_bgm(GAME_BGM)

            # game screen click
            elif game_state == "playing":
                mousex = event.pos[0]
                mousey = event.pos[1]

                clicked_row = int(mousey // square_size)
                clicked_col = int(mousex // square_size)

                # keep click inside board
                if 0 <= clicked_row < board_rows and 0 <= clicked_col < board_cols:
                    if available_square(clicked_row, clicked_col):
                        mark_square(clicked_row, clicked_col, player)

                        # player win
                        if check_win(1):
                            result_message = "You Win!"
                            game_state = "result"

                        # player turn finished
                        if game_state == "playing":
                            player = player % 2 + 1

                            # ai move
                            if best_move():
                                if check_win(2):
                                    result_message = "You Lose!"
                                    game_state = "result"
                                else:
                                    player = player % 2 + 1

                        # draw
                        if game_state == "playing" and is_board_full():
                            result_message = "Draw!"
                            game_state = "result"

            # result screen click
            elif game_state == "result":
                if yes_button and yes_button.collidepoint(event.pos):
                    restart_game()
                    player = 1
                    result_message = ""
                    game_state = "playing"
                    play_bgm(GAME_BGM)

                elif no_button and no_button.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        # optional keyboard restart during playing/result
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart_game()
                player = 1
                result_message = ""
                game_state = "playing"
                play_bgm(GAME_BGM)

    # draw current screen
    if game_state == "title":
        start_button = draw_title_screen(screen)

    elif game_state == "playing":
        screen.fill(black)
        draw_lines()
        draw_figures()

    elif game_state == "result":
        yes_button, no_button = draw_result_screen(screen, result_message)

    # update the display
    pygame.display.update()
