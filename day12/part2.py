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

# dots = line
# groups = blocks
# i = i
# bi = 
# current = streak
def countArrangementsMemo(line, groups, i, gi, streak, dp):
    key = (i, gi, streak)

    if key in dp:
        return dp[key]
    
    if i >= len(line):
        if streak == 0 and gi >= len(groups):
            return 1
        elif streak == groups[gi] and gi == len(groups) - 1:
            return 1
        else:
            return 0
        
        # if gi < len(groups):
        #     return 0
        # elif gi >= len(groups) and streak > 1:
        #     return 0
        # elif gi == len(groups) - 1 and streak != groups[gi]:
        #     return 0
        # return 1
    

    count = 0
    if line[i] == '.':
        if gi >= len(groups) or streak == 0:
            count = countArrangementsMemo(line, groups, i + 1, gi, 0, dp)
        elif streak == groups[gi]:
            count = countArrangementsMemo(line, groups, i + 1, gi + 1, 0, dp)
    elif line[i] == '#':
        if gi < len(groups) and streak + 1 <= groups[gi]:
            count = countArrangementsMemo(line, groups, i + 1, gi, streak + 1, dp)
    elif line[i] == '?':
        # assume a '#'
        # check if streak would be allowed, if not, no possible arrangements
        if gi < len(groups) and streak + 1 <= groups[gi]:
            count += countArrangementsMemo(line, groups, i + 1, gi, streak + 1, dp)

        # assume a '.'
        if gi >= len(groups) or streak == 0:
            count += countArrangementsMemo(line, groups, i + 1, gi, 0, dp)
        elif streak == groups[gi]:
            count += countArrangementsMemo(line, groups, i + 1, gi + 1, 0, dp)

    dp[key] = count
    return count


def findSumOfArrangements(filename):
    result = 0
    with open(filename) as f:
        for line in f.readlines():
            [line, groups] = line.strip().split()
            # groups = [int(x) for x in groups.split(',')]
            groups = [int(x) for x in groups.split(',')] * 5
            line = '?'.join([line for i in range(5)])
            print(line)
            print(groups)
            dp = {}
            # count = countArrangements(line, groups, 0, 0)
            countMemo = countArrangementsMemo(line, groups, 0, 0, 0, dp)
            # if (count != countMemo):
            #     print(count, countMemo)
            result += countMemo

        
        # print(countArrangements('#', [1], 0, 0))
        # print(countArrangements('???', [1], 0, 0))
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

findSumOfArrangements(sampleFilename) # 525152
findSumOfArrangements(inputFilename) # 1493340882140

# import sys
# import re
# from copy import deepcopy
# from math import gcd
# from collections import defaultdict, Counter, deque
# D = open(sys.argv[1]).read().strip()
# L = D.split('\n')
# G = [[c for c in row] for row in L]

# # i == current position within dots
# # bi == current position within blocks
# # current == length of current block of '#'
# # state space is len(dots) * len(blocks) * len(dots)
# DP = {}
# def f(dots, blocks, i, bi, current):
#   key = (i, bi, current)
#   if key in DP:
#     return DP[key]
#   if i==len(dots):
#     if bi==len(blocks) and current==0:
#       return 1
#     elif bi==len(blocks)-1 and blocks[bi]==current:
#       return 1
#     else:
#       return 0
#   ans = 0
#   for c in ['.', '#']:
#     if dots[i]==c or dots[i]=='?':
#       if c=='.' and current==0:
#         ans += f(dots, blocks, i+1, bi, 0)
#       elif c=='.' and current>0 and bi<len(blocks) and blocks[bi]==current:
#         ans += f(dots, blocks, i+1, bi+1, 0)
#       elif c=='#':
#         ans += f(dots, blocks, i+1, bi, current+1)
#   DP[key] = ans
#   return ans

# for part2 in [False,True]:
#   ans = 0
#   for line in L:
#     dots,blocks = line.split()
#     if part2:
#       dots = '?'.join([dots, dots, dots, dots, dots])
#       blocks = ','.join([blocks, blocks, blocks, blocks, blocks])
#     blocks = [int(x) for x in blocks.split(',')]
#     DP.clear()
#     score = f(dots, blocks, 0, 0, 0)
#     #print(dots, blocks, score, len(DP))
#     ans += score
#   print(ans)