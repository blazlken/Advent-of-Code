from typing import Tuple, List

def parse_input(filename:str) -> List[List[Tuple[int]]]:
    f = open(filename, 'r')

    res = []
    for l in f:
        l = l.split(' -> ')
        res.append([tuple(map(int, l[0].split(','))),tuple(map(int, l[1].split(',')))])

    f.close()

    return res

class Line():
    def __init__(self, start: Tuple[int], stop: Tuple[int], diagonals:bool = False) -> None:
        self.list = []
        self.start = start
        self.stop = stop
        self.dx = 0
        self.dy = 0

        if self.start[0] > self.stop[0]:
            self.dx = -1

        elif self.start[0] < self.stop[0]:
            self.dx = 1

        if self.start[1] > self.stop[1]:
            self.dy = -1

        elif self.start[1] < self.stop[1]:
            self.dy = 1

        if self.dx != 0 and self.dy != 0 and not(diagonals):
            return

        self.__generate_list()

    def __generate_list(self):
        self.list = [self.start]

        while self.list[-1] != self.stop:
            self.list.append((self.list[-1][0] + self.dx, self.list[-1][1] + self.dy))

def part1(line_list: List[List[Tuple[int]]]) -> int:
    coordinates = {}

    for l in line_list:
        line = Line(l[0], l[1], False)

        for c in line.list:
            if c not in coordinates:
                coordinates[c] = 0

            coordinates[c] += 1

    count = 0
    MIN_CONDITION = 2
    for v in coordinates.values():
        if v >= MIN_CONDITION:
            count += 1

    return count

def part2(line_list: List[List[Tuple[int]]]) -> int:
    coordinates = {}

    for l in line_list:
        line = Line(l[0], l[1], True)

        for c in line.list:
            if c not in coordinates:
                coordinates[c] = 0

            coordinates[c] += 1

    count = 0
    MIN_CONDITION = 2
    for v in coordinates.values():
        if v >= MIN_CONDITION:
            count += 1

    return count

if __name__ == '__main__':
    print(f"Part 1: {part1(parse_input('input.txt'))}")
    print(f"Part 2: {part2(parse_input('input.txt'))}")