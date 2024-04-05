import os

dayDir = os.path.dirname(__file__)
sampleFilename = os.path.join(dayDir, 'sampleInput1.txt')
inputFilename = os.path.join(dayDir, 'input.txt')

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

DIRECTIONS = {NORTH, EAST, SOUTH, WEST}

def move(pos, d):
    if d == NORTH:
        return (pos[0], pos[1] - 1)
    elif d == SOUTH:
        return (pos[0], pos[1] + 1)
    elif d == WEST:
        return (pos[0] - 1, pos[1])
    elif d == EAST: 
        return (pos[0] + 1, pos[1])

def getRow(pos, col_len):
    return int(pos[1] % col_len)

def getCol(pos, row_len):
    return int(pos[0] % row_len)

def getTile(pos, grid):
    r = getRow(pos, len(grid))
    c = getCol(pos, len(grid[0]))
    return grid[r][c]

def isValidDirection(grid, pos, d, plots):
    newPos = move(pos, d)
    if getTile(newPos, grid) == '#' or newPos in plots:
        return False
    return True

def getNewDirections(grid, pos, plots):
    exit_dirs = []
    for d in DIRECTIONS:
        if isValidDirection(grid, pos, d, plots):
            exit_dirs.append(d)
    return exit_dirs

def countPlots(grid, steps):
    pos = 0
    for i in range(len(grid)):
        if 'S' in grid[i]:
            pos = (grid[i].index('S'), i)

    count = 0
    plots = {
        0: {pos},
        1: set(),
    }
    srcs = {pos}
    while count < steps:
        count += 1
        dests = set()
        for src in srcs:
            plot_set = count % 2
            dirs = getNewDirections(grid, src, plots[plot_set])
            for exit_dir in dirs:
                newPos = move(src, exit_dir)
                plots[plot_set].add(newPos)
                dests.add(newPos)
        srcs = dests
                
    return len(plots[steps % 2])

def extrapolateValues(sequence):
    result = 0
    sequences = [sequence]
    all_zeros = False
    while not all_zeros:
        all_zeros = True  
        curr = []
        s = sequences[-1]
        for i in range(len(s) - 1):
            val = s[i + 1] - s[i]
            curr.append(s[i + 1] - s[i])
            if val != 0:
                all_zeros = False
        sequences.append(curr)

    result = 0
    for i in range(len(sequences) - 1, -1, -1):
        result += sequences[i][-1]
    return result

def getResultFromExtrapolatedValues(values, iterations):
    for i in range(iterations):
        n = extrapolateValues(values)
        values = values[1:] + [n]

    return n

def calculatePolynomialCoefficients(x, y):
    x0 = x[0]
    x1 = x[1]
    x2 = x[2]
    y0 = y[0]
    y1 = y[1]
    y2 = y[2]

    c1 = (x1**2 - x2**2) / (x2 - x1)
    c2 = (y2 - y1) / (x2 - x1)

    a = (y0 - (x0 * c2) - y2 + (x2 * c2)) / ((x0**2) + (x0 * c1) - (x2**2) - (x2 * c1))
    b = ((a * (x1**2 - x2**2)) + y2 - y1) / (x2 - x1)
    c = y2 - (a * x2**2) - (b * x2)
    return [c, b, a]

def evaluatePolynomial(x, c): 
    return int(c[2] * (x ** 2) + c[1] * x + c[0]) 

def countReachableGardenPlots(filename, steps):
    with open(filename) as f:
        grid = [[x for x in line.strip()] for line in f.readlines()]
    
    x = []
    y = []
    for i in range(4):
        xi = 65 + 131 * i
        x.append(xi)
        y.append(countPlots(grid, xi))

    c = calculatePolynomialCoefficients(x, y)
    polynomial = evaluatePolynomial(steps, c)

    # already have x=0,1,2,3 
    # means we have technically already ran 3 times
    iterations = ((steps - 65) // 131) - 3
    extrapolated = getResultFromExtrapolatedValues(y, iterations)

    print('Polynomial answer for {} is {}'.format(inputFilename, polynomial))
    print('Extrapolated answer for {} is {}'.format(inputFilename, extrapolated))

# NOTE: this solution only works with actual input, uses a trick with the size and layout of the grid to determine a polynomial
# countReachableGardenPlots(sampleFilename, 6) # 16
# countReachableGardenPlots(sampleFilename, 10) # 50
# countReachableGardenPlots(sampleFilename, 50) # 1594
# countReachableGardenPlots(sampleFilename, 100) # 6536
# countReachableGardenPlots(sampleFilename, 500) # 167004
# countReachableGardenPlots(sampleFilename, 1000) # 668697
# countReachableGardenPlots(sampleFilename, 5000) # 16733044
countReachableGardenPlots(inputFilename, 26501365) # 627960775905777