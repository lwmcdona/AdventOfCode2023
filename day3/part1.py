import os
import re

day2Dir = os.path.dirname(__file__)
sampleFilename = os.path.join(day2Dir, 'sampleInput1.txt')
sampleFilename2 = os.path.join(day2Dir, 'sampleInput2.txt')
inputFilename = os.path.join(day2Dir, 'input.txt')

def isPartNumber(grid, row, col_start, col_end):
    searchStart = max(0, col_start - 1)
    searchEnd = col_end

    x = searchStart
    while x <= searchEnd:
        if row > 0:
            # check above
            if grid[row - 1][x] != '.' and grid[row - 1][x] != ' ' and not grid[row - 1][x].isalnum():
                # symbol found
                return True
        if row < len(grid) - 1:
            # check below
            if grid[row + 1][x] != '.' and grid[row + 1][x] != ' ' and not grid[row + 1][x].isalnum():
                # symbol found
                return True
        if x == searchStart or x == searchEnd:
            # check current line
            if grid[row][x] != '.' and grid[row][x] != ' ' and not grid[row][x].isalnum():
                # symbol found
                return True
        x += 1
    return False

def sumPartNumbers(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
        values = []
        for i in range(len(lines)):
            digits = []
            start = -1
            for j in range(len(lines[i])):
                if (lines[i][j].isdigit()):
                    if start < 0:
                        start = j
                    digits.append(lines[i][j])
                elif start >= 0:
                    # check for valid number
                    if (isPartNumber(lines, i, start, j)):
                        values.append(int(''.join(digits)))  
                    digits = []
                    start = -1

            if start >= 0:
                if (isPartNumber(lines, i, start, len(lines[i]) - 1)):
                    values.append(int(''.join(digits)))  
                digits = []
                start = -1
    result = 0
    for value in values:
        result += value
    
    print('Answer for {} is {}'.format(filename, result))


sumPartNumbers(sampleFilename)
sumPartNumbers(sampleFilename2)
sumPartNumbers(inputFilename)


