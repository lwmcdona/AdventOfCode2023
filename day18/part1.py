import os
import re

dayDir = os.path.dirname(__file__)
sampleFilename = os.path.join(dayDir, 'sampleInput1.txt')
inputFilename = os.path.join(dayDir, 'input.txt')

pattern = re.compile(r'([UDRL]) (\d+) \(.*\)')

def processLine(line):
    m = pattern.match(line)
    if m: 
        return (m[1], int(m[2]))
    
def moveDigger(line, loc):
    (h, d) = line
    if h == 'U':
        loc[1] -= d
    elif h == 'D':
        loc[1] += d
    elif h == 'R':
        loc[0] += d
    elif h == 'L':
        loc[0] -= d

def calculateDeterminant(pos1, pos2):
    return (pos1[0] * pos2[1]) - (pos2[0] * pos1[1])

def calculateCubicMeters(filename):
    result = 0
    with open(filename) as f:
        lines = f.readlines()
        lines = list(map(processLine, lines))

        loc = [0, 0]
        area = 0
        exterior = 0
        for line in lines:
            prev = [loc[0], loc[1]]
            moveDigger(line, loc)
            area += calculateDeterminant(prev, loc)
            exterior += line[1]

        area = int(abs(area / 2))
        # use Pick's Theorem to calculate the number of interior points
        interior = int(area + 1 - (exterior / 2))

        result = interior + exterior
        
    print('Answer for {} is {}'.format(filename, result))


calculateCubicMeters(sampleFilename) # 62
calculateCubicMeters(inputFilename) # 34329