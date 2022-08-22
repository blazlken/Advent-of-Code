from typing import List, Counter
from collections import Counter

def parse_input(filename:str)->Counter:
    f = open(filename, 'r')
    
    c = Counter(map(int, f.read().split(',')))

    f.close()
    return c

def increment_day(counter: Counter) -> None:
    for k in range(0, 10):
        if k not in counter:
            counter[k] = 0

    temp = counter[0]

    for k in range(9):
        counter[k] = counter[k+1]

    counter[6] += temp
    counter[8] = temp

def wait_day(starting_lanternfish: Counter, days: int) -> int:
    for _ in range(days):
        increment_day(starting_lanternfish)

    return sum(starting_lanternfish.values())

if __name__ == '__main__':
    print(f"Part 1: {wait_day(parse_input('input.txt'),80)}")
    print(f"Part 2: {wait_day(parse_input('input.txt'),256)}")