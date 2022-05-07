'''
Charlotte's hard-coded player from 2020
'''

import time

class charlottePlayer:

    def __init__(self):
        self.charlottePlayer = ()
        self.name = "CY NPC"

    def makeMove(self, current, isFirstMove, previousMove):
        print("There are currently", current, "chips.")
        start = time.time()
        if current <= 2: # take everything
            move = current
        else:
            # fill array of fibonacci numbers
            fibonacci = []
            fibonacci.append(1)
            fibonacci.append(2)
            for i in range(2, 12):
                next = fibonacci[i - 1] + fibonacci[i - 2]
                fibonacci.append(next)

            # find mid and high fibonacci numbers (chips location in the fibonacci array)
            index = len(fibonacci) - 1
            mid = 1 # placeholder
            high = 1 # placeholder
            while current <= fibonacci[index]:
                index = index - 1
            mid = index
            high = index + 1

            # search through lower fibonacci numbers
            low = mid - 1
            valid = True
            if low < 0:
                valid = False
            while valid:
                if fibonacci[mid] + fibonacci[low] > current:
                    low = low - 1
                else:
                    valid = False
                if low < 0:
                    low = low + 1
                    valid = False

            target = 0
            if fibonacci[mid] == current:
                target = current - 1
            elif fibonacci[low] + fibonacci[mid] == current:
                target = fibonacci[mid]
            else:
                target = fibonacci[low] + fibonacci[mid]

            if previousMove * 2 < current - target and not isFirstMove:
                # repeat search until index 0 is searched
                low = low - 1
                valid2 = True
                if low < 0:
                    valid2 = False
                while valid2:
                    while target + fibonacci[low] > current and valid2:
                        if low - 1 >= 0: # search through fibonacci numbers
                            low = low - 1
                        else:
                            valid2 = False # exit inner while loop
                    target = fibonacci[low] + target # set temporary target
                    if low - 1 >= 0 and previousMove * 2 < current - target: # continue searching
                        low = low - 1
                        valid2 = True
                    else:
                        valid2 = False

            # set chips to removed
            move = current - target

            # first move possible scenario: jump straight to mid
            if isFirstMove and current - fibonacci[mid] <= current / 3 and current - fibonacci[mid] > 0:
                move = current - fibonacci[mid]
            # to catch errors when chips left is 3 (not acccounted for in the fibonacci array)
            if (not isFirstMove and move > previousMove * 2) or move <= 0 or current == 3 or current / 3.0 <= move:
                move = 1
            # automatically win
            if 2 * previousMove >= current:
                move = current

        print("CY NPC took", move, "chips")
        end = time.time()
        print("This turn took:", end - start, "seconds")
        return move