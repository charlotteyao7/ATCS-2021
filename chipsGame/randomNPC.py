'''
An NPC that plays randomly
'''

import random

class randomNPC:

    def __init__(self):
        self.randomNPC = ()
        self.name = "Random NPC"

    def makeMove(self, current, isFirstMove, previousMove):
        print("There are currently", current, "chips.")
        if isFirstMove:
            move = int(random.uniform(1, current)) # includes current, but casting to int rounds down to current - 1
        else:
            if (2 * previousMove) >= current:
                move = int(random.uniform(1, current + 1)) # includes current + 1, but casting to int rounds down to current
            else:
                move = int(random.uniform(1, 2 * previousMove + 1))
        print("Random NPC took", move, "chips")
        return move