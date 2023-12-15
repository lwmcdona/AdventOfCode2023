import os
import re
import math

dayDir = os.path.dirname(__file__)
sampleFilename = os.path.join(dayDir, 'sampleInput1.txt')
sampleFilename2 = os.path.join(dayDir, 'sampleInput2.txt')
sampleFilename3 = os.path.join(dayDir, 'sampleInput3.txt')
inputFilename = os.path.join(dayDir, 'input.txt')

pattern = re.compile(r'(\w+) = \((\w+), (\w+)\)')

directions = {
    'L': 0,
    'R': 1,
}

def getNumSteps(filename):
    network = {}
    with open(filename) as f:
        lines = f.readlines()
        instructions = lines[0].strip()
        starting_nodes = []
        for line in lines[1:]:
            m = pattern.match(line)
            if m:
                # print(m.groups())
                network[m[1]] = (m[2], m[3])
                if m[1][-1] == 'A':
                    starting_nodes.append(m[1])

    intervals = []
    for i in range(len(starting_nodes)):
        intervals.append({})

    for n in range(len(starting_nodes)):
        i = 0
        steps = 0
        finished = False
        while not finished:
            # print(instructions[i])
            starting_nodes[n] = network[starting_nodes[n]][directions[instructions[i]]]
            steps += 1
            if starting_nodes[n][-1] == 'Z':
                if starting_nodes[n] not in intervals[n]:
                    intervals[n][starting_nodes[n]] = steps
                else:
                    finished = True

            i = (i + 1) % len(instructions)

    combinations = [[]]
    for dict in intervals:
        tmp = []
        for val in dict.values():
            for l in combinations:
                new_list = l.copy()
                new_list.append(val)
                tmp.append(new_list)
        combinations = tmp

    result = None
    for l in combinations:    
        multiple = math.lcm(*l)
        if not result:
            result = multiple
        elif multiple < result:
            result = multiple

    print('Answer for {} is {}'.format(filename, result))


getNumSteps(sampleFilename)
getNumSteps(sampleFilename2)
getNumSteps(sampleFilename3)
getNumSteps(inputFilename)