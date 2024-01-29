import os

dayDir = os.path.dirname(__file__)
sampleFilename = os.path.join(dayDir, 'sampleInput1.txt')
inputFilename = os.path.join(dayDir, 'input.txt')

def isEqualColumn(p, l, r):
    for i in range(len(p)):
        if p[i][l] != p[i][r]:
            return False
    return True

def isEqualRow(p, t, b):
    for i in range(len(p[t])):
        if p[t][i] != p[b][i]:
            return False
    return True

def getSumOfLinesOfReflection(filename):
    result = 0
    with open(filename) as f:
        pattern_lines = [[x for x in line.strip()] for line in f.readlines()]

        patterns = []
        start = 0
        for i in range(len(pattern_lines)):
            if pattern_lines[i] == []:
                patterns.append(pattern_lines[start:i])
                start = i + 1
        patterns.append(pattern_lines[start:])

        for p in patterns:
            reflected = False

            # check for horizontal reflection
            for i in range(len(p) - 1):
                if isEqualRow(p, i, i + 1):
                    t = i - 1
                    b = i + 2
                    reflected = True
                    while t >=0 and b < len(p):
                        if not isEqualRow(p, t, b):
                            reflected = False
                            break
                        t -= 1
                        b += 1

                    if reflected:
                        result += 100 * (i + 1)

            # check for vertical reflection
            if not reflected:
                for i in range(len(p[0]) - 1):
                    if isEqualColumn(p, i, i + 1):
                        l = i - 1
                        r = i + 2
                        reflected = True
                        while l >= 0 and r < len(p[0]):
                            if not isEqualColumn(p, l, r):
                                reflected = False
                                break
                            l -= 1
                            r += 1

                        if reflected:
                            result += i + 1
        
    print('Answer for {} is {}'.format(filename, result))

getSumOfLinesOfReflection(sampleFilename) # 405
getSumOfLinesOfReflection(inputFilename) # 32035