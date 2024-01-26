import os

dayDir = os.path.dirname(__file__)
sampleFilename = os.path.join(dayDir, 'sampleInput1.txt')
inputFilename = os.path.join(dayDir, 'input.txt')

def countArrangements(line, groups, i, streak):
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
            count = countArrangements(line, groups, i + 1, 0)
        elif streak == groups[0]:
            count = countArrangements(line, groups[1:], i + 1, 0)
    elif line[i] == '#':
        if len(groups) > 0 and streak + 1 <= groups[0]:
            count = countArrangements(line, groups, i + 1, streak + 1)
    elif line[i] == '?':
        # assume a '#'
        # check if streak would be allowed, if not, no possible arrangements
        if len(groups) > 0 and streak + 1 <= groups[0]:
            count += countArrangements(line, groups, i + 1, streak + 1)

        # assume a '.'
        if len(groups) == 0 or streak == 0:
            count += countArrangements(line, groups, i + 1, 0)
        elif streak == groups[0]:
            count += countArrangements(line, groups[1:], i + 1, 0)
    return count


def findSumOfArrangements(filename):
    result = 0
    with open(filename) as f:
        for line in f.readlines():
            [line, groups] = line.strip().split()
            groups = [int(x) for x in groups.split(',')]
            result += countArrangements(line, groups, 0, 0)
        
    print('Answer for {} is {}'.format(filename, result))

findSumOfArrangements(sampleFilename) # 21
findSumOfArrangements(inputFilename) # 7032