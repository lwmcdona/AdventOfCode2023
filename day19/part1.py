import os
import re

dayDir = os.path.dirname(__file__)
sampleFilename = os.path.join(dayDir, 'sampleInput1.txt')
inputFilename = os.path.join(dayDir, 'input.txt')

workflowPattern = re.compile(r'(\w+){(.*)}')
rulePattern = re.compile(r'(?:(\w)([<>])(\d+):)*(\w+)')
partPattern = re.compile(r'{x=(\d+),m=(\d+),a=(\d+),s=(\d+)}')

FIELD = 0
OP = 1
VALUE = 2
WORKFLOW = 3

def addRatingNumbersForAcceptedParts(filename):
    result = 0
    workflows = {}
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
        emptyLineIndex = lines.index('')
        w = lines[0:emptyLineIndex]
        parts = lines[emptyLineIndex+1:]

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

        for partString in parts:
            p = partPattern.match(partString)
            if p:
                part = {
                    'x': int(p[1]),
                    'm': int(p[2]),
                    'a': int(p[3]),
                    's': int(p[4]),
                }

                workflow = workflows['in']
                i = 0
                while i < len(workflow):
                    rule = workflow[i]
                    next = None
                    if rule[OP] == '<':
                        if part[rule[FIELD]] < int(rule[VALUE]):
                            next = rule[WORKFLOW]
                        else: 
                            i += 1
                    elif rule[OP] == '>':
                        if part[rule[FIELD]] > int(rule[VALUE]):
                            next = rule[WORKFLOW]
                        else: 
                            i += 1
                    else:
                        next = rule[WORKFLOW]

                    if next:
                        if next == 'A':
                            result += part['x'] + part['m'] + part['a'] + part['s']
                            break
                        elif next == 'R':
                            break
                        else:
                            workflow = workflows[next]
                            i = 0
        
    print('Answer for {} is {}'.format(filename, result))


addRatingNumbersForAcceptedParts(sampleFilename) # 19114
addRatingNumbersForAcceptedParts(inputFilename) # 377025