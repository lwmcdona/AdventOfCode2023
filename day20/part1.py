import os

dayDir = os.path.dirname(__file__)
sampleFilename = os.path.join(dayDir, 'sampleInput1.txt')
sampleFilename2 = os.path.join(dayDir, 'sampleInput2.txt')
inputFilename = os.path.join(dayDir, 'input.txt')

# pulse is (src, dest, val)

class FlipFlop:
    def __init__(self, name, dests):
        self.name = name
        self.dests = dests
        self.state = 0

    def processPulse(self, pulse):
        (_, dest, val) = pulse
        pulses = []
        if val == 0:
            if self.state == 0:
                output = 1
            else: 
                output = 0
            self.state = not self.state
            for dest in self.dests:
                pulses.append((self.name, dest, output))
        return pulses

class Conjunction:
    def __init__(self, name, dests):
        self.name = name
        self.dests = dests
        self.memory = {}

    def addSrc(self, src):
        self.memory[src] = 0

    def processPulse(self, pulse):
        (src, dest, val) = pulse
        pulses = []
        self.memory[src] = val
        output = 0
        for v in self.memory.values():
            if v == 0:
                output = 1
                break
        for dest in self.dests:
            pulses.append((self.name, dest, output))
        return pulses

def addSrcs(name, dests, srcs):
    for dest in dests:
        if dest not in srcs:
            srcs[dest] = []
        srcs[dest].append(name)

def pushButton(queue, modules):
    low = 1
    high = 0
    while len(queue) > 0:
        pulse = queue.pop(0)
        (src, dest, val) = pulse
        if dest in modules:
            pulses = modules[dest].processPulse(pulse)
            queue.extend(pulses)
        if val == 0:
            low += 1
        else: 
            high += 1
    return (low, high)

def getMultipleOfLowAndHighPulses(filename):
    result = 0
    modules = {}
    with open(filename) as f:
        srcs = {}
        conjunctions = []
        lines = [[x.strip() for x in line.strip().split('->')] for line in f.readlines()]
        for line in lines:
            dests = [x.strip() for x in line[1].split(',')]
            if line[0][0] == '%':
                name = line[0][1:]
                modules[name] = FlipFlop(name, dests)
                addSrcs(name, dests, srcs)
            elif line[0][0] == '&':
                name = line[0][1:]
                modules[name] = Conjunction(name, dests)
                addSrcs(name, dests, srcs)
                conjunctions.append(name)
            else:
                pulses = []
                for dest in dests:
                    pulses.append(('broadcaster', dest, 0))
                addSrcs('broadcaster', dests, srcs)
        
        for c in conjunctions:
            for src in srcs[c]:
                modules[c].addSrc(src)

        low = 0
        high = 0
        for i in range(1000):
            queue = []
            queue.extend(pulses)
            (l, h) = pushButton(queue, modules)
            low += l
            high += h
        result = low * high
        
    print('Answer for {} is {}'.format(filename, result))


getMultipleOfLowAndHighPulses(sampleFilename) # 32000000
getMultipleOfLowAndHighPulses(sampleFilename2) # 11687500
getMultipleOfLowAndHighPulses(inputFilename) # 791120136