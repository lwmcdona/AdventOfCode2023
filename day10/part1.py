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
SEGMENTS = {
    '|': {
        NORTH: NORTH,
        SOUTH: SOUTH,
    },
    '-': {
        WEST: WEST,
        EAST: EAST,
    },
    'L': {
        SOUTH: EAST,
        WEST: NORTH,
    },
    'J': {
        SOUTH: WEST,
        EAST: NORTH,
    },
    '7': {
        NORTH: WEST,
        EAST: SOUTH,
    },
    'F': {
        NORTH: EAST,
        WEST: SOUTH, 
    },
    '.': {},
    'S': {},
}

# y = pos / row_len
# x = pos % row_len

def getX(pos, row_len):
    return pos % row_len

def getY(pos, row_len):
    return int(pos / row_len)

def getPipe(grid, pos, row_len):
    return grid[getY(pos, row_len)][getX(pos, row_len)]

def findFarthestSegment(filename):
    result = 0
    pos = 0
    with open(filename) as f:
        grid = [[x for x in line.strip()] for line in f.readlines()]
        row_len = len(grid[0])

        # change in pos for given direction
        DIRECTIONS[NORTH] = -row_len
        DIRECTIONS[EAST] = 1
        DIRECTIONS[SOUTH] = row_len
        DIRECTIONS[WEST] = -1

        for i in range(len(grid)):
            if 'S' in grid[i]:
                pos = grid[i].index('S') + i * row_len

        start = pos
        direction = NORTH
        steps = 0

        for i in range(0, 4):
            tmp = pos + DIRECTIONS[i]
            pipe = getPipe(grid, tmp, row_len)
            if pipe in SEGMENTS and i in SEGMENTS[pipe]:
                print(SEGMENTS[pipe])
                direction = i
                pos = tmp
                steps += 1
                print("({},{})".format(getX(pos, row_len), getY(pos, row_len)))
                break

        while start != pos:
            pipe = getPipe(grid, pos, row_len)
            direction = SEGMENTS[pipe][direction]
            pos += DIRECTIONS[direction]
            steps += 1

        result = int(steps / 2)
        
    print('Answer for {} is {}'.format(filename, result))


findFarthestSegment(sampleFilename) # 4
findFarthestSegment(sampleFilename2) # 8
findFarthestSegment(inputFilename) # 6903