"""
Before your interview, write a program that lets two humans play a game of Tic Tac Toe in a terminal.
The program should: 
[X]  let the players take turns to input their moves. 
[X]  report the outcome of the game.

During your interview, you will pair on adding support for a computer player to your game. 
You can start with random moves and make the AI smarter if you have time.
"""

# Tic Tac Toe for two players (terminal-based)

def play_game():
    board = [str(i) for i in range(9)]

    def print_board():
        print()
        print(f" {board[0]} | {board[1]} | {board[2]} ")
        print("---+---+---")
        print(f" {board[3]} | {board[4]} | {board[5]} ")
        print("---+---+---")
        print(f" {board[6]} | {board[7]} | {board[8]} ")
        print()

    def check_winner(player):
        wins = [
            (0,1,2), (3,4,5), (6,7,8),
            (0,3,6), (1,4,7), (2,5,8),
            (0,4,8), (2,4,6)
        ]
        return any(board[a] == board[b] == board[c] == player for a,b,c in wins)

    def is_draw():
        for cell in board:
            if cell not in ("X", "O"):
                return False 
        return True 
        

    current_player = "X"

    print("Tic Tac Toe")
    print("Positions are numbered 0–8:")
    print_board()

    while True:
        move = input(f"Player {current_player}, choose a position (0-8): ")

        if not move.isdigit() or not 0 <= int(move) < 9:
            print("Invalid input, must be number 0 through 8 inclusive.")
            continue

        pos = int(move)
        if not board[pos].isdigit():
            print("That spot is already taken. Try again.")
            continue

        board[pos] = current_player

        if check_winner(current_player):
            print_board()
            print(f"Congrats, Player {current_player}! 🎉")
            break

        if is_draw():
            print_board()
            print("It's a draw!")
            break

        print_board()
        current_player = "O" if current_player == "X" else "X"


while True:
    play_game()
    choice = input("\nPress Enter to start again... or input any other char to end game")
    if choice != "":
        print("Goodbye!")
        break    
    print("\n" * 2)
