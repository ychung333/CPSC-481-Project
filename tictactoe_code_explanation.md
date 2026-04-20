# Tic Tac Toe AI Code Explanation(only about tictactoe.py)

## Summary Purpose

The purpose of this program is to:

- open a Tic Tac Toe game window
- let the player click to make a move
- let the AI respond with its move
- check for wins or ties
- restart the game when `R` is pressed

---

## Big Picture

This code has a few main parts:

1. setup  
2. board data  
3. drawing the game  
4. game rules  
5. AI logic  
6. the main game loop  

Think of it like this:

- **setup** = getting the table ready
- **board data** = remembering where each move is
- **drawing** = showing the game on the screen
- **rules** = checking what is allowed and who won
- **AI logic** = the computer thinking ahead
- **main loop** = the part that keeps the game running

---

## 1. Setup Block

This part imports the tools and starts Pygame.

```python
import sys
import pygame
import numpy as np

pygame.init()
```

### What it does
- `sys` helps fully close the program
- `pygame` handles the game window, drawing, mouse input, and keyboard input
- `numpy` is used to create the 3x3 board
- `pygame.init()` turns Pygame on

### Simple idea
This is like turning on the game system and getting your tools ready.

---

## 2. Colors and Size Block

This part sets up the colors and game sizes.

```python
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

WIDTH = 300
HEIGHT = 300
LINE_WIDTH = 5
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
```

### What it does
- stores the colors the game will use
- stores the window size
- stores the board size
- calculates the size of each square and symbol

### Important idea
Since the board is 300 pixels wide and has 3 columns, each square becomes 100 pixels wide.

### Simple idea
This is like choosing the board size, line thickness, and piece sizes before the game starts.

---

## 3. Screen and Board Block

This part creates the game window and the actual board data.

```python
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')
screen.fill(BLACK)

board = np.zeros((BOARD_ROWS, BOARD_COLS))
```

### What it does
- opens the game window
- gives the window a title
- fills the background black
- creates a 3x3 board full of zeroes

### What the board values mean
- `0` = empty
- `1` = player
- `2` = AI

### Simple idea
This is like opening the game board and setting every square to empty.

---

## 4. Drawing Block

These functions draw the board and the game pieces.

### `draw_lines()`
This function draws the Tic Tac Toe grid.

```python
def draw_lines(color=WHITE):
    for i in range(1, BOARD_ROWS):
        pygame.draw.line(screen, color, (0, SQUARE_SIZE * i), (WIDTH, SQUARE_SIZE * i), LINE_WIDTH)
        pygame.draw.line(screen, color, (SQUARE_SIZE * i, 0), (SQUARE_SIZE * i, HEIGHT), LINE_WIDTH)
```

### What it does
- draws 2 horizontal lines
- draws 2 vertical lines
- creates the 3x3 board

### `draw_figures()`
This function draws circles and X's based on the board values.

```python
def draw_figures(circle_color=GREEN, cross_color=RED):
```

### What it does
- checks every square on the board
- if it sees a `1`, it draws a circle
- if it sees a `2`, it draws an X

### Simple idea
The board array stores the moves, and the drawing functions turn those moves into visible shapes on the screen.

---

## 5. Board Helper Functions Block

These are the helper functions that manage the board and check the rules.

### `mark_square(row, col, player)`
Places a move on the board.

### `available_square(row, col)`
Checks if a square is empty.

### `is_board_full(check_board=board)`
Checks if there are no empty spaces left.

### `check_win(player, check_board=board)`
Checks if a player has 3 in a row.

It checks:
- vertical wins
- horizontal wins
- diagonal wins

### Simple idea
These functions are like the game referee. They decide:
- whether a move is allowed
- whether the board is full
- whether someone won

---

## 6. AI Block: `minimax()`

This is the smartest part of the program.

```python
def minimax(minimax_board, depth, is_maximizing):
```

### What it does
This function lets the AI think ahead and score possible future moves.

### How it works
It pretends to keep playing the game in the future until it reaches:
- an AI win
- a player win
- or a tie

Then it gives each outcome a score:
- AI win = very high score
- player win = very low score
- tie = 0

### Maximizing and minimizing
- when it is the AI's turn, it tries to get the **highest** score
- when it is the player's turn, it assumes the player tries to give the AI the **lowest** score

### Simple analogy
It is like the AI playing many fake games in its head before making the real move.

---

## 7. AI Move Selection Block: `best_move()`

```python
def best_move():
```

### What it does
This function checks every empty square and uses `minimax()` to find the best move for the AI.

### How it works
- try one possible move
- score it with `minimax()`
- undo it
- try the next one
- keep the move with the best score

### Simple idea
`minimax()` does the thinking, and `best_move()` chooses the actual move to play.

---

## 8. Restart Block

```python
def restart_game():
```

### What it does
- clears the screen
- redraws the board
- resets every square back to 0

### Simple idea
This starts the game over from scratch.

---

## 9. Starting State Block

```python
draw_lines()

player = 1
game_over = False
```

### What it does
- draws the board at the start
- makes player 1 go first
- says the game is not over yet

---

## 10. Main Game Loop Block

```python
while True:
```

This is the part that keeps the game running.

### What it does
It keeps checking:
- did the player click?
- did the player press a key?
- did someone win?
- should the screen be updated?

### Simple analogy
This is like the game manager constantly watching everything.

---

## 11. Event Handling Block

Inside the main loop, the code checks for events.

### Quit event
If the user closes the window, the game shuts down.

### Mouse click event
If the player clicks:
- get the mouse position
- figure out which square was clicked
- check if that square is empty
- place the player's move there

### After the player move
- check if the player won
- if not, let the AI move
- check if the AI won
- if nobody won, check for a tie

### Keyboard event
If the player presses `R`, the game restarts.

### Simple idea
This block is where the game reacts to what the user does.

---

## 12. Redrawing the Screen Block

At the end of each loop, the game redraws everything.

```python
screen.fill(BLACK)
```

This clears the old frame first.

Then:
- if the game is still going, it draws the normal board and pieces
- if the game is over, it changes colors depending on the result

Examples:
- player win = green board lines
- AI win = red board lines
- tie = gray board lines and marks

### Why this matters
Without redrawing, the game would not update properly on the screen.

---

## 13. Display Update Block

```python
pygame.display.update()
```

### What it does
This shows everything that was just drawn.

### Simple idea
The code draws in the background first, and this command says, "Now show it on the screen."

---

## Overall Flow of the Program

Here is the whole flow in simple words:

1. start Pygame  
2. create the window  
3. make an empty board  
4. draw the Tic Tac Toe grid  
5. wait for the player to click  
6. place the player's move  
7. check for a win  
8. let the AI choose the best move  
9. check for a win or tie  
10. redraw the screen  
11. repeat until the game ends or restarts  

---

## Short Easy Summary

This code is a Tic Tac Toe game with an AI opponent.

- the **board array** stores the moves
- the **draw functions** show the board and pieces
- the **rule functions** check wins and empty spaces
- the **main loop** keeps the game alive
- the **minimax algorithm** makes the AI smart

### Final analogy
Think of the program like a little team:

- **board** = memory
- **draw functions** = artists
- **check functions** = referees
- **main loop** = manager
- **minimax** = strategist
