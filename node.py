# this will represent a node in the solution tree (f(n) = g(n) + h(n))
from action import Action
from state import State
from enums import AlgosEnum

GOAL = [1,2,3,4,5,6,7,8,0] # goal state for 8-puzzle
GOAL_COORDINATES = { # wehere each number is expected to be
    1: (0,0),
    2: (0,1),
    3: (0,2),
    4: (1,0),
    5: (1,1),
    6: (1,2),
    7: (2,0),
    8: (2,1),
    0: (2,2)
}

class Node:
    def __init__(self, g, heuristic, parent, action, puzzle):
        self.reachCost = g
        self.heuristicCost = self.calculateHeuristic(heuristic)
        self.totalCost = self.reachCost + self.heuristicCost
        self.parent = parent
        self.actionToReachThis = action
        self.state = State(puzzle)

    # makes it more readable
    def __lt__(self, rhs):
        return self.totalCost < rhs.totalCost
    
    def calculateHeuristic(self, mode):
        if mode == AlgosEnum.UNIFORM: # f(n) = g(n), h(n) = 0
            return 0
        return self.getHeuristic(mode)
    
    def getHeuristic(self, mode):
        if mode == AlgosEnum.MISPLACED:
            return 1
        else: # must be euclidean
            return 2


