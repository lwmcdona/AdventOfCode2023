import os
import re

day2Dir = os.path.dirname(__file__)
sampleFilename = os.path.join(day2Dir, 'sampleInput1.txt')
inputFilename = os.path.join(day2Dir, 'input.txt')

cube_index = {
    'red': 0,
    'green': 1,
    'blue': 2,
}

cubes = re.compile(r"(\d+) (blue|green|red)")

def sumPossibleGameIds(filename):
    with open(filename) as f:
        lines = f.readlines()
        result = 0
        for line in lines:
            draws = cubes.findall(line)
            max_cubes = {'red': 0, 'blue': 0, 'green': 0}
            for draw in draws:
                if max_cubes[draw[1]] < int(draw[0]):
                    max_cubes[draw[1]] = int(draw[0])
            power = 1
            for value in max_cubes.values():
                power *= value
            result += power
        print('Answer for {} is {}'.format(filename, result))

sumPossibleGameIds(sampleFilename)
sumPossibleGameIds(inputFilename)



