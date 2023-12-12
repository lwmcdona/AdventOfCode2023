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
        times = [int(x) for x in lines[0].strip().split()[1:]]
        distances = [int(x) for x in lines[1].strip().split()[1:]]

        for i in range(len(times)):
            result *= getNumWaysToWin(times[i], distances[i])
    print('Answer for {} is {}'.format(filename, result))


getAllWaysToWin(sampleFilename)
getAllWaysToWin(inputFilename)


