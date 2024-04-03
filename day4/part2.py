import os
import re

day4Dir = os.path.dirname(__file__)
sampleFilename = os.path.join(day4Dir, 'sampleInput1.txt')
inputFilename = os.path.join(day4Dir, 'input.txt')

def getNumScratchcards(i, lines, memo):
    if i in memo: 
        return memo[i]
    
    nums = lines[i].split(':')[1].split('|')
    pattern = re.compile(r'\d+')
    winning_nums = pattern.findall(nums[0])
    my_nums = pattern.findall(nums[1])

    num_cards = 1
    matching_nums = 0
    for num in my_nums:
        if num in winning_nums:
            matching_nums += 1
            num_cards += getNumScratchcards(i + matching_nums, lines, memo)
    memo[i] = num_cards
    return memo[i]

def getTotalScratchCards(filename):
    memo = {}
    with open(filename) as f:
        lines = f.readlines()
        result = 0
        for i in range(len(lines)):
            result += getNumScratchcards(i, lines, memo)
            
    print('Answer for {} is {}'.format(filename, result))

getTotalScratchCards(sampleFilename)
getTotalScratchCards(inputFilename)


