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

def countArrangements(line, groups, i=0, streak=0):
    count = 0
    if i >= len(line):
        if len(groups) > 1:
            return 0
        elif len(groups) == 0 and streak > 1:
            return 0
        elif len(groups) == 1 and streak != groups[0]:
            return 0
        return 1

    if line[i] == '.':
        if len(groups) == 0 or streak == 0:
            return countArrangements(line, groups, i + 1)
        elif streak == groups[0]:
            return countArrangements(line, groups[1:], i + 1)
        return 0
    elif line[i] == '#':
        if len(groups) > 0 and streak + 1 <= groups[0]:
            return countArrangements(line, groups, i + 1, streak + 1)
        return 0
    elif line[i] == '?':
        # assume a '#'
        # check if streak would be allowed, if not, no possible arrangements
        if len(groups) > 0 and streak + 1 <= groups[0]:
            count += countArrangements(line, groups, i + 1, streak + 1)

        # assume a '.'
        if len(groups) == 0 or streak == 0:
            count += countArrangements(line, groups, i + 1)
        elif streak == groups[0]:
            count += countArrangements(line, groups[1:], i + 1)
        return count


def findSumOfArrangements(filename):
    result = 0
    with open(filename) as f:
        for line in f.readlines():
            [line, groups] = line.strip().split()
            groups = [int(x) for x in groups.split(',')]
            print(line)
            print(groups)
            groups[1:]
            result += countArrangements(line, groups)
        
        print(countArrangements('#', [1], 0, 0))
        print(countArrangements('???', [1], 0, 0))
        # grid = [[x for x in line.strip()] for line in f.readlines()]

        # # expand rows
        # expanded_rows = []
        # galaxy_cols = set()
        # i = 0
        # for i in range(len(grid)):
        #     duplicate = True
        #     expanded_rows.append(grid[i])
        #     for j in range(len(grid[i])):
        #         if grid[i][j] == '#':
        #             duplicate = False
        #             galaxy_cols.add(j)
        #     if duplicate:
        #         expanded_rows.append(grid[i])
        #         i += 1
        #     i += 1

        # # expand columns
        # expanded = []
        # for i in range(len(expanded_rows)):
        #     row = []
        #     for j in range(len(expanded_rows[i])):
        #         row.append(expanded_rows[i][j])
        #         if j not in galaxy_cols:
        #             row.append(expanded_rows[i][j])
        #     expanded.append(row)

        # # find galaxies
        # galaxies = []
        # row_len = len(expanded[0])
        # for i in range(len(expanded)):
        #     for j in range(len(expanded[i])):
        #         if expanded[i][j] == '#':
        #             galaxies.append(i * row_len + j)
        
        # result = 0
        # for i in range(len(galaxies)):
        #     for j in range(i + 1, len(galaxies)):
        #         d = getDistance(galaxies[i], galaxies[j], row_len)
        #         result += d
        
    print('Answer for {} is {}'.format(filename, result))

findSumOfArrangements(sampleFilename) # 21
findSumOfArrangements(inputFilename) # 