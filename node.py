# this will represent a node in the solution tree (f(n) = g(n) + h(n))
from action import Action

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
    def __init__(self, g, h, parent, action, state):
        self.totalCost = g + h
        self.reachCost = g
        self.heuristicCost = h
        self.parent = parent
        self.actionToReachThis = action
        self.state = state

    # makes it more readable
    def __lt__(self, rhs):
        return self.totalCost < rhs.totalCost

