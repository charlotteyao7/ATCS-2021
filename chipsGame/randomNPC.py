"""
Name: Charlotte Yao
Date: May 9, 2022
AT CS

An NPC that plays randomly
"""

import random
import time


class randomNPC:

    ''' Initializer '''
    def __init__(self):
        self.randomNPC = ()
        self.name = "Random NPC"

    ''' Function that is called to make a move '''
    def makeMove(self, current, isFirstMove, previousMove):
        print("There are currently", current, "chips.")
        start = time.time()

        # Generate a random move within valid moves
        if isFirstMove:
            move = int(random.uniform(1, current))  # Includes current, but casting to int rounds down to current - 1
        else:
            if (2 * previousMove) >= current:
                move = int(random.uniform(1, current + 1))  # Includes current + 1, but casting to int rounds down to current
            else:
                move = int(random.uniform(1, 2 * previousMove + 1))

        # Print and return the move
        print("Random NPC took", move, "chips")
        end = time.time()
        print("This turn took:", end - start, "seconds")
        return move