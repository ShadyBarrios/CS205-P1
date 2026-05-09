ROW_SIZE = 3

def formatPuzzle(puzzle):
    output = ""
    for i in range(0, len(puzzle)):
        if(i % ROW_SIZE == 0):
            output += "["
        output += str(puzzle[i])
        if (i+1) % ROW_SIZE == 0:
            output += "]\n"
        else:
            output += " "
    
    return output
