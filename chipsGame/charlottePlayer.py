"""
Name: Charlotte Yao
Date: May 9, 2022
AT CS

Charlotte's hard-coded player from Post AP CS (2020)

FIRST MOVE:
1. If chips left - nearest fibonacci number is less than or equal to one-third of the chips left, remove the amount of chips
needed to get to there (fibonacci numbers are significant: You want the opponent to be making the move at those numbers)
2. If not, follow the steps for "AFTER FIRST MOVE"

AFTER FIRST MOVE:
1. If there are less than two chips left, take all the chips* (check beginning and end)
2. Else:
2a. Search backwards through the array and find the first index that holds a fibonacci number where
the sum of that number and the nearest fibonacci number is greater than or equal to the chips remaining
2b. Save the sum of the two fibonacci numbers as a variable (target)
    A) If chips left and nearest fibonacci number are the same, set target to one less
    B) Else if target is equal to the chips remaining, set target to the nearest fibonacci number
2c. Repeat the following until index 0 is searched:
    A) Search through fibonacci numbers lower than previously searched until the value of target and the new index is greater than chips left
    B) Update target to the sum of this new index and the previous target
2d. If at any point in time your max move is greater or equal to the difference between current chips and target, take the difference
2e. *If at any point in time your max move is greater or equal to the chips left, take everything
2f. Take the chips needed to reach the target. If target was never found or if reaching target is not valid, take 1 (defualt catch)

"""

import time


class charlottePlayer:

    ''' Initializer '''
    def __init__(self):
        self.charlottePlayer = ()
        self.name = "CY NPC"

    ''' Function that is called to make a move '''
    def makeMove(self, current, isFirstMove, previousMove):
        print("There are currently", current, "chips.")
        start = time.time()
        if current <= 2:  # Take everything
            move = current
        else:
            # Fill array of fibonacci numbers
            fibonacci = []
            fibonacci.append(1)
            fibonacci.append(2)
            for i in range(2, 12):
                next = fibonacci[i - 1] + fibonacci[i - 2]
                fibonacci.append(next)

            # Find mid and high fibonacci numbers (chips location in the fibonacci array)
            index = len(fibonacci) - 1
            while current <= fibonacci[index]:
                index = index - 1
            mid = index

            # Search through lower fibonacci numbers
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

            if fibonacci[mid] == current:
                target = current - 1
            elif fibonacci[low] + fibonacci[mid] == current:
                target = fibonacci[mid]
            else:
                target = fibonacci[low] + fibonacci[mid]

            if previousMove * 2 < current - target and not isFirstMove:
                # Repeat search until index 0 is searched
                low = low - 1
                valid2 = True
                if low < 0:
                    valid2 = False
                while valid2:
                    while target + fibonacci[low] > current and valid2:
                        if low - 1 >= 0:  # Search through fibonacci numbers
                            low = low - 1
                        else:
                            valid2 = False  # Exit inner while loop
                    target = fibonacci[low] + target  # Set temporary target
                    if low - 1 >= 0 and previousMove * 2 < current - target:  # Continue searching
                        low = low - 1
                        valid2 = True
                    else:
                        valid2 = False

            # Set chips to removed
            move = current - target

            # First move possible scenario: jump straight to mid
            if isFirstMove and current - fibonacci[mid] <= current / 3 and current - fibonacci[mid] > 0:
                move = current - fibonacci[mid]
            # Catch errors when chips left is 3 (not acccounted for in the fibonacci array)
            if (not isFirstMove and move > previousMove * 2) or move <= 0 or current == 3 or current / 3.0 <= move:
                move = 1
            # Automatically win
            if 2 * previousMove >= current:
                move = current

        # Print and return the move
        print("CY NPC took", move, "chips")
        end = time.time()
        print("This turn took:", end - start, "seconds")
        return move