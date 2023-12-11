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
    result = None
    maps = []
    starts = []
    seeds = []
    with open(filename) as f:
        section = -1
        for line in f.readlines():
            line = line.strip()
            if len(line) == 0:
                continue
            elif line.find('seeds') != -1:
                values = [int(x) for x in pattern.findall(line)]
                seeds = [(values[i], values[i] + values[i+1]) for i in range(0, len(values), 2)]
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

    for seed_range in seeds:
        ranges_to_process = [seed_range]
        for section in range(len(maps)):
            converted_ranges = []
            for (start, end) in ranges_to_process:
                start_index = binarySearch(starts[section], start)
                end_index = binarySearch(starts[section], end)
                for i in range(start_index, end_index + 1):
                    if i == -1: 
                        if i + 1 < len(starts[section]):
                            converted_ranges.append((start, min(starts[section][i+1], end)))
                        else: 
                            converted_ranges.append((start,  end))
                    else:

                        source_start = starts[section][i]
                        (source_end, conversion) = maps[section][source_start]

                        divider = source_end
                        convert_start = None
                        nonconvert_end = None

                        if start < source_start:
                            convert_start = source_start
                        elif start < source_end:
                            convert_start = start
                        else: 
                            divider = start

                        if end < source_end:
                            divider = end
                        elif i + 1 < len(starts[section]):
                            if end < starts[section][i + 1]:
                                nonconvert_end = end
                            else:
                                nonconvert_end = starts[section][i + 1]
                        else: 
                            nonconvert_end = end

                        if divider > source_end:
                            converted_ranges.append((divider, nonconvert_end))
                        elif divider < source_end:
                            converted_ranges.append((convert_start + conversion, divider + conversion))
                        else: 
                            converted_ranges.append((convert_start + conversion, divider + conversion))
                            if source_end != nonconvert_end:
                                converted_ranges.append((divider, nonconvert_end))
            ranges_to_process = converted_ranges

        for (lower, _) in converted_ranges:
            if not result:
                result = lower
            else: 
                result = min(result, lower)

    print('Answer for {} is {}'.format(filename, result))


getMinLocation(sampleFilename)
getMinLocation(inputFilename)


