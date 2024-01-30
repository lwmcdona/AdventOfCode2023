import os

dayDir = os.path.dirname(__file__)
sampleFilename = os.path.join(dayDir, 'sampleInput1.txt')
inputFilename = os.path.join(dayDir, 'input.txt')

def getHashValue(s):
    val = 0
    for c in s:
        val = (val + ord(c)) * 17 % 256
    return val

def getSumOfHash(filename):
    result = 0
    with open(filename) as f:
        steps = f.readline().strip().split(',')

        for step in steps:
            val = getHashValue(step)
            result += val
        
    print('Answer for {} is {}'.format(filename, result))

getSumOfHash(sampleFilename) # 1320
getSumOfHash(inputFilename) # 501680