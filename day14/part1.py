import os

dayDir = os.path.dirname(__file__)
sampleFilename = os.path.join(dayDir, 'sampleInput1.txt')
inputFilename = os.path.join(dayDir, 'input.txt')

def getTotalLoad(filename):
    result = 0
    with open(filename) as f:
        lines = [[x for x in line.strip()] for line in f.readlines()]

        max_load = len(lines)

        for k in range(len(lines)):
            print(lines[k])
        print()

        for i in range(len(lines)):
            for j in range(len(lines[i])):
                if lines[i][j] == 'O':
                    row = i
                    while row > 0 and lines[row - 1][j] == '.':
                        lines[i][j] = '.'
                        row -= 1
                    
                    lines[row][j] = 'O'

                    # calculate the load for rock
                    load = max_load - row
                    result += load

        for k in range(len(lines)):
            print(lines[k])
        print()
        
    print('Answer for {} is {}'.format(filename, result))

getTotalLoad(sampleFilename) # 136
getTotalLoad(inputFilename) # 111979