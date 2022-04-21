from userPlayer import *

pile = int(input("What size pile? "))

p1 = userPlayer("Charlotte")
p2 = userPlayer("Natalie")

isFirstMove = True
player1Turn = True
previousMove = 0
while(pile > 0):
    if player1Turn:
        print("PLAYER 1 TURN:")
        nextMove = int(p1.makeMove(pile, isFirstMove, previousMove))
    else:
        print("PLAYER 2 TURN:")
        nextMove = int(p2.makeMove(pile, isFirstMove, previousMove))
    pile = pile - nextMove
    lastMove = nextMove
    player1Turn = not player1Turn
if player1Turn:
    print(p2.name, "wins!")
else:
    print(p1.name, "wins!")