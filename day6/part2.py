import os
import math

dayDir = os.path.dirname(__file__)
sampleFilename = os.path.join(dayDir, 'sampleInput1.txt')
inputFilename = os.path.join(dayDir, 'input.txt')

def getNumWaysToWin(time, distance):
    root = math.sqrt((time * time) - (4 * distance))
    high = math.ceil((time + root) / 2) - 1
    low = math.floor((time - root) / 2) + 1
    return high - low + 1

def getAllWaysToWin(filename):
    result = 1
    with open(filename) as f:
        lines = f.readlines()
        time = int(''.join(lines[0].strip().split()[1:]))
        distance = int(''.join(lines[1].strip().split()[1:]))
        print(time)
        print(distance)
        result *= getNumWaysToWin(time, distance)
    print('Answer for {} is {}'.format(filename, result))


getAllWaysToWin(sampleFilename)
getAllWaysToWin(inputFilename)


