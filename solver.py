# this is where the solution itself will live, ill collect metrics here
from node import Node
from state import State
from queue import PriorityQueue
from util import formatPuzzle

class Solver:
    def __init__(self, puzzle, mode):
        self.startNode = Node(0,mode,None,None,State(puzzle))
        self.mode = mode;

    def solve(self):
        return self.heuristicSearch()
    
    def heuristicSearch(self):
        numNodesExpanded = 0
        maxQueueSize = 0

        frontier = PriorityQueue()
        visitedStates = set() # will store seen states

        if self.startNode.isGoal():
            print("GOAL STATE")
            return Solution(1, 0, 0, "")
        
        # priority queue input is (val, obj) where queue is organized by val from least to greatest
        frontier.put((self.startNode.totalCost, self.startNode))
        queueSize = 1

        output = ""
        while frontier:
            node = frontier.get()[1] # remember (val, obj)
            queueSize -= 1
            numNodesExpanded += 1

            output += f"The best state to expand with g(n) = {node.reachCost} and h(n) = {node.heuristicCost:.2f} is ...\n"
            output += f"{formatPuzzle(node.state.board)}\n"
            
            visitedStates.add(node.state)

            # Expand node adding to the frontier
            child = None
            for child in node.children():
                if child.state not in visitedStates:
                    if child.isGoal():
                        output += "GOAL STATE\n"
                        output += f"{formatPuzzle(child.state.board)}\n"
                        solution = Solution(child.reachCost, numNodesExpanded, maxQueueSize, output)
                        return solution
                    
                    frontier.put((child.totalCost, child))

                    queueSize += 1
                    if queueSize > maxQueueSize:
                        maxQueueSize = queueSize


class Solution:
    def __init__(self, depth, nodesExpanded, maxQueueSize, trace):
        self.depth = depth
        self.nodesExpanded = nodesExpanded
        self.maxQueueSize = maxQueueSize
        self.trace = trace
    
    def exportTrace(self):
        metrics = f"Solution Depth: {self.depth}\nNumber of nodes expanded: {self.nodesExpanded}\nMax Queue size: {self.maxQueueSize}\n"
        self.trace += f"\n{metrics}"

        try:
            with open("solutiontrace.txt", "w") as file:
                file.write(self.trace)
                return True
        except FileNotFoundError:
            print("Error: solutiontrace.txt could not be opened.")
            return False