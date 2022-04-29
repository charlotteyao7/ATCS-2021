'''
An unbeatable AI that implements the minimax algorithm
'''

class minimaxAI:

    def __init__(self):
        self.minimaxAI = ()
        self.name = "Minimax AI"
        self.AITurn = False

    def makeMove(self, current, isFirstMove, previousMove):
        score, move = self.minimax(None, current, isFirstMove, previousMove)
        return move

    def minimax(self, optMove, current, isFM, pM):
        if isFM:
            self.AITurn = True
        depth = 1000

        if depth > 0:
            if current < 0:
                if self.AITurn:
                    return 10, optMove
                else:
                    return -10, optMove
            else:
                return 0, optMove
        else:
            return 0, current

        optMove = -1
        if self.AITurn:
            best = -10
            if iSFM:
                for i in range(1, current):
                    current = current - i
                    self.AITurn = not self.AITurn
                    score = self.minimax(current, False, i)[0]
                    if score > best:
                        best = score
                        optMove = i
                    current = current + i
            else:
                for j in range(1, 2 * pM + 1):
                    current = current - j
                    self.AITurn = not self.AITurn
                    score = self.minimax(current, False, j)[0]
                    if score > best:
                        best = score
                        optMove = j
                    current = current + j
            return best, optMove
        else:
            worst = 10
            if isFM:
                for n in range(1, current):
                    current = current - n
                    self.AITurn = not self.AITurn
                    score = self.minimax(current, False, n)[0]
                    if score < worse:
                        worst = score
                        optMove = n
                    current = current + n
            else:
                for m in range(1, 2 * pM + 1):
                    current = current - m
                    self.AITurn = not self.AITurn
                    score = self.minimax(current, False, m)[0]
                    if score < worse:
                        worst = score
                        optMove = m
                    current = current + m
            return worst, optMove


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