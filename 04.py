from adventofcode import AoC


EMPTY = -1
NEIGH_VECTORS = [
    (0, 1),     # row, col diff
    (0, -1),
    (1, 1),
    (1, -1),
    (1, 0),
    (-1, 1),
    (-1, 0),
    (-1, -1)
]


def parse_input(inp: str) -> list[list[int]]:
    grid = []
    for line in inp.splitlines():
        grid.append([0 if c == "@" else EMPTY for c in line])
    return grid


def el_is_roll(el):
    return el != EMPTY


def increment_neighbors(grid):
    grid_len = len(grid)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            # if element is a roll, increment all neighboring counters, else do nothing
            if not el_is_roll(grid[i][j]):
                continue
            for vec in NEIGH_VECTORS:
                (neigh_i, neigh_j) = (i + vec[0], j + vec[1])
                if neigh_i >= grid_len or neigh_i < 0 or neigh_j >= grid_len or neigh_j < 0:
                    continue

                if el_is_roll(grid[neigh_i][neigh_j]):
                    grid[neigh_i][neigh_j] += 1


def part1(inp: str) -> str | int | None:
    grid = parse_input(inp)
    increment_neighbors(grid)
    return sum(1 for row in grid for el in row if el_is_roll(el) and el < 4)


def reparse_grid(grid):
    new_grid = []
    for i in range(len(grid)):
        new_grid.append([])
        for j in range(len(grid[i])):
            if grid[i][j] < 4:
                new_grid[i].append(EMPTY)
            else:
                new_grid[i].append(0)
    return new_grid


def part2(inp: str) -> str | int | None:
    grid = parse_input(inp)
    sum_cnt = 0
    while True:
        increment_neighbors(grid)

        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if el_is_roll(grid[i][j]) and grid[i][j] < 4:
                    grid[i][j] = -1
                    cnt += 1
        # no rolls were removed this round, finish
        if cnt == 0:
            break
        sum_cnt += cnt
        grid = reparse_grid(grid)
    return sum_cnt


aoc = AoC(part_1=part1, part_2=part2)
inp = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""
expected_result = 13
aoc.assert_p1(inp, expected_result)
aoc.submit_p1()

expected_result = 43
aoc.assert_p2(inp, expected_result)
aoc.submit_p2()
