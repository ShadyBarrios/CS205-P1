# this is where the solution itself will live, ill collect metrics here
from node import Node

class Solver:
    def __init__(self, puzzle, mode):
        self.solutionDepth = 0
        self.numNodesExpanded = 0
        self.maxQueueSize = 0
        self.startNode = Node(0,mode,None,None,puzzle)
        self.mode = mode;