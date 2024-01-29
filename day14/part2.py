import os

dayDir = os.path.dirname(__file__)
sampleFilename = os.path.join(dayDir, 'sampleInput1.txt')
inputFilename = os.path.join(dayDir, 'input.txt')

def rollNorth(lines, max_load):
    load = 0
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == 'O':
                row = i
                while row > 0 and lines[row - 1][j] == '.':
                    lines[i][j] = '.'
                    row -= 1
                
                lines[row][j] = 'O'

                # calculate the load for rock
                load += max_load - row
    return load

def rollWest(lines, max_load):
    load = 0
    for j in range(len(lines[0])):
        for i in range(len(lines)):
            if lines[i][j] == 'O':
                col = j
                while col > 0 and lines[i][col - 1] == '.':
                    lines[i][j] = '.'
                    col -= 1
                
                lines[i][col] = 'O'

                # calculate the load for rock
                load += max_load - i
    return load

def rollSouth(lines, max_load):
    load = 0
    num_rows = len(lines)
    num_cols = len(lines[0])
    for i in range(num_rows - 1, -1, -1):
        for j in range(num_cols):
            if lines[i][j] == 'O':
                row = i
                while row < num_rows - 1 and lines[row + 1][j] == '.':
                    lines[i][j] = '.'
                    row += 1
                
                lines[row][j] = 'O'

                # calculate the load for rock
                load += max_load - row
    return load

def rollEast(lines, max_load):
    load = 0
    num_rows = len(lines)
    num_cols = len(lines[0])
    for j in range(num_cols - 1, -1, -1):
        for i in range(num_rows):
            if lines[i][j] == 'O':
                col = j
                while col < num_cols - 1 and lines[i][col + 1] == '.':
                    lines[i][j] = '.'
                    col += 1
                
                lines[i][col] = 'O'

                # calculate the load for rock
                load += max_load - i
    return load

def getTotalLoad(filename):
    result = 0
    total_cycles = 1000000000
    with open(filename) as f:
        lines = [[x for x in line.strip()] for line in f.readlines()]
        max_load = len(lines)
        
        seen = set()
        pattern = []
        matches = 0
        p_len = 0
        p_index = 0
        p_start = 0

        cycle = 0
        req_pattern_reps = 5
        while True:
            cycle += 1
            rollNorth(lines, max_load)
            rollWest(lines, max_load)
            rollSouth(lines, max_load)
            load = rollEast(lines, max_load)

            if load not in seen:
                seen.add(load)
                pattern = [load]
                matches = 0
                p_len = 1
                p_index = 0
                p_start = cycle
            else:
                if len(pattern) < p_len:
                    pattern.append(load)
                elif pattern[p_index] != load:
                    pattern.append(load)
                    p_len += 1
                elif pattern[p_index] == load:      
                    p_index += 1
                    if p_index >= len(pattern):
                        matches += 1
                        if matches >= req_pattern_reps:
                            # arbitrary number, specifies how many pattern repetitions are necessary to be accepted
                            break
                        p_index = 0

        result = pattern[(total_cycles - p_start) % len(pattern)]
        
    print('Answer for {} is {}'.format(filename, result))

getTotalLoad(sampleFilename) # 64
getTotalLoad(inputFilename) # 102055