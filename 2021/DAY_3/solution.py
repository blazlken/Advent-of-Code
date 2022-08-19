from typing import List, Any

def parse_input(filename:str) -> List[int]:
    f = open(filename, 'r')
    output = f.read().split()
    f.close()
    return output 

class PrefixTrie():
    class Node():
        def __init__(self, value: Any):
            self.value = value
            self.amount = 0
            self.children = {}
            self.end = False

        def getChild(self, value: Any):
            if value not in self.children:
                self.children[value] = self.__class__(value)

            return self.children[value]

    def __init__(self, lst: List[str]):
        self.root = self.Node(None)
        self.maxSlots = len(lst[0])

        for b in lst:
            cur = self.root
            cur.amount += 1

            for d in b:
                cur = cur.getChild(d)
                cur.amount += 1

            cur.end = True

    def calculateOxyGen(self) -> int:
        cur = self.root
        multiplier = 2 ** (self.maxSlots - 1)
        res = 0

        while not(cur.end):
            if '0' in cur.children and '1' in cur.children:
                cur0 = cur.getChild('0')
                cur1 = cur.getChild('1')

                if cur1.amount >= cur0.amount:
                    cur = cur1
                    res += multiplier

                else:
                    cur = cur0

            elif '0' in cur.children:
                cur = cur.getChild('0')

            elif '1' in cur.children:
                cur = cur.getChild('1')
                res += multiplier

            multiplier = multiplier // 2

        return res

    def calculateCO2Scrub(self) -> int:
        cur = self.root
        multiplier = 2 ** (self.maxSlots - 1)
        res = 0

        while not(cur.end):
            if '0' in cur.children and '1' in cur.children:
                cur0 = cur.getChild('0')
                cur1 = cur.getChild('1')

                if cur1.amount < cur0.amount:
                    cur = cur1
                    res += multiplier

                else:
                    cur = cur0

            elif '0' in cur.children:
                cur = cur.getChild('0')

            elif '1' in cur.children:
                cur = cur.getChild('1')
                res += multiplier

            multiplier = multiplier // 2

        return res

def calculateGammaRate(lst: List[str]) -> int:
    slotAmount = len(lst[0])
    table = [[0,0] for _ in range(slotAmount)]

    for b in lst:
        digit = 0
        for d in b:
            table[digit][int(d)] += 1
            digit += 1

    max_digits = []
    for t in table:
        if t[0] > t[1]:
            d = 0
        else:
            d = 1

        max_digits.append(d)

    return int('0b' + ''.join(list(map(str, max_digits))), base=2)

def calculateEpsilonRate(lst: List[str]) -> int:
    slotAmount = len(lst[0])

    return (2 ** slotAmount - 1) - calculateGammaRate(lst)

if __name__ == '__main__':
    trie = PrefixTrie(parse_input("input.txt"))

    print("Part A: %s" % (calculateGammaRate(parse_input("input.txt")) * calculateEpsilonRate(parse_input("input.txt"))))
    print("Part B: %s" % (trie.calculateOxyGen() * trie.calculateCO2Scrub()))