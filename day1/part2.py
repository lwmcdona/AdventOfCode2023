import os
import re

day1Dir = os.path.dirname(__file__)
sampleFilename = os.path.join(day1Dir, 'sampleInput2.txt')
inputFilename = os.path.join(day1Dir, 'input.txt')

digits = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

value = re.compile(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))")   

def calculateTotal(filename):

    result = 0
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            matches = value.findall(line)
            print(matches)
            first = matches[0]
            last = matches[-1]
            if (first in digits):
                first = digits[first]
            if (last in digits):
                last = digits[last]
            # last = digits[matches[-1]]
            print(first + last)
            result += int(first + last)
    print('Answer for {} is {}'.format(filename, result))

calculateTotal(sampleFilename)
# calculateTotal(inputFilename)



