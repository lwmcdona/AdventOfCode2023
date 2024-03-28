import os
import re
import copy

dayDir = os.path.dirname(__file__)
sampleFilename = os.path.join(dayDir, 'sampleInput1.txt')
inputFilename = os.path.join(dayDir, 'input.txt')

workflowPattern = re.compile(r'(\w+){(.*)}')
rulePattern = re.compile(r'(?:(\w)([<>])(\d+):)*(\w+)')

FIELD = 0
OP = 1
VALUE = 2
WORKFLOW = 3

def getCombinations(workflows, wfName, combos):
    if wfName == 'A':
        return (combos['x'][1] - combos['x'][0]) * (combos['m'][1] - combos['m'][0]) * (combos['a'][1] - combos['a'][0]) * (combos['s'][1] - combos['s'][0])
    elif wfName == 'R':
        return 0
    
    numCombos = 0
    for rule in workflows[wfName]:
        if rule[OP] == '<':
            newCombos = copy.deepcopy(combos)
            newCombos[rule[FIELD]][1] = int(rule[VALUE])
            combos[rule[FIELD]][0] = int(rule[VALUE])
            numCombos += getCombinations(workflows, rule[WORKFLOW], newCombos)
        elif rule[OP] == '>':
            newCombos = copy.deepcopy(combos)
            newCombos[rule[FIELD]][0] = int(rule[VALUE]) + 1
            combos[rule[FIELD]][1] = int(rule[VALUE]) + 1
            numCombos += getCombinations(workflows, rule[WORKFLOW], newCombos)
        else:
            numCombos += getCombinations(workflows, rule[WORKFLOW], combos)
    return numCombos

def addRatingNumbersForAcceptedParts(filename):
    result = 0
    workflows = {}
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
        w = lines[0:lines.index('')]

        for workflow in w:
            m = workflowPattern.match(workflow)
            if m:
                r = m[2].split(',')
                rules = []
                for rule in r:
                    n = rulePattern.match(rule)
                    if n:
                        rules.append((n[1], n[2], n[3], n[4]))
                    workflows[m[1]] = rules

        combos = {
            'x': [1, 4001],
            'm': [1, 4001],
            'a': [1, 4001],
            's': [1, 4001],
        }

        result = getCombinations(workflows, 'in', combos)
        
    print('Answer for {} is {}'.format(filename, result))


addRatingNumbersForAcceptedParts(sampleFilename) # 167409079868000
addRatingNumbersForAcceptedParts(inputFilename) # 135506683246673