import copy

class SimpleBars(list):
    def __str__(self):
        return ''.join(self)

    def next(self):
        tmp = copy.copy(self)
        for i in range(len(self)):
            if i == 0:
                self[i] = self.createNextGen(tmp[len(tmp) - 1], tmp[i], tmp[i + 1])
            elif i == len(self) - 1:
                self[i] = self.createNextGen(tmp[i - 1], tmp[i], tmp[0])
            else:
                self[i] = self.createNextGen(tmp[i - 1], tmp[i], tmp[i + 1])
        return ''.join(self)

    def createNextGen(self, before, current, after):
        if (before == 'i' and current == 'T' and after == 'i'):
            return 'i'
        elif (before == 'i' and current == 'T'):
            return ' '
        elif (current == 'T' and after == 'i'):
            return ' '
        elif (current == 'T'):
            return 'i'
        elif (before == 'i' and current == ' ' and after == 'i'):
            return ' '
        elif (before == 'i' and current == ' '):
            return 'i'
        elif (current == ' ' and after == 'i'):
            return 'i'
        elif (current == ' '):
            return ' '
        elif (current == 'i'):
            return 'T'

class Bars(list):
    def __str__(self):
        return ''.join(self)
        
    def next(self):
        tmp = copy.copy(self)
        for i in range(len(self)):
            if i == 0:
                self[i] = self.createNextGen(tmp[len(tmp) - 1], tmp[i], tmp[i + 1])
            elif i == len(self) - 1:
                self[i] = self.createNextGen(tmp[i - 1], tmp[i], tmp[0])
            else:
                self[i] = self.createNextGen(tmp[i - 1], tmp[i], tmp[i + 1])
        return ''.join(self)

    def getIndex(self, character):
        if character == ' ':
            return 0
        elif character == 'i':
            return 1
        elif character == 'T':
            return 2
        elif character == 'I':
            return 3

    def createNextGen(self, before, current, after):
        nextGenMap = [
            [
                [' ', 'i', ' ', 'i'],
                ['T', 'I', 'T', 'I'],
                ['i', ' ', 'i', ' '],
                ['I', 'T', 'I', 'T'],
            ],
            [
                ['i', ' ', 'i', ' '],
                ['I', 'T', 'I', 'T'],
                [' ', 'i', ' ', 'i'],
                ['T', 'I', 'T', 'I'],
            ],
            [
                [' ', 'i', ' ', 'i'],
                ['T', 'I', 'T', 'I'],
                ['i', ' ', 'i', ' '],
                ['I', 'T', 'I', 'T'],
            ],
            [
                ['i', ' ', 'i', ' '],
                ['I', 'T', 'I', 'T'],
                [' ', 'i', ' ', 'i'],
                ['T', 'I', 'T', 'I'],
            ],
        ]
        return nextGenMap[self.getIndex(before)][self.getIndex(current)][self.getIndex(after)]