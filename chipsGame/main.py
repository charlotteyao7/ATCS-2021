from userPlayer import *
from randomNPC import *

pile = int(input("What size pile? "))

p1 = userPlayer("Charlotte")
#p2 = userPlayer("Natalie")
p2 = randomNPC()

isFirstMove = True
player1Turn = True
invalidMove = False
previousMove = 0
while pile > 0:
    if player1Turn:
        print(p1.name.upper() + "'S TURN:")
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