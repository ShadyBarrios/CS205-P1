# this will represent a state (to be contained within a node)

class State:
    def __init__(self, puzzle):
        self.board = puzzle
    
    def __hash__(self): # needed for tracking visited states
        return hash(self.board)
    
    def __eq__(self, rhs):
        if not isinstance(rhs, State): return False
        return self.board == rhs.board

    # need to add function that will return what type of moves
    # can be performed and on which idx

