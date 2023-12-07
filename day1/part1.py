import os

day1Dir = os.path.dirname(__file__)
sampleFilename = os.path.join(day1Dir, 'sampleInput1.txt')
inputFilename = os.path.join(day1Dir, 'input.txt')

def calculateTotal(filename):
    result = 0
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            first = None
            for c in line:
                if c.isdigit():
                    if not first:
                        first = c
                    last = c
            result += int(first + last)
    print('Answer for {} is {}'.format(filename, result))

calculateTotal(sampleFilename)
calculateTotal(inputFilename)



