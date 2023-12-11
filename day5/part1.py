import os
import re

dayDir = os.path.dirname(__file__)
sampleFilename = os.path.join(dayDir, 'sampleInput1.txt')
inputFilename = os.path.join(dayDir, 'input.txt')

pattern = re.compile(r'\d+')

def binarySearch(arr, target):
    lower = 0
    upper = len(arr)
    while lower < upper:
        mid = int((upper + lower) / 2)
        if (arr[mid] > target):
            upper = mid
        else: 
            lower = mid + 1
    return upper - 1

def getMinLocation(filename):
    maps = []
    starts = []
    with open(filename) as f:
        section = -1
        for line in f.readlines():
            line = line.strip()
            if len(line) == 0:
                continue
            elif line.find('seeds') != -1:
                seeds = [int(x) for x in pattern.findall(line)]
                print(seeds)
            elif line.find('map') != -1:
                section += 1
                maps.append({})
                starts.append([])
            else:
                [d_start, s_start, length] = [int(x) for x in pattern.findall(line)]
                starts[section].append(s_start)
                maps[section][s_start] = (s_start + length, d_start - s_start)

    for section in starts:
        section.sort()

    print(starts[2])

    print(binarySearch(starts[2], -1))
    print(binarySearch(starts[2], 0))
    print(binarySearch(starts[2], 1))
    print(binarySearch(starts[2], 6))
    print(binarySearch(starts[2], 7))
    print(binarySearch(starts[2], 8))
    print(binarySearch(starts[2], 10))
    print(binarySearch(starts[2], 11))
    print(binarySearch(starts[2], 12))
    print(binarySearch(starts[2], 52))
    print(binarySearch(starts[2], 53))
    print(binarySearch(starts[2], 54))

    # locations = []
    result = None
    for seed in seeds:
        print('Seed: ', seed)
        converted = seed
        for i in range(len(maps)):
            start_index = binarySearch(starts[i], converted)
            if start_index > -1:
                source_start = starts[i][start_index]
                (source_end, conversion) = maps[i][source_start]
                if converted < source_end:
                    converted += conversion
            print(converted)
        if not result:
            result = converted
        else: 
            result = min(result, converted)
    print('Answer for {} is {}'.format(filename, result))


getMinLocation(sampleFilename)
getMinLocation(inputFilename)


