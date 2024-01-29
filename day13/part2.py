import os

dayDir = os.path.dirname(__file__)
sampleFilename = os.path.join(dayDir, 'sampleInput1.txt')
inputFilename = os.path.join(dayDir, 'input.txt')

OPPOSITE = {
    '#': '.',
    '.': '#',
}

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

def getReflectionValues(p):
    values = []

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
                values.append(100 * (i + 1))
                # return 100 * (i + 1)


    # check for vertical reflection
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
                values.append(i + 1)
                # return i + 1
    return values

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
            oldVal = getReflectionValues(p)[0]
            newVal = 0
            for i in range(len(p)):
                for j in range(len(p[i])):
                    p[i][j] = OPPOSITE[p[i][j]]

                    vals = getReflectionValues(p)

                    p[i][j] = OPPOSITE[p[i][j]]

                    for v in vals: 
                        if oldVal != v:
                            newVal = v
                            break

                    if newVal != 0:
                        break
                    
                if newVal != 0:
                    break

            result += newVal
        
    print('Answer for {} is {}'.format(filename, result))

getSumOfLinesOfReflection(sampleFilename) # 400
getSumOfLinesOfReflection(inputFilename) # 24847