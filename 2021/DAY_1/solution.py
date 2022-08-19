from typing import List

def parse_input(input:str) -> List[int]:
    f = open(input, 'r')
    output = list(map(int, f.read().split()))
    f.close()
    return output 

def window_increases(lst: List[int], window_size:int) -> int:
    count = 0
    prev_val = sum(lst[0:window_size])

    for i in range(window_size, len(lst)):
        cur_val = prev_val + lst[i] - lst[i-window_size]

        if cur_val > prev_val:
            count += 1

        prev_val = cur_val
        
    return count

if __name__ == '__main__':
    print("Part A: %d" % (window_increases(parse_input("input.txt"), 1)))
    print("Part B: %d" % (window_increases(parse_input("input.txt"), 3)))