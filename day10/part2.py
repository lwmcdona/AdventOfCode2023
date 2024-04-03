import os

dayDir = os.path.dirname(__file__)
sampleFilename = os.path.join(dayDir, 'sampleInput1.txt')
sampleFilename2 = os.path.join(dayDir, 'sampleInput2.txt')
sampleFilename3 = os.path.join(dayDir, 'sampleInput3.txt')
sampleFilename4 = os.path.join(dayDir, 'sampleInput4.txt')
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

def calculateDeterminant(pos1, pos2, row_len):
    return (getX(pos1, row_len) * getY(pos2, row_len)) - (getX(pos2, row_len) * getY(pos1, row_len))

def countEnclosedTiles(filename):
    picksResult = 0
    scanResult = 0

    with open(filename) as f:
        grid = [[x for x in line.strip()] for line in f.readlines()]
        row_len = len(grid[0])

        DIRECTIONS[NORTH] = -row_len
        DIRECTIONS[EAST] = 1
        DIRECTIONS[SOUTH] = row_len
        DIRECTIONS[WEST] = -1
    
        pos = 0
        coords = set()

        # find S in grid as initial position
        for i in range(len(grid)):
            if 'S' in grid[i]:
                pos = grid[i].index('S') + i * row_len

        
        area = 0
        coords.add(pos)

        # find a direction from S and move there
        start = pos
        direction = NORTH
        for i in range(0, 4):
            tmp = pos + DIRECTIONS[i]
            pipe = getPipe(grid, tmp, row_len)
            if pipe in SEGMENTS and i in SEGMENTS[pipe]:
                direction = i
                pos = tmp
                break

        area = area + calculateDeterminant(start, pos, row_len)
        coords.add(pos)

        # follow the pipe
        prevPos = pos
        while start != pos:
            pipe = getPipe(grid, pos, row_len)
            direction = SEGMENTS[pipe][direction]
            pos += DIRECTIONS[direction]

            area = area + calculateDeterminant(prevPos, pos, row_len)
            coords.add(pos)
            
            prevPos = pos
        
        area = int(abs(area / 2))
        
        # use Pick's theorem to calculate result
        # num enclosed = area + 1 - (num_points / 2)
        picksResult = int(area + 1 - (len(coords) / 2))

        # scan the grid to calculate result
        for i in range(len(grid)):
            region = False
            for j in range(len(grid[i])):
                if ((row_len * i) + j) in coords:
                    c = grid[i][j]
                    if c == 'S':
                        connections = []
                        if NORTH in SEGMENTS[grid[i-1][j]]:
                            connections.append(SOUTH)
                        if SOUTH in SEGMENTS[grid[i+1][j]]:
                            connections.append(NORTH)
                        if WEST in SEGMENTS[grid[i][j-1]]:
                            connections.append(EAST)
                        if EAST in SEGMENTS[grid[i][j+1]]:
                            connections.append(WEST)
                        
                        if len(connections) != 2:
                            print('ERROR')
                        for key in SEGMENTS.keys():
                            if connections[0] in SEGMENTS[key] and connections[1] in SEGMENTS[key]:
                                c = key
                                break
                        
                    if c == '|' or c == '7' or c == 'F':
                        region = not region
                else:
                    if region == True: 
                        scanResult += 1
        
    print("Pick's answer for {} is {}".format(filename, picksResult))
    print("Scan answer for {} is {}".format(filename, scanResult))

countEnclosedTiles(sampleFilename) # 1
countEnclosedTiles(sampleFilename2) # 2
countEnclosedTiles(sampleFilename3) # 8
countEnclosedTiles(sampleFilename4) # 10
countEnclosedTiles(inputFilename) # 265