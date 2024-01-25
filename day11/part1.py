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

def findSumOfShortestDistances(filename):
    result = 0
    with open(filename) as f:
        grid = [[x for x in line.strip()] for line in f.readlines()]

        # expand rows
        expanded_rows = []
        galaxy_cols = set()
        i = 0
        for i in range(len(grid)):
            duplicate = True
            expanded_rows.append(grid[i])
            for j in range(len(grid[i])):
                if grid[i][j] == '#':
                    duplicate = False
                    galaxy_cols.add(j)
            if duplicate:
                expanded_rows.append(grid[i])
                i += 1
            i += 1

        # expand columns
        expanded = []
        for i in range(len(expanded_rows)):
            row = []
            for j in range(len(expanded_rows[i])):
                row.append(expanded_rows[i][j])
                if j not in galaxy_cols:
                    row.append(expanded_rows[i][j])
            expanded.append(row)

        # find galaxies
        galaxies = []
        row_len = len(expanded[0])
        for i in range(len(expanded)):
            for j in range(len(expanded[i])):
                if expanded[i][j] == '#':
                    galaxies.append(i * row_len + j)
        
        result = 0
        for i in range(len(galaxies)):
            for j in range(i + 1, len(galaxies)):
                d = getDistance(galaxies[i], galaxies[j], row_len)
                result += d
        
    print('Answer for {} is {}'.format(filename, result))

findSumOfShortestDistances(sampleFilename) # 374
findSumOfShortestDistances(inputFilename) # 10033566