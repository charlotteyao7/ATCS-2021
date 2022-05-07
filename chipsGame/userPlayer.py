"""
Name: Charlotte Yao
Date: May 9, 2022
AT CS

Allows the user to play
"""


class userPlayer:

    ''' Initializer '''
    def __init__(self, name):
        self.userPlayer = ()
        self.name = name

    ''' Function that is called to make a move '''
    def makeMove(self, current, isFirstMove, previousMove):
        print("There are currently", current, "chips.")

        # Tell the user how many chips they may take
        if isFirstMove:
            print("You can take between 1 and", current - 1, "chips.")
        else:
            if (2 * previousMove) >= current:
                print("You can take between 1 and", current, "chips.")
            else:
                print("You can take between 1 and", (2 * previousMove), "chips.")

        # Ask for user input and return their input
        move = input("How many chips would you like to take? ")
        return move