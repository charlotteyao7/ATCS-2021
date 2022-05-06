'''
An unbeatable AI that implements the minimax algorithm
'''

class minimaxAI:

    def __init__(self):
        self.minimaxAI = ()
        self.name = "Minimax AI"

    def makeMove(self, current, isFirstMove, previousMove):
        print("There are currently", current, "chips.")
        if isFirstMove:
            AIturn = True
        else:
            AIturn = False
        score, move = self.minimax(current, isFirstMove, previousMove, AIturn, 100)
        print("Minimax AI took", move, "chips")
        return move

    def minimax(self, current, isFM, pM, AIturn, depth):
        if depth > 0:
            if current < 0:
                if AIturn:
                    return 10, None
                else:
                    return -10, None
        else:
            return 0, None

        optMove = 1
        if AIturn:
            best = -10
            if isFM:
                endIndex = current
            else:
                if (2 * pM) >= current:
                    endIndex = current + 1
                else:
                    endIndex = 2 * pM + 1
            for i in range(1, endIndex):
                current = current - i
                AIturn = False
                score = self.minimax(current, False, i, AIturn, depth - 1)[0]
                if score > best:
                    best = score
                    optMove = i
                current = current + i
            return best, optMove
        else:
            worst = 10
            if isFM:
                endIndex = current
            else:
                if (2 * pM) >= current:
                    endIndex = current + 1
                else:
                    endIndex = 2 * pM + 1
            for n in range(1, endIndex):
                current = current - n
                AIturn = True
                score = self.minimax(current, False, n, AIturn, depth - 1)[0]
                if score < worst:
                    worst = score
                    optMove = n
                current = current + n
            return worst, optMove