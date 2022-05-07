from userPlayer import *
from randomNPC import *
from minimaxAI import *
from expectimaxAI import *
from charlottePlayer import *

players = [userPlayer("User 1"), userPlayer("User 2"), randomNPC(), minimaxAI(), expectimaxAI(), charlottePlayer()]

print(" 1. User 1 \n 2. User 2 \n 3. Random NPC \n 4. Minimax AI \n 5. Expectimax AI \n 6. CY Player")
input1 = int(input("Select first player (1-6): "))
p1 = players[input1 - 1]
input2 = int(input("Select second player (1-6): "))
p2 = players[input2 - 1]

pile = int(input("What size pile? "))
print()

isFirstMove = True
player1Turn = True
invalidMove = False
previousMove = 0
while pile > 0:
    if player1Turn:
        print(p1.name.upper() + "'S TURN:")
        start = time.time()
        nextMove = int(p1.makeMove(pile, isFirstMove, previousMove))
    else:
        print(p2.name.upper() + "'S TURN:")
        nextMove = int(p2.makeMove(pile, isFirstMove, previousMove))
    print()

    if (not isFirstMove and nextMove > 2 * previousMove) or (isFirstMove and nextMove > pile - 1) or (nextMove < 1) or (nextMove > pile):
        invalidMove = True
        break

    pile = pile - nextMove
    previousMove = nextMove
    player1Turn = not player1Turn
    isFirstMove = False
if invalidMove:
    if player1Turn:
        print(p1.name, "made an illegal move.")
    else:
        print(p2.name, "made an illegal move.")
if player1Turn:
    print(p2.name, "wins!")
else:
    print(p1.name, "wins!")