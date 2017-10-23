from search import *
from informedSearch import *

class EightPuzzleState(ProblemState):
    target=0

    def __init__(self, puzzleArray):
        self.puzzleArray = puzzleArray
    def __str__(self):
        # print("|" + str(self.puzzleArray[0]) + "|" + str(self.puzzleArray[1]) + "|" + str(self.puzzleArray[2]) + "|")
        # print("|" + str(self.puzzleArray[3]) + "|" + str(self.puzzleArray[4]) + "|" + str(self.puzzleArray[5]) + "|")
        # print("|" + str(self.puzzleArray[6]) + "|" + str(self.puzzleArray[7]) + "|" + str(self.puzzleArray[8]) + "|")
        return "("+str(self.puzzleArray)+")"
    def illegal(self):
        if self.target < 0 or self.target > 8: return True
        return False
    def equals(self, state):
        return self.puzzleArray == state.puzzleArray
    def up(self):
        inputArray = list(self.puzzleArray)
        a = inputArray.index(0)
        b = a - 3
        self.target = a - 3
        if b < 0: return EightPuzzleState(self.puzzleArray)
        inputArray[a], inputArray[b] = inputArray[b], inputArray[a]
        return EightPuzzleState(inputArray)
    def down(self):
        inputArray = list(self.puzzleArray)
        a = inputArray.index(0)
        b = a + 3
        self.target = a + 3
        if b > 8: return EightPuzzleState(self.puzzleArray)
        inputArray[a], inputArray[b] = inputArray[b], inputArray[a]
        return EightPuzzleState(inputArray)
    def left(self):
        inputArray = list(self.puzzleArray)
        a = inputArray.index(0)
        b = a - 1
        self.target = a - 1
        if b < 0: return EightPuzzleState(self.puzzleArray)
        inputArray[a], inputArray[b] = inputArray[b], inputArray[a]
        return EightPuzzleState(inputArray)
    def right(self):
        inputArray = list(self.puzzleArray)
        a = inputArray.index(0)
        b = a + 1
        self.target = a + 1
        if b > 8: return EightPuzzleState(self.puzzleArray)
        inputArray[a], inputArray[b] = inputArray[b], inputArray[a]
        return EightPuzzleState(inputArray)
    def operatorNames(self):
        if (self.puzzleArray.index(0) == 0):
            return ["down", "right"]
        if (self.puzzleArray.index(0) == 1):
            return ["down", "left", "right"]
        if (self.puzzleArray.index(0) == 2):
            return ["down", "left"]
        if (self.puzzleArray.index(0) == 3):
            return ["up", "down", "right"]
        if (self.puzzleArray.index(0) == 5):
            return ["up", "down", "left"]
        if (self.puzzleArray.index(0) == 6):
            return ["up", "right"]
        if (self.puzzleArray.index(0) == 7):
            return ["up", "left", "right"]
        if (self.puzzleArray.index(0) == 8):
            return ["up", "left"]
        if (self.puzzleArray.index(0) == 4):
            return ["up", "down", "left", "right"]
    def applyOperators(self):
        if (self.puzzleArray.index(0) == 0):
            return [self.down(), self.right()]
        if (self.puzzleArray.index(0) == 1):
            return [self.down(), self.left(), self.right()]
        if (self.puzzleArray.index(0) == 2):
            return [self.down(), self.left()]
        if (self.puzzleArray.index(0) == 3):
            return [self.up(), self.down(), self.right()]
        if (self.puzzleArray.index(0) == 5):
            return [self.up(), self.down(), self.left()]
        if (self.puzzleArray.index(0) == 6):
            return [self.up(), self.right()]
        if (self.puzzleArray.index(0) == 7):
            return [self.up(), self.left(), self.right()]
        if (self.puzzleArray.index(0) == 8):
            return [self.up(), self.left()]
        if (self.puzzleArray.index(0) == 4):
            return [self.up(), self.down(), self.left(), self.right()]
    def heuristic(self, state):
        """
        standard BFS
        """
        return 0
        """
        A* tiles
        """
        # if (self.puzzleArray.index(0) == state.puzzleArray.index(0)):
        #     return 0
        # else:
        #     return 1
        """
        A* dist
        """
        # size = 3
        # start = self.puzzleArray.index(0)
        # goal = state.puzzleArray.index(0)
        # distance = 0
        # while (goal != start):
        #     while (start % size != goal % size):
        #         if (start % size < goal % size):
        #             start = start + 1
        #             distance = distance + 1
        #         if (start % size > goal % size):
        #             start = start - 1
        #             distance = distance + 1
        #     if (start < goal):
        #         start = start + 3
        #         distance = distance + 1
        #     else:
        #         start = start - 3
        #         distance = distance + 1
        # return distance

# myList = [1, 3, 0, 8, 2, 4, 7, 6, 5] #A
# myList = [1, 3, 4, 8, 6, 2, 0, 7, 5] #B
# myList = [0, 1, 3, 4, 2, 5, 8, 7, 6] #C
# myList = [7, 1, 2, 8, 0, 3, 6, 5, 4] #D
# myList=[8, 1, 2, 7, 0, 4, 6, 5, 3] #E
# myList=[2, 6, 3, 4, 0, 5, 1, 8, 7] #F
# myList=[7, 3, 4, 6, 1, 5, 8, 0, 2] #G
myList=[7, 4, 5, 6, 0, 3, 8, 1, 2] #H
myGoal=[1, 2, 3, 8, 0, 4, 7, 6, 5]



InformedSearch(EightPuzzleState(myList), EightPuzzleState(myGoal))


"""
Result
             Node Expansions
Problem   BFS  A*(tiles)  A*(dist)
A	        7	    5	    3
B	        80	    63	    49
C	        238	    138	    214
D	        770	    386	    942
E	        904	    560	    556
F	        2127	1589	1065
G	        7696	5466	10297
H	        60072	41185	59416

"""
