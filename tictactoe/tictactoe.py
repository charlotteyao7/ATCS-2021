import random

class TicTacToe:
    def __init__(self):
        # Sets up the board to be '-'
        self.board = []
        for i in range(0, 3):
            self.board.append(['-', '-', '-'])

    def print_instructions(self):
        # Prints the instructions to the game
        print("\tWelcome to TicTacToe!")
        print("\tPlayer 1 is X and Player 2 is O")
        print("\tTake turns placing your pieces - the first to 3 in a row wins!")
        return

    def print_board(self):
        # Prints the board
        print('    0  1  2')
        for i in range(0, 3):
            s = ""
            for j in range(0, 3):
                s = s + '  ' + self.board[i][j]
            print(str(i) + ' ' + s)
        return

    def is_valid_move(self, row, col):
        # Checks if the move is 'valid'
        if row >= 0 and row <=2 and col >=0 and col <= 2:
            if self.board[row][col] == '-':
                return True
        return False

    def place_player(self, player, row, col):
        # Places the player on the board
        self.board[row][col] = player
        return

    def take_manual_turn(self, player):
        # Asks the user for a row, col until a valid response
        #  is given them place the player's icon in the right spot
        row = input("Enter a row: ")
        col = input("Enter a col: ")
        while True:
            try:
                if self.is_valid_move(int(row), int(col)):
                    break
                else:
                    print("Please enter a valid move.")
                    row = input("Enter a row: ")
                    col = input("Enter a col: ")
            except ValueError:
                print("Please enter a valid move.")
                row = input("Enter a row: ")
                col = input("Enter a col: ")
        self.place_player(player, int(row), int(col))

    def take_random_turn(self, player):
        # Generates a random valid spot for the NPC to move
        ranRow = random.randint(0, 2)
        ranCol = random.randint(0, 2)
        while not self.is_valid_move(ranRow, ranCol):
            ranRow = random.randint(0, 2)
            ranCol = random.randint(0, 2)
        self.place_player(player, ranRow, ranCol)

    def take_turn(self, player):
        # Simply calls the take_manual_turn and take_random_turn functions
        print(player + "'s Turn")
        if player == 'X':
            self.take_manual_turn('X')
        else:
            self.take_minimax_turn('O')
        return

    def check_col_win(self, player):
        # Checks col win
        for j in range(0, 3):
            if self.board[0][j] == player and self.board[1][j] == player and self.board[2][j] == player:
                return True
        return False

    def check_row_win(self, player):
        # Checks row win
        for row in self.board:
            if row == [player, player, player]:
                return True
        return False

    def check_diag_win(self, player):
        # Checks diagonal win
        if self.board[0][0] == player and self.board[1][1] == player and self.board[2][2] == player:
            return True
        elif self.board[0][2] == player and self.board[1][1] == player and self.board[2][0] == player:
            return True
        return False

    def check_win(self, player):
        # Checks if player won
        if self.check_col_win(player) or self.check_row_win(player) or self.check_diag_win(player):
            return True
        return False

    def check_tie(self):
        # Checks for tie
        for row in self.board:
            for space in row:
                if space == '-':
                    return False
        return True

    def minimax(self, player):
        if self.check_win('O'):
            return (10, None, None)
        elif self.check_win('X'):
            return (-10, None, None)
        elif self.check_tie():
            return (0, None, None)

        opt_row = -1
        opt_col = -1
        if player == 'O':
            best = -10
            for i in range(0, 3):
                for j in range(0, 3):
                    if self.is_valid_move(i, j):
                        self.place_player('O', i, j)
                        score = self.minimax('X')[0]
                        if best < score:
                            best = score
                            opt_row = i
                            opt_col = j
                        self.place_player('-', i, j)
            return (best, opt_row, opt_col)

        if player == 'X':
            worst = 10
            for n in range(0, 3):
                for m in range(0, 3):
                    if self.is_valid_move(n, m):
                        self.place_player('X', n, m)
                        score = self.minimax('O')[0]
                        if worst > score:
                            worst = score
                            opt_row = n
                            opt_col = m
                        self.place_player('-', n, m)
            return (worst, opt_row, opt_col)

    def take_minimax_turn(self, player):
        score, row, col = self.minimax(player)
        print("Score: ", score, " Row: ", row, " Col: ", col)
        self.place_player(player, row, col)

    def play_game(self):
        # Runs the game
        self.print_instructions()
        self.print_board()
        while not self.check_tie() and not self.check_win('X') and not self.check_win('O'):
            self.take_turn('X')
            self.print_board()
            if not self.check_win('X') and not self.check_tie():
                self.take_turn('O')
                self.print_board()
        if self.check_win('X'):
            print('X wins!')
        elif self.check_win('O'):
            print('O wins!')
        elif self.check_tie():
            print('Tie!')
        else:
            print('Error')
        return