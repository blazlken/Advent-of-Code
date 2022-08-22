from typing import Counter, Callable
from collections import Counter

def constant_rate(start: int, stop: int) -> int:
    return abs(start-stop)

def increasing_rate(start: int, stop: int) -> int:
    return int(abs(start-stop) * (1 + abs(start-stop)) / 2)

def parse_input(filename:str)->Counter[int]:
    f = open(filename, 'r')
    c = Counter(map(int, f.read().split(',')))
    f.close()

    return c

def min_fuel(positions:Counter, f: Callable)->int:
    res = []
    max_dist = max(positions.keys())
    min_dist = min(positions.keys())

    for p in range(min_dist, max_dist+1):
        s = 0

        for i in range(min_dist, max_dist+1):
            if i in positions:
                s += positions[i] * f(i,p)

        res.append(s)
    
    return min(res)

if __name__ == '__main__':
    print(f"Part 1: {min_fuel(parse_input('input.txt'), constant_rate)}")
    print(f"Part 2: {min_fuel(parse_input('input.txt'), increasing_rate)}")