# Scott Gonzalez Barrios - sgonz266
""" SAMPLE TRACE

Welcome to my 8-Puzzle Solver. 
Type '1' to use a default puzzle, or '2' to create your own.
Enter your puzzle, using a zero to represent the blank. Please only enter valid 8-puzzles. 
Enter the puzzle demilimiting the numbers with a space. RET only when finished. 
Enter the first row: 1 2 3
Enter the second row: 4 0 6
Enter the third row: 7 5 8
Select algorithm. 
(1) for Uniform Cost Search, 
(2) for the Misplaced Tile Heuristic, or 
(3) the Manhattan Distance Heuristic.

...

"""
from enums import AlgosEnum
from util import formatPuzzle
from solver import Solver

# NOTE: IT IS IMPORTANT TO KEEP THE PUZZLES AS TUPLES SO THAT THEY CAN BE HASHED

def main():
    print("Welcome to my 8-puzzle solver.")
    try:
        puzzleChoice = int(input("Type '1' to use a default puzzle, or '2' to create your own. "))
    except ValueError: # incase they put string values or something
        print("Invalid input type. Try again")
        return
    
    if puzzleChoice != 1 and puzzleChoice != 2:
        print("Invalid choice. Try again.")
        return

    if puzzleChoice == 1: # just put this random seq of numbers from the example
        puzzle = (0, 1, 2, 4, 5, 3, 7, 8, 6)
    else:
        print("Enter your puzzle, using a zero to represent the blank. Please only enter valid 8-puzzles.")
        print("Enter the puzzle demilimiting the numbers with a space. RET only when finished.")
        rowOne = input("Enter the first row: ")
        rowTwo = input("Enter the second row: ")
        rowThree = input("Enter the third row: ")

        rowOne = rowOne.split()
        rowTwo = rowTwo.split()
        rowThree = rowThree.split()

        rows = [rowOne, rowTwo, rowThree]
        puzzle = []
        for i in range(0, len(rows)): # constructing the puzzle in 1d array format
            if len(rows[i]) != 3:
                print(f"Improper row input in row {i+1}. Try again.")
                return
            
            for digit in rows[i]:
                if not digit.isdigit():
                    print(f"Non-digit input detected. Try again.")
                    return
                else:
                    digit = int(digit)
                    if digit < 0 or digit > 8 or (digit in puzzle):
                        print(f"Invalid digit input detected. Try again.")
                        return
                    else:
                        puzzle.append(digit)
        
    print("Given puzzle: ")
    puzzle = tuple(puzzle)
    print(formatPuzzle(puzzle))

    try:
        print("Select algorithm.")
        print("(1) for Uniform Cost Search")
        print("(2) for the Misplaced Tile Heuristic")
        print("(3) the Manhattan Distance Heuristic.")
        algoChoice = int(input("Choice: "))
    except ValueError:
        print("Invalid input type. Try again.")
        return

    if algoChoice < 1 or algoChoice > 3:
        print("Invalid input. Try again.")
        return
    
    if algoChoice == 1: algoChoice = AlgosEnum.UNIFORM
    elif algoChoice == 2: algoChoice = AlgosEnum.MISPLACED
    elif algoChoice == 3: algoChoice = AlgosEnum.EUCLIDEAN
    
    # here i will call algo and then print out the output
    print(f"Algo Choice: {algoChoice}")
    solver = Solver(puzzle, algoChoice)
    solution = solver.solve()
    if solution.exportTrace():
        print("Solution trace exported to solutiontrace.txt")
    

if __name__ == "__main__":
    main()