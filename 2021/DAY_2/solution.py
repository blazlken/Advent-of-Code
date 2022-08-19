from typing import List, TypeVar

T = TypeVar('A', str, int)

def parse_input(filename:str) -> List[int]:
    f = open(filename, 'r')
    output = []
    
    for l in f:
        o = l.rstrip().split(' ')
        output.append([o[0], int(o[1])])

    f.close()
    return output 

def dive(lst: List[List[T]], aimOn: bool) -> List[int]:
    depth = 0
    horizontal = 0
    aim = 0
    
    for c in lst:
        command = c[0]
        amount = c[1]

        if aimOn:
            if command == 'up':
                aim -= amount

            elif command == 'down':
                aim += amount

            elif command == 'forward':
                horizontal += amount
                depth += amount * aim

            else:
                raise ValueError("Unknown command: {command}")

        else:
            if command == 'up':
                depth -= amount

            elif command == 'down':
                depth += amount

            elif command == 'forward':
                horizontal += amount

            else:
                raise ValueError("Unknown command: {command}")

    return [horizontal, depth, aim]

if __name__ == '__main__':
    diveA = dive(parse_input("input.txt"), False)
    diveB = dive(parse_input("input.txt"), True)

    print("Part A: %s" % (diveA[0] * diveA[1]))
    print("Part A: %s" % (diveB[0] * diveB[1]))