'''
Allows the user to play
'''

class userPlayer:

    def __init__(self, name):
        self.userPlayer = ()
        self.name = name

    def makeMove(self, current, isFirstMove, previousMove):
        print("There are currently", current, "chips.")
        if isFirstMove:
            print("You can take between 1 and", current - 1, "chips.")
        else:
            if (2 * previousMove) >= current:
                print("You can take between 1 and", current, "chips.")
            else:
                print("You can take between 1 and", (2 * previousMove), "chips.")
        move = input("How many chips would you like to take? ")
        return move