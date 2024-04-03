import os
import re

dayDir = os.path.dirname(__file__)
sampleFilename = os.path.join(dayDir, 'sampleInput1.txt')
sampleFilename2 = os.path.join(dayDir, 'sampleInput2.txt')
inputFilename = os.path.join(dayDir, 'input.txt')

pattern = re.compile(r'([A-Z]+) = \(([A-Z]+), ([A-Z]+)\)')

directions = {
    'L': 0,
    'R': 1,
}

def getNumSteps(filename):
    result = 0
    network = {}
    with open(filename) as f:
        lines = f.readlines()
        instructions = lines[0].strip()
        for line in lines[1:]:
            m = pattern.match(line)
            if m:
                network[m[1]] = (m[2], m[3])
                
    node = 'AAA'
    i = 0
    while node != 'ZZZ':
        node = network[node][directions[instructions[i]]]
        i = (i + 1) % len(instructions)
        result += 1
    print('Answer for {} is {}'.format(filename, result))


getNumSteps(sampleFilename)
getNumSteps(sampleFilename2)
getNumSteps(inputFilename)


