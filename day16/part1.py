import os

dayDir = os.path.dirname(__file__)
sampleFilename = os.path.join(dayDir, 'sampleInput1.txt')
sampleFilename2 = os.path.join(dayDir, 'sampleInput2.txt')
inputFilename = os.path.join(dayDir, 'input.txt')

DIRECTIONS = {}

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

# maps enter direction to exit direction
TILES = {
    '\\': {
        NORTH: [WEST],
        EAST: [SOUTH],
        SOUTH: [EAST],
        WEST: [NORTH]
    },
    '/': {
        NORTH: [EAST],
        EAST: [NORTH],
        SOUTH: [WEST],
        WEST: [SOUTH]
    },
    '|': {
        NORTH: [NORTH],
        EAST: [NORTH, SOUTH],
        SOUTH: [SOUTH],
        WEST: [NORTH, SOUTH]
    },
    '-': {
        NORTH: [EAST, WEST],
        EAST: [EAST],
        SOUTH: [EAST, WEST],
        WEST: [WEST]
    },
    '.': {
        NORTH: [NORTH], 
        EAST: [EAST],
        SOUTH: [SOUTH],
        WEST: [WEST]
    },
}

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
    return True

def getEnergized(grid, poses, num_cols):
    energized = set()
    seen = set()
    while len(poses) > 0:
        pose = poses.pop(0)
        if pose not in seen:
            (position, direction) = pose
            tile = getTile(grid, position, num_cols)
            energized.add(position)
            seen.add(pose)
            directions = TILES[tile][direction]
            for d in directions:
                if isValidDirection(grid, position, d, num_cols):
                    poses.append((position + DIRECTIONS[d], d))
    return energized

def countEnergizedTiles(filename):
    result = 0
    with open(filename) as f:
        grid = [[x for x in line.strip()] for line in f.readlines()]
        num_cols = len(grid[0])

        # change in pos for given direction
        DIRECTIONS[NORTH] = -num_cols
        DIRECTIONS[EAST] = 1
        DIRECTIONS[SOUTH] = num_cols
        DIRECTIONS[WEST] = -1

        poses = [(0, EAST)]
        energized = getEnergized(grid, poses, num_cols)
        result = len(energized)
        
    print('Answer for {} is {}'.format(filename, result))


countEnergizedTiles(sampleFilename) # 46
countEnergizedTiles(inputFilename) # 7979