# this will represent a node in the solution tree (f(n) = g(n) + h(n))
import math
from action import Action
from state import State
from enums import AlgosEnum

GOAL = (1,2,3,4,5,6,7,8,0) # goal state for 8-puzzle
GOAL_COORDINATES = { # where each number is expected to be
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
    def __init__(self, g, mode, parent, action, state):
        self.state = state
        self.reachCost = g
        self.mode = mode
        self.heuristicCost = self.calculateHeuristic()
        self.totalCost = self.reachCost + self.heuristicCost
        self.parent = parent
        self.actionToReachThis = action

    # makes it more readable
    def __lt__(self, rhs):
        return self.totalCost < rhs.totalCost
    
    def calculateHeuristic(self):
        if self.mode == AlgosEnum.UNIFORM: # f(n) = g(n), h(n) = 0
            return 0
        return self.getHeuristic()
    
    def getHeuristic(self):
        if self.mode == AlgosEnum.MISPLACED:
            return self.misplaced()
        else: # must be euclidean
            return self.euclidean()
    
    def misplaced(self):
        counter = 0
        for idx in range(0, len(GOAL)):
            counter += int(GOAL[idx] != self.state.getTile(idx))
        return counter

    def euclidean(self):
        runningSum = 0
        for i in range(len(self.state.board)):
            if self.state.board[i] == 0: # skip blank
                continue

            row = i / 3 # Change 3 for larger puzzles
            col = i % 3 
            goal_row, goal_col = GOAL_COORDINATES[self.state.board[i]]

            # pythag!
            runningSum += math.sqrt((row - goal_row) ** 2 + (col - goal_col) ** 2)
        return runningSum

    def children(self): # generate childeren with the same heuristic
        children = []

        actions = self.state.calculatePossibleActions()
        for action in actions:
            newState = self.state.performAction(action)
            newNode = Node(self.reachCost + 1, self.mode, self, action, newState)
            children.append(newNode)

        return children

    def isGoal(self):
        return self.state.board == GOAL


