# this will represent a state (to be contained within a node)
from action import Action
from enums import ActionsEnum

class State:
    def __init__(self, puzzle):
        self.board = tuple(puzzle)
        self.possibleActions = self.calculatePossibleActions()
    
    def __hash__(self): # needed for tracking visited states
        return hash(self.board)
    
    def __eq__(self, rhs):
        if not isinstance(rhs, State): return False
        return self.board == rhs.board

    # need to add function that will return what type of moves
    # can be performed and on which idx
    def calculatePossibleActions(self):
        # neat trick, only consider the 0 since numbers can only move "to"
        # the 0. so treat the 0 like a real tile and find where it can move
        zero = self.board.index(0)
        zeroRow = zero / 3
        zeroCol = zero % 3 # change this three for larger puzzles

        possibleActions = []

        if zeroRow > 0: # zero can move up, think of 0th row as the top of puzzle
            possibleActions.append(Action(zero, zero - 3, ActionsEnum.UP))
        if zeroRow < 2: # change for larger puzzles, zero can move down
            possibleActions.append(Action(zero, zero + 3, ActionsEnum.DOWN))
        if zeroCol > 0 : # zero can move left
            possibleActions.append(Action(zero, zero - 1, ActionsEnum.LEFT))
        if zeroCol < 2: # zero can move right
            possibleActions.append(Action(zero, zero + 1, ActionsEnum.RIGHT))
        
        return possibleActions
    
    # need to create function that given an action, it returns a new state post-operation
    def performAction(self, action : Action):
        if action not in self.possibleActions:
            print("Invalid action passed")
            return None
        
        board = list(self.board) # tuples are immutable
        # swap the two
        board[action.srcIdx], board[action.destIdx] = board[action.destIdx], board[action.srcIdx]

        return State(tuple(board))


