import os

dayDir = os.path.dirname(__file__)
sampleFilename = os.path.join(dayDir, 'sampleInput1.txt')
inputFilename = os.path.join(dayDir, 'input.txt')

DIRECTIONS = {}

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

# row = pos / num_cols
# col = pos % num_cols

def getRow(pos, num_cols):
    return int(pos / num_cols)

def getCol(pos, num_cols):
    return pos % num_cols

def getTile(grid, pos, num_cols):
    r = getRow(pos, num_cols)
    c = getCol(pos, num_cols)
    return grid[r][c]

def isValidDirection(grid, position, direction, num_cols):
    r = getRow(position, num_cols)
    c = getCol(position, num_cols)

    newPos = position + DIRECTIONS[direction]
    if newPos < 0 or newPos >= len(grid) * num_cols:
        return False
    if getRow(newPos, num_cols) != r and getCol(newPos, num_cols) != c:
        return False
    if getTile(grid, newPos, num_cols) == '#':
        return False
    return True

def getPossibleDirections(grid, num_cols, pos):
    exit_dirs = []
    for d in DIRECTIONS.keys():
        if isValidDirection(grid, pos, d, num_cols):
            exit_dirs.append(d)
    return exit_dirs

def countReachableGardenPlots(filename, steps):
    result = 0
    with open(filename) as f:
        grid = [[x for x in line.strip()] for line in f.readlines()]
        num_cols = len(grid[0])

        # change in pos for given direction
        DIRECTIONS[NORTH] = -num_cols
        DIRECTIONS[EAST] = 1
        DIRECTIONS[SOUTH] = num_cols
        DIRECTIONS[WEST] = -1

        pos = 0
        for i in range(len(grid)):
            if 'S' in grid[i]:
                pos = grid[i].index('S') + i * num_cols

        count = 0
        srcs = {pos}
        while count < steps:
            dests = set()
            for src in srcs:
                dirs =  getPossibleDirections(grid, num_cols, src)
                for exit_dir in dirs:
                    newPos = src + DIRECTIONS[exit_dir]
                    dests.add(newPos)
            srcs = dests
            count += 1
                    
        result = len(srcs)
        
    print('Answer for {} is {}'.format(filename, result))

countReachableGardenPlots(sampleFilename, 6) # 16
countReachableGardenPlots(inputFilename, 64) # 3768