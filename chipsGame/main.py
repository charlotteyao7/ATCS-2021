"""
Name: Charlotte Yao
Date: May 9, 2022
AT CS

Driver of the Chips Game that initializes the player objects and calls methods
"""

from userPlayer import *
from randomNPC import *
from minimaxAI import *
from expectimaxAI import *
from charlottePlayer import *

''' Set up the game '''
# Print the game rules
print("Welcome to the Chips Game! The rules are as follows: \n "
      "1. Two players take turns removing chips from a pile with n number of chips. \n "
      "2. The first player to play can remove between 1 and (n-1) chips. \n "
      "3. The second player can remove between 1 and 2x the previous number of chips removed by the first player. \n "
      "4. The player that removes the last chip from the pile wins. \n")

# Make an array of player choices
players = [userPlayer("User 1"), userPlayer("User 2"), randomNPC(), minimaxAI(), expectimaxAI(), charlottePlayer()]

# Ask the user for their choice of players
print("PLAYER SELECTION:")
print(" 1. User 1 \n 2. User 2 \n 3. Random NPC \n 4. Minimax AI \n 5. Expectimax AI \n 6. CY Player")
input1 = int(input("Select first player (1-6): "))
p1 = players[input1 - 1]
input2 = int(input("Select second player (1-6): "))
p2 = players[input2 - 1]

# Ask for user input on pile size
pile = int(input("What size pile? "))
print()

''' Game play '''
isFirstMove = True
player1Turn = True
invalidMove = False
previousMove = 0
while pile > 0:
    # Call the players' make move function
    if player1Turn:
        print(p1.name.upper() + "'S TURN:")
        start = time.time()
        nextMove = int(p1.makeMove(pile, isFirstMove, previousMove))
    else:
        print(p2.name.upper() + "'S TURN:")
        nextMove = int(p2.makeMove(pile, isFirstMove, previousMove))
    print()

    # Check if the move is valid
    if (not isFirstMove and nextMove > 2 * previousMove) or (isFirstMove and nextMove > pile - 1) or (nextMove < 1) or (nextMove > pile):
        invalidMove = True
        break

    # Set up for the next player's move
    pile = pile - nextMove
    previousMove = nextMove
    player1Turn = not player1Turn
    isFirstMove = False

''' Print end game results '''
# Disqualifies the player for an invalid move
if invalidMove:
    if player1Turn:
        print(p1.name, "made an illegal move.")
    else:
        print(p2.name, "made an illegal move.")

# Print the result of the game
# (the opposite because the boolean is flipped after each turn)
if player1Turn:
    print(p2.name, "wins!")
else:
    print(p1.name, "wins!")