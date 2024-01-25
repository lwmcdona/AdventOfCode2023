import os

dayDir = os.path.dirname(__file__)
sampleFilename = os.path.join(dayDir, 'sampleInput1.txt')
inputFilename = os.path.join(dayDir, 'input.txt')

def getX(pos, row_len):
    return pos % row_len

def getY(pos, row_len):
    return int(pos / row_len)

def getDistance(g1, g2, row_len):
    return abs(getX(g1, row_len) - getX(g2, row_len)) + abs(getY(g1, row_len) - getY(g2, row_len))

def findSumOfShortestDistances(filename, multiplier):
    result = 0
    m = multiplier - 1
    with open(filename) as f:
        grid = [[x for x in line.strip()] for line in f.readlines()]
        row_len = len(grid[0])

        galaxy_cols = set()

        galaxies = []
        empty_rows = []
        empty_cols = []
        expanded_galaxies = []

        i = 0
        for i in range(len(grid)):
            duplicate = True
            for j in range(len(grid[i])):
                if grid[i][j] == '#':
                    galaxies.append(i * row_len + j)
                    expanded_galaxies.append(i * row_len + j)
                    galaxy_cols.add(j)
                    duplicate = False
            if duplicate:
                empty_rows.append(i)

        for i in range(row_len):
            if i not in galaxy_cols:
                empty_cols.append(i)

        # expand rows
        expanded_row_len = row_len + (len(empty_cols) * m)
        for row in empty_rows:
            for i in range(len(galaxies)):
                if galaxies[i] > row * row_len:
                    expanded_galaxies[i] += expanded_row_len * m

        # expand cols
        for col in empty_cols:
            for i in range(len(galaxies)):
                row = getY(galaxies[i], row_len)
                expanded_galaxies[i] += row * m
                if getX(galaxies[i], row_len) > col:
                    expanded_galaxies[i] += m
        
        result = 0
        for i in range(len(expanded_galaxies)):
            for j in range(i + 1, len(expanded_galaxies)):
                d = getDistance(expanded_galaxies[i], expanded_galaxies[j], expanded_row_len)
                result += d
       
    print('Answer for {} with multiplier {} is {}'.format(filename, multiplier, result))


findSumOfShortestDistances(sampleFilename, 2) # 374
findSumOfShortestDistances(sampleFilename, 10) # 1030
findSumOfShortestDistances(sampleFilename, 100) # 8410
findSumOfShortestDistances(inputFilename, 1000000) # 560822911938