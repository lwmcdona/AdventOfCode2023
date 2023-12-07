import os
import re

day2Dir = os.path.dirname(__file__)
sampleFilename = os.path.join(day2Dir, 'sampleInput1.txt')
inputFilename = os.path.join(day2Dir, 'input.txt')

allowed_cubes = {
    'red': 12,
    'green': 13,
    'blue': 14,
}

game = re.compile(r"Game (\d+)")
cubes = re.compile(r"(\d+) (blue|green|red)")

def sumPossibleGameIds(filename):
    with open(filename) as f:
        lines = f.readlines()
        result = 0
        for line in lines:
            gameNum = game.match(line)[1]
            draws = cubes.findall(line)
            possible = True
            for draw in draws:
                if allowed_cubes[draw[1]] < int(draw[0]):
                    possible = False
                    break
            if possible:
                result += int(gameNum)
        print('Answer for {} is {}'.format(filename, result))

sumPossibleGameIds(sampleFilename)
sumPossibleGameIds(inputFilename)



