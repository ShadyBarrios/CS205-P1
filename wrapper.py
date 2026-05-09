# this is where the solution itself will live, ill collect metrics here

class Wrapper:
    def __init__(self, puzzle):
        self.solutionDepth = 0
        self.numNodesExpanded = 0
        self.maxQueueSize = 0