from typing import List

class BingoGame():
    class BingoBoard():
        def __init__(self, board_no:int, drawn:List[bool]) -> None:
            self.board = []
            self.winning_row = []
            self.drawn = drawn
            self.board_no = board_no

        def add_row(self, row:List[int]) -> None:
            self.board.append(row)

        def generate_wins(self) -> None:
            self.winning_row = []
            
            for r in self.board:
                self.winning_row.append(r)

            for c in range(5):
                self.winning_row.append([self.board[r][c] for r in range(5)])

        def is_winner(self) -> bool:
            return any([all([self.drawn[x] for x in b]) for b in self.winning_row])

        def get_sum_score(self) -> int:
            s = 0

            for r in self.board:
                for c in r:
                    if not(self.drawn[c]):
                        s += c

            return s

    def __init__(self, filename:str) -> None:
        f = open(filename)
        self.drawn_order = list(map(int, f.readline().split(",")))
        self.drawn = [False for _ in range(100)]
        self.boards = []
        self.drawn_step = -1

        board_no = 0
        current_board = None
        for l in f:
            l = l.rstrip()
            if l == "":
                if current_board != None:
                    self.boards.append(current_board)

                board_no += 1
                current_board = self.BingoBoard(board_no, self.drawn)

            else:
                current_board.add_row([int(x) for x in l.split() if x != ""])

        self.boards.append(current_board)

        for b in self.boards:
            b.generate_wins()

        f.close()

    def set_draw(self, end: bool) -> None:
        if end:
            self.drawn_step = len(self.drawn)
            for i in range(len(self.drawn)):
                self.drawn[i] = True

        else:
            self.drawn_step = -1
            for i in range(len(self.drawn)):
                self.drawn[i] = False

    def next_step(self) -> List[BingoBoard]:
        if self.drawn_step < len(self.drawn_order):
            self.drawn_step += 1

            self.drawn[self.drawn_order[self.drawn_step]] = True
            
            if any([b.is_winner() for b in self.boards]):
                return self.boards

            return None

        else:
            raise IndexError("step out of drawn_order bounds")

    def prev_step(self) -> List[BingoBoard]:
        if self.drawn_step >= 0:
            self.drawn_step -= 1

            self.drawn[self.drawn_order[self.drawn_step]] = False
            
            if any([b.is_winner() for b in self.boards]):
                return self.boards

            return None

        else:
            raise IndexError("step out of drawn_order bounds")

def part1(game: BingoGame) -> int:
    for _ in range(len(game.drawn_order)):
        board = game.next_step()

        if board != None:
            for b in board:
                if b.is_winner():
                    return b.get_sum_score() * game.drawn_order[game.drawn_step]

    return None

def part2(game: BingoGame) -> int:
    game.set_draw(True)

    for _ in range(len(game.drawn_order)):
        c = 0
        board = game.prev_step()

        for b in board:
            if not(b.is_winner()):
                return (b.get_sum_score()-game.drawn_order[game.drawn_step]) * game.drawn_order[game.drawn_step]

    return None

if __name__ == '__main__':
    game = BingoGame("input.txt")
    print(f"Part 1: {part1(game)}")
    print(f"Part 2: {part2(game)}")