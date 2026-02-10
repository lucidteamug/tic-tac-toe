# Tic Tac Toe (Terminal Game)

A simple two-player Tic Tac Toe game played in the terminal.
Both players take turns entering their moves, and the game reports the winner or a draw. After each game, players can restart without exiting the program.

---

## Features

* Two human players (X and O)
* Turn-based input via the terminal
* Input validation (no overwriting moves, valid positions only)
* Win and draw detection
* Replay support (“Press Enter to start again”)

---

## How to Run

### Requirements

* Python 3.x

### Steps

1. Clone or download this repository
2. Navigate to the project folder
3. Run the game:

```bash
python tictactoe.py
```

---

## How to Play

The board positions are numbered like this:

```
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9
```

* Player **X** goes first
* On your turn, enter a number from **1 to 9**
* The game ends when:

  * A player gets three in a row (row, column, or diagonal)
  * All spaces are filled (draw)

If a player wins, the game prints:

```
Congrats, Player X!
```

After the game finishes, press **Enter** to start a new round.

---

## Example Gameplay

```
Player X, choose a position (1-9): 5
Player O, choose a position (1-9): 1
...
Congrats, Player X! 🎉

Press Enter to start again...
```

---

## Project Structure

```
tictactoe.py   # Main game file
README.md      # Game documentation
```

---

## Possible Improvements

* Player name input
* Score tracking across rounds
* AI opponent
* Colored board output
* Clear screen between turns

---

Have fun, and congrats to the winner! 🎉
