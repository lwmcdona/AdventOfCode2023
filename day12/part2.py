import os

dayDir = os.path.dirname(__file__)
sampleFilename = os.path.join(dayDir, 'sampleInput1.txt')
inputFilename = os.path.join(dayDir, 'input.txt')

def countArrangementsMemo(line, groups, i, streak, dp):
    key = (i, len(groups), streak)
    if key in dp:
        return dp[key]
    
    count = 0
    if i >= len(line):
        if len(groups) > 1:
            count = 0
        elif len(groups) == 0 and streak > 1:
            count = 0
        elif len(groups) == 1 and streak != groups[0]:
            count = 0
        else: 
            count = 1
    elif line[i] == '.':
        if len(groups) == 0 or streak == 0:
            count = countArrangementsMemo(line, groups, i + 1, 0, dp)
        elif streak == groups[0]:
            count = countArrangementsMemo(line, groups[1:], i + 1, 0, dp)
    elif line[i] == '#':
        if len(groups) > 0 and streak + 1 <= groups[0]:
            count = countArrangementsMemo(line, groups, i + 1, streak + 1, dp)
    elif line[i] == '?':
        # assume a '#'
        # check if streak would be allowed, if not, no possible arrangements
        if len(groups) > 0 and streak + 1 <= groups[0]:
            count += countArrangementsMemo(line, groups, i + 1, streak + 1, dp)

        # assume a '.'
        if len(groups) == 0 or streak == 0:
            count += countArrangementsMemo(line, groups, i + 1, 0, dp)
        elif streak == groups[0]:
            count += countArrangementsMemo(line, groups[1:], i + 1, 0, dp)
    dp[key] = count
    return count


def findSumOfArrangements(filename):
    result = 0
    with open(filename) as f:
        for line in f.readlines():
            [line, groups] = line.strip().split()
            groups = [int(x) for x in groups.split(',')] * 5
            line = '?'.join([line for _ in range(5)])

            dp = {}
            result += countArrangementsMemo(line, groups, 0, 0, dp)
        
    print('Answer for {} is {}'.format(filename, result))

findSumOfArrangements(sampleFilename) # 525152
findSumOfArrangements(inputFilename) # 1493340882140