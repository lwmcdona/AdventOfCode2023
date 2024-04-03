import os
import re

day4Dir = os.path.dirname(__file__)
sampleFilename = os.path.join(day4Dir, 'sampleInput1.txt')
inputFilename = os.path.join(day4Dir, 'input.txt')

def calculateCardPoints(filename):
    result = 0
    with open(filename) as f:
        for line in f.readlines():
            points = 0
            line = line.split(':')[1].split('|')
            winning_nums = re.findall(r'\d+', line[0])
            my_nums = re.findall(r'\d+', line[1])
            for num in my_nums:
                if num in winning_nums:
                    if points == 0:
                        points = 1
                    else: 
                        points *= 2
            result += points
    print('Answer for {} is {}'.format(filename, result))

calculateCardPoints(sampleFilename)
calculateCardPoints(inputFilename)


