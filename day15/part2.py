import os
import re

dayDir = os.path.dirname(__file__)
sampleFilename = os.path.join(dayDir, 'sampleInput1.txt')
sampleFilename2 = os.path.join(dayDir, 'sampleInput2.txt')
inputFilename = os.path.join(dayDir, 'input.txt')

contents = re.compile(r"(.*)(=|-)(\d*)")

def getHashValue(s):
    val = 0
    for c in s:
        val = (val + ord(c)) * 17 % 256
    return val

def getFocusingPower(filename):
    result = 0
    with open(filename) as f:
        steps = f.readline().strip().split(',')

        boxes = {}
        for step in steps:
            m = contents.match(step)
            label = m.group(1)
            op = m.group(2)

            box = getHashValue(label)

            if op == '=':
                val = int(m.group(3))
                if box not in boxes:
                    boxes[box] = {}
                    boxes[box][label] = val
                elif label not in boxes[box]:
                    boxes[box][label] = val
                else:
                    boxes[box][label] = val
            elif op == '-':
                if box in boxes and label in boxes[box]:
                    del boxes[box][label]

        for (box, lens) in boxes.items():
            lenses = list(lens.values())
            for i in range(len(lenses)):
                power = (box + 1) * (i + 1) * lenses[i]
                result += power

        
    print('Answer for {} is {}'.format(filename, result))

getFocusingPower(sampleFilename) # 145
getFocusingPower(inputFilename) # 241094