'''
An AI that implements the expectimax algorithm
'''

class expectimaxAI:

    def __init__(self):
        self.expectimaxAI = ()
        self.name = "Expectimax AI"
        self.best = -1000

    def makeMove(self, current, isFirstMove, previousMove):
        print("There are currently", current, "chips.")
        if isFirstMove:
            AIturn = True
        else:
            AIturn = False
        score, move = self.expectimax(current, isFirstMove, previousMove, AIturn, 100)
        self.best = -1000
        print("Expectimax AI took", move, "chips")
        return move

    def expectimax(self, current, isFM, pM, AIturn, depth):
        #print("there are currently", str(current), "chips")
        if depth > 0:
            if current <= 0:
                #print("current is <= 0")
                if AIturn:
                    #print("return 10")
                    return 10, None
                else:
                    #print("return -10")
                    return -10, None
            #else:
                #print('return 0')
        else:
            return 0, None

        optMove = 1
        if AIturn:
            best = -10
            if isFM:
                endIndex = current
            else:
                if (2 * pM) >= current:
                    endIndex = current + 1
                    #print("opt move =", current)
                    #best = 100
                    optMove = current
                else:
                    endIndex = 2 * pM + 1
            for i in range(1, endIndex):
                current = current - i
                AIturn = False
                score = self.expectimax(current, False, i, AIturn, depth - 1)[0]
                if score > best:
                    best = score
                    optMove = i
                current = current + i
            return best, optMove
        else:
            total = 0
            count = 0
            if isFM:
                endIndex = current
            else:
                if (2 * pM) >= current:
                    endIndex = current + 1
                    #print("there is", str(current), "left over. Highest possible move is:", str(endIndex - 1))
                else:
                    endIndex = 2 * pM + 1
            #print("endIndex:", endIndex)
            for n in range(1, endIndex):
                #print("n:", n)
                current = current - n
                AIturn = True
                count = count + 1
                score = self.expectimax(current, False, n, AIturn, depth - 1)[0]
                #print("score for n="+str(n)+" is", score)
                #print(str(score) +" +", str(total), "=", str(score+total))
                total = total + score
                current = current + n
            average = total / count
            #print("local total:", total)
            #print("count:", count)
            #print("average:", average)
            if average >= self.best:
                self.best = average
                optMove = n
                #print("best is now", self.best)
            #optMove = int(random.uniform(1, endIndex))
            return self.best, optMove