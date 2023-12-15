import os
import math

dayDir = os.path.dirname(__file__)
sampleFilename = os.path.join(dayDir, 'sampleInput1.txt')
inputFilename = os.path.join(dayDir, 'input.txt')

FIVE_OF_A_KIND = 6
FOUR_OF_A_KIND = 5
FULL_HOUSE = 4
THREE_OF_A_KIND = 3
TWO_PAIR = 2
ONE_PAIR = 1
HIGH_CARD = 0

CARD_VALUES = {
    'A': 12,
    'K': 11,
    'Q': 10,
    'T': 9, 
    '9': 8, 
    '8': 7, 
    '7': 6, 
    '6': 5, 
    '5': 4, 
    '4': 3,
    '3': 2,
    '2': 1,
    'J': 0
}

def getHandType(hand):
    jokers = 0
    counts = {}
    for c in hand:
        if c == 'J':
            jokers += 1
        elif c in counts:
            counts[c] += 1
        else:
            counts[c] = 1

    if len(counts.values()) == 0:
        matching = jokers
    else:
        matching = max(counts.values()) + jokers
        
    if matching == 5:
        return FIVE_OF_A_KIND
    if matching == 4:
        return FOUR_OF_A_KIND
    if matching == 3 and len(counts.values()) == 2:
        return FULL_HOUSE
    if matching == 3 and len(counts.values()) == 3:
        return THREE_OF_A_KIND
    if matching == 2 and len(counts.values()) == 3:
        return TWO_PAIR
    if matching == 2 and len(counts.values()) == 4:
        return ONE_PAIR
    return HIGH_CARD

def createSortingTuple(hand_tuple):
    return (
        getHandType(hand_tuple[0]),
        CARD_VALUES[hand_tuple[0][0]],
        CARD_VALUES[hand_tuple[0][1]],
        CARD_VALUES[hand_tuple[0][2]],
        CARD_VALUES[hand_tuple[0][3]],
        CARD_VALUES[hand_tuple[0][4]]
    )


def getTotalWinningsWithJoker(filename):
    result = 0
    with open(filename) as f:
        lines = f.readlines()
        hand_tuples = [(values[0], int(values[1])) for values in [line.strip().split() for line in lines]] 
        for hand in hand_tuples:
            createSortingTuple(hand)
            # print((getHandType(hand_tuples[0]), CARD_VALUES[hand_tuples[0][0]], CARD_VALUES[hand_tuples[0][1]], CARD_VALUES[hand_tuples[0][2]], CARD_VALUES[hand_tuples[0][3]], CARD_VALUES[hand_tuples[0][4]]))   
        hand_tuples.sort(key = lambda x: createSortingTuple(x), reverse=False)
        for i in range(len(hand_tuples)):
            result += (i + 1) * hand_tuples[i][1]
        # print(hands)
    print('Answer for {} is {}'.format(filename, result))


getTotalWinningsWithJoker(sampleFilename)
getTotalWinningsWithJoker(inputFilename)


