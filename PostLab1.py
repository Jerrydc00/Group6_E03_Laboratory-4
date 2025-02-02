class TicTacToe:
    def __init__(self):
        """Set up the game board and designate the first player."""
        self.grid = [[" " for _ in range(3)] for _ in range(3)]
        self.active_player = "X"

    def show_board(self):
        """Print the current board state."""
        for row in self.grid:
            print(" | ".join(row))
            print("-" * 5)

    def place_marker(self, r, c):
        """
        Place a marker on the board if the position is available.
        Args:
            r (int): Row index (0-2).
            c (int): Column index (0-2).
        Returns:
            bool: True if move is successful, False otherwise.
        """
        if 0 <= r < 3 and 0 <= c < 3 and self.grid[r][c] == " ":
            self.grid[r][c] = self.active_player
            return True
        print("Invalid move. Try again.")
        return False

    def is_winner(self):
        """Determine if the current player has won."""
        for i in range(3):
            if all(self.grid[i][j] == self.active_player for j in range(3)) or \
               all(self.grid[j][i] == self.active_player for j in range(3)):
                return True

        if all(self.grid[i][i] == self.active_player for i in range(3)) or \
           all(self.grid[i][2 - i] == self.active_player for i in range(3)):
            return True

        return False
