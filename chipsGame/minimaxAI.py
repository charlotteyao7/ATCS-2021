'''
An unbeatable AI that implements the minimax algorithm
'''

class minimaxAI:

    def __init__(self):
        self.minimaxAI = ()
        self.name = "Minimax AI"
        self.AITurn = True

    def makeMove(self, current, isFirstMove, previousMove):
        score, move = self.minimax(current, isFirstMove, previousMove)
        return move

    def minimax(self, current, isFM, pM):
        # self.AITurn = not self.AITurn
        depth = 1000

        if depth > 0:
            if current < 0:
                if self.AITurn:
                    return 10, current, isFM, pM
                else:
                    return -10, current, isFM, pM
            else:
                return 0, current, isFM, pM
        else:
            return 0, current, isFM, pM

        opt_move = -1

        '''
        FROM TIC TAC TOE
        
        opt_row = -1
        opt_col = -1
        if player == 'O':
            best = -10
            for i in range(0, 3):
                for j in range(0, 3):
                    if self.is_valid_move(i, j):
                        self.place_player('O', i, j)
                        score = self.minimax('X', depth - 1)[0]
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
                        score = self.minimax('O', depth - 1)[0]
                        if worst > score:
                            worst = score
                            opt_row = n
                            opt_col = m
                        self.place_player('-', n, m)
            return (worst, opt_row, opt_col) '''