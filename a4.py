# NOTE: Until you fill in the TTTBoard class mypy is going to give you multiple errors
# talking about unimplemented class attributes, don't worry about this as you're working


class TTTBoard:
    """A tic tac toe board

    Attributes:
        board - a list of '*'s, 'X's & 'O's. 'X's represent moves by player 'X', 'O's
            represent moves by player 'O' and '*'s are spots no one has yet played on
    """

    def __init__(self):
        """Initialize a 3x3 tic tac toe board with 9 '*' """
        self.board = ['*'] * 9

    def __str__(self):
        """Return a string representation of the board"""
        return (f"{self.board[0]} {self.board[1]} {self.board[2]}\n"
            f"{self.board[3]} {self.board[4]} {self.board[5]}\n"
            f"{self.board[6]} {self.board[7]} {self.board[8]}")
    
    def make_move(self, player, pos):
        """Places a move for the player at position pos is valid
        
        Args:
            player - string "X" or "O"
            pos - integer 0-8 representing board position
        Returns:
            True if a move was made, False otherwise
        """
        if 0 <= pos <= 8 and self.board[pos] == '*':
            self.board[pos] = player
            return True
        return False
    
    def has_won(self, player):
        """Check if the player has won
        
        Args:
            player - string of either "X" or "O"
        Return:
            True if the player has won, False otherwise
        """
        # Define all winning combinations (rows, columns, diagonals)
        win_combos = [
            [0, 1, 2],  # top row
            [3, 4, 5],  # middle row
            [6, 7, 8],  # bottom row
            [0, 3, 6],  # left column
            [1, 4, 7],  # middle column
            [2, 5, 8],  # right column
            [0, 4, 8],  # diagonal top-left to bottom-right
            [2, 4, 6]   # diagonal top-right to bottom-left
        ]

        # Check each winning combination
        for combo in win_combos:
            if (self.board[combo[0]] == player and 
                self.board[combo[1]] == player and 
                self.board[combo[2]] == player):
                return True
        return False
    
    def game_over(self):
        """Check if the game is over (someone has won or the board is full)"""
        return self.has_won("X") or self.has_won("O") or '*' not in self.board
    
    def clear(self):
        """Clears the board to reset the game"""
        self.board = ['*'] * 9

def play_tic_tac_toe() -> None:
    """Uses your class to play TicTacToe"""

    def is_int(maybe_int: str):
        """Returns True if val is int, False otherwise

        Args:
            maybe_int - string to check if it's an int

        Returns:
            True if maybe_int is an int, False otherwise
        """
        try:
            int(maybe_int)
            return True
        except ValueError:
            return False

    brd = TTTBoard()
    players = ["X", "O"]
    turn = 0

    while not brd.game_over():
        print(brd)
        move: str = input(f"Player {players[turn]} what is your move? ")

        if not is_int(move):
            raise ValueError(
                f"Given invalid position {move}, position must be integer between 0 and 8 inclusive"
            )

        if brd.make_move(players[turn], int(move)):
            turn = not turn

    print(f"\nGame over!\n\n{brd}")
    if brd.has_won(players[0]):
        print(f"{players[0]} wins!")
    elif brd.has_won(players[1]):
        print(f"{players[1]} wins!")
    else:
        print(f"Board full, cat's game!")


if __name__ == "__main__":
    # here are some tests. These are not at all exhaustive tests. You will DEFINITELY
    # need to write some more tests to make sure that your TTTBoard class is behaving
    # properly.
    brd = TTTBoard()
    brd.make_move("X", 8)
    brd.make_move("O", 7)

    assert brd.game_over() == False

    brd.make_move("X", 5)
    brd.make_move("O", 6)
    brd.make_move("X", 2)

    assert brd.has_won("X") == True
    assert brd.has_won("O") == False
    assert brd.game_over() == True

    brd.clear()

    assert brd.game_over() == False

    brd.make_move("O", 3)
    brd.make_move("O", 4)
    brd.make_move("O", 5)

    assert brd.has_won("X") == False
    assert brd.has_won("O") == True
    assert brd.game_over() == True

    # Additional tests
    print("\nRunning additional tests...")
    
    # Test: Board full without winner (cat's game)
    brd.clear()
    brd.make_move("X", 0)
    brd.make_move("O", 1)
    brd.make_move("X", 2)
    brd.make_move("O", 4)
    brd.make_move("X", 3)
    brd.make_move("O", 5)
    brd.make_move("X", 7)
    brd.make_move("O", 6)
    brd.make_move("X", 8)
    assert brd.game_over() == True
    assert brd.has_won("X") == False
    assert brd.has_won("O") == False
    print("Cat's game test passed!")
    
    # Test: Diagonal win (top-right to bottom-left)
    brd.clear()
    brd.make_move("X", 2)
    brd.make_move("X", 4)
    brd.make_move("X", 6)
    assert brd.has_won("X") == True
    print("Diagonal win test passed!")
    
    # Test: Column win
    brd.clear()
    brd.make_move("O", 1)
    brd.make_move("O", 4)
    brd.make_move("O", 7)
    assert brd.has_won("O") == True
    print("Column win test passed!")
    
    # Test: Invalid move (position already taken)
    brd.clear()
    brd.make_move("X", 0)
    result = brd.make_move("O", 0)
    assert result == False
    print("Invalid move test passed!")
    
    # Test: Invalid move (out of bounds)
    result = brd.make_move("X", 9)
    assert result == False
    result = brd.make_move("X", -1)
    assert result == False
    print("Out of bounds test passed!")
    
    print("\nAll tests passed!")
    
    # uncomment to play!
    play_tic_tac_toe()
