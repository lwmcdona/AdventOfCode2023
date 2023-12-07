import os

day2Dir = os.path.dirname(__file__)
sampleFilename = os.path.join(day2Dir, 'sampleInput1.txt')
sampleFilename2 = os.path.join(day2Dir, 'sampleInput2.txt')
inputFilename = os.path.join(day2Dir, 'input.txt')

def addValueToGears(gear_values, grid, row, col_start, col_end, row_start_grid_index, value):
    searchStart = max(0, col_start - 1)
    searchEnd = col_end

    x = searchStart
    while x <= searchEnd:
        if row > 0:
            # check above
            if grid[row - 1][x] == '*':
                grid_index = row_start_grid_index + x - len(grid[row - 1])
                if not grid_index in gear_values:
                    gear_values[grid_index] = []
                gear_values[grid_index].append(value)
        if row < len(grid) - 1:
            # check below
            if grid[row + 1][x] == '*':
                grid_index = row_start_grid_index + x + len(grid[row])
                if not grid_index in gear_values:
                    gear_values[grid_index] = []
                gear_values[grid_index].append(value)
        if x == searchStart or x == searchEnd:
            # check current line
            if grid[row][x] == '*':
                grid_index = row_start_grid_index + x
                if not grid_index in gear_values:
                    gear_values[grid_index] = []
                gear_values[grid_index].append(value)
        x += 1

def sumPartNumbers(filename):
    with open(filename) as f:
        row_start_grid_index = 0
        lines = f.read().splitlines()
        gear_values = {}
        for i in range(len(lines)):
            digits = []
            start = -1
            for j in range(len(lines[i])):
                if (lines[i][j].isdigit()):
                    if start < 0:
                        start = j
                    digits.append(lines[i][j])
                elif start >= 0:
                    # check for gears
                    addValueToGears(gear_values, lines, i, start, j, row_start_grid_index, int(''.join(digits))) 
                    digits = []
                    start = -1

            if start >= 0:
                addValueToGears(gear_values, lines, i, start, j, row_start_grid_index, int(''.join(digits))) 
                digits = []
                start = -1
            row_start_grid_index += len(lines)
    result = 0
    for gear in gear_values.keys():
        if len(gear_values[gear]) == 2:
            result += (gear_values[gear][0] * gear_values[gear][1])
    
    print('Answer for {} is {}'.format(filename, result))


sumPartNumbers(sampleFilename)
sumPartNumbers(sampleFilename2)
sumPartNumbers(inputFilename)


