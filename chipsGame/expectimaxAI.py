'''
An AI that implements the expectimax algorithm
'''

class expectimaxAI:

    def __init__(self):
        self.expectimaxAI = ()
        self.name = "Expectimax AI"

    def makeMove(self, current, isFirstMove, previousMove):
        print("There are currently", current, "chips.")
        if isFirstMove:
            AIturn = True
        else:
            AIturn = False
        score, move = self.expectimax(current, isFirstMove, previousMove, AIturn, 100)
        print("Expectimax AI took", move, "chips")
        return move

    def expectimax(self, current, isFM, pM, AIturn, depth):
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
                endIndex = 2 * pM + 1
            for i in range(1, endIndex):
                current = current - i
                AIturn = False
                score = self.expectimax(current, False, i, AIturn, depth - 1)[0]
                if score > best:
                    best = score
                    optMove = i
                current = current + i
            return best, optMove
        else:
            best = -10
            value = 0
            if isFM:
                endIndex = current
            else:
                endIndex = 2 * pM + 1
            for n in range(1, endIndex):
                current = current - n
                AIturn = True
                score = self.expectimax(current, False, n, AIturn, depth - 1)[0]
                p = 1 / (endIndex - 1)  # probability of each move
                value = value + (p * score)
                if value > best:
                    best = value
                    optMove = n
                current = current + n
            return best, optMove