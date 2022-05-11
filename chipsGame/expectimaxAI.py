"""
Name: Charlotte Yao
Date: May 9, 2022
AT CS

An AI that implements the expectimax algorithm
"""

import time


class expectimaxAI:

    ''' Initializer '''
    def __init__(self):
        self.expectimaxAI = ()
        self.name = "Expectimax AI"
        self.best = -1000

    ''' Function that is called to make a move '''
    def makeMove(self, current, isFirstMove, previousMove):
        print("There are currently", current, "chips.")
        if isFirstMove:
            AIturn = True
        else:
            AIturn = False
        start = time.time()

        # Call the expectimax function and retrieve the move
        score, move = self.expectimax(current, isFirstMove, previousMove, AIturn, 100, -100, 100)

        # Print and return the move
        print("Expectimax AI took", move, "chips")
        end = time.time()
        print("This turn took:", end - start, "seconds")
        return move

    ''' Function that is called by makeMove to determine the next move '''
    def expectimax(self, current, isFM, pM, AIturn, depth, alpha, beta):

        # Base case if no more nodes below
        if depth > 0:
            if current <= 0:
                if AIturn:
                    return 10, None
                else:
                    return -10, None
        else:
            return 0, None

        # Expectimax algorithm with alpha beta pruning
        optMove = 1
        if AIturn:
            best = -10
            # Set the last index to check
            if isFM:
                endIndex = current
            else:
                if (2 * pM) >= current:
                    endIndex = current + 1
                    optMove = current
                else:
                    endIndex = 2 * pM + 1
            # Check all possible moves
            for i in range(1, endIndex):
                current = current - i
                AIturn = False
                # Recursive call and take in the score
                score = self.expectimax(current, False, i, AIturn, depth - 1, alpha, beta)[0]
                if score > best:
                    # Set this move as the temporary optimal move
                    best = score
                    optMove = i
                if alpha < score:
                    alpha = score
                current = current + i
                if alpha >= beta:
                    # Prune the branch
                    return best, optMove
            return best, optMove
        else:  # Other player's turn
            total = 0
            count = 0
            # Set the last index to check
            if isFM:
                endIndex = current
            else:
                if (2 * pM) >= current:
                    endIndex = current + 1
                else:
                    endIndex = 2 * pM + 1
            # Check all possible moves
            for n in range(1, endIndex):
                current = current - n
                AIturn = True
                count = count + 1
                # Recursive call and take in the score
                score = self.expectimax(current, False, n, AIturn, depth - 1, alpha, beta)[0]
                if beta > score:
                    beta = score
                total = total + score
                current = current + n
                if alpha >= beta:
                    # Prune the branch
                    return self.best, optMove
            average = total / count
            if average >= self.best:
                # Set this move as the temporary optimal move
                self.best = average
                optMove = n
            return self.best, optMove