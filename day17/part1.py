import os
import heapq

dayDir = os.path.dirname(__file__)
sampleFilename = os.path.join(dayDir, 'sampleInput1.txt')
inputFilename = os.path.join(dayDir, 'input.txt')

DIRECTIONS = {}

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

# maps enter direction to exit direction
REVERSE_DIRECTIONS = {
    NORTH: SOUTH,
    EAST: WEST,
    SOUTH: NORTH,
    WEST: EAST
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

def getPossibleDirections(grid, num_cols, pos, enter_dir, streak):
    exit_dirs = []
    for d in DIRECTIONS.keys():
        if d != REVERSE_DIRECTIONS[enter_dir] and isValidDirection(grid, pos, d, num_cols) and (streak < 3 or d != enter_dir):
            exit_dirs.append(d)
    return exit_dirs

# heap stores in format (loss, position, direction, streak)
def getMinHeatLoss(grid, num_cols, start, end):
    losses = {}
    pq = []
    heapq.heappush(pq, (0, start, EAST, 0))

    while pq:
        loss, pos, enter_dir, streak = heapq.heappop(pq)
        if pos == end:
            return loss

        for exit_dir in getPossibleDirections(grid, num_cols, pos, enter_dir, streak):
            newPos = pos + DIRECTIONS[exit_dir]
            newLoss = loss + getTile(grid, newPos, num_cols)
            if exit_dir == enter_dir:
                newStreak = streak + 1
            else: 
                newStreak = 1
            key = (newPos, exit_dir, newStreak)
            if key not in losses or losses[key] > newLoss:
                losses[key] = newLoss
                heapq.heappush(pq, (newLoss, newPos, exit_dir, newStreak))
    return -1

def calculateMinHeatLoss(filename):
    result = 0
    with open(filename) as f:
        grid = [[int(x) for x in line.strip()] for line in f.readlines()]
        num_cols = len(grid[0])

        # change in pos for given direction
        DIRECTIONS[NORTH] = -num_cols
        DIRECTIONS[EAST] = 1
        DIRECTIONS[SOUTH] = num_cols
        DIRECTIONS[WEST] = -1

        end = (len(grid) * num_cols) - 1
        result = getMinHeatLoss(grid, num_cols, 0, end)
        
    print('Answer for {} is {}'.format(filename, result))


calculateMinHeatLoss(sampleFilename) # 102
calculateMinHeatLoss(inputFilename) # 1023