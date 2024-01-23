import os

dayDir = os.path.dirname(__file__)
sampleFilename = os.path.join(dayDir, 'sampleInput1.txt')
inputFilename = os.path.join(dayDir, 'input.txt')

def extrapolateValues(filename):
    result = 0
    with open(filename) as f:
        lines = [line.strip().split() for line in f.readlines()]
        for line in lines:
            sequences = [[int(x) for x in line]]
            all_zeros = False
            while not all_zeros:
                all_zeros = True  
                curr = []
                s = sequences[-1]
                for i in range(len(s) - 1):
                    val = s[i + 1] - s[i]
                    curr.append(s[i + 1] - s[i])
                    if val != 0:
                        all_zeros = False
                sequences.append(curr)

            line_result = 0
            for i in range(len(sequences) - 1, -1, -1):
                line_result += sequences[i][-1]
            result += line_result
        
    print('Answer for {} is {}'.format(filename, result))


extrapolateValues(sampleFilename)
extrapolateValues(inputFilename)