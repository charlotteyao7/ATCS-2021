'''
An AI that implements the expectimax algorithm
'''

import time

class expectimaxAI:

    def __init__(self):
        self.expectimaxAI = ()
        self.name = "Expectimax AI"
        self.best = -1000

    def makeMove(self, current, isFirstMove, previousMove):
        print("There are currently", current, "chips.")
        if isFirstMove:
            AIturn = True
        else:
            AIturn = False
        start = time.time()
        score, move = self.expectimax(current, isFirstMove, previousMove, AIturn, 100, -100, 100)
        self.best = -1000
        print("Expectimax AI took", move, "chips")
        end = time.time()
        print("This turn took:", end - start, "seconds")
        return move

    def expectimax(self, current, isFM, pM, AIturn, depth, alpha, beta):
        if depth > 0:
            if current <= 0:
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
                    optMove = current
                else:
                    endIndex = 2 * pM + 1
            for i in range(1, endIndex):
                current = current - i
                AIturn = False
                score = self.expectimax(current, False, i, AIturn, depth - 1, alpha, beta)[0]
                if score > best:
                    best = score
                    optMove = i
                if alpha < score:
                    alpha = score
                current = current + i
                if alpha >= beta:
                    return best, optMove
            return best, optMove
        else:
            total = 0
            count = 0
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
                count = count + 1
                score = self.expectimax(current, False, n, AIturn, depth - 1, alpha, beta)[0]
                if beta > score:
                    beta = score
                total = total + score
                current = current + n
                if alpha >= beta:
                    return self.best, optMove
            average = total / count
            if average >= self.best:
                self.best = average
                optMove = n
            return self.best, optMove