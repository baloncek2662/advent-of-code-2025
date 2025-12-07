from adventofcode import AoC
from functools import lru_cache


SPLITTER = "^"
BEAM = "|"


def part1(inp: str) -> str | int | None:
    lines = [[e for e in l] for l in inp.splitlines()[1:]]
    lines[0][len(lines[0]) // 2] = BEAM
    for i, line in enumerate(lines):
        if i == len(lines) - 1:
            break

        for j, col in enumerate(line):
            if col == SPLITTER and lines[i - 1][j] == BEAM:
                # split to left but only if beam from above is not already coming down
                if j - 1 >= 0 and lines[i][j - 1] != BEAM:
                    lines[i][j - 1] = BEAM
                # split to right but only if beam from above is not already coming down
                if j + 1 < len(lines) and lines[i][j + 1] != BEAM:
                    lines[i][j + 1] = BEAM

        # send all beams straight down
        for j, col in enumerate(line):
            if col == BEAM and lines[i + 1][j] != SPLITTER:
                lines[i + 1][j] = BEAM
    res = 0
    for i, line in enumerate(lines):
        if i == len(lines) - 1:
            break
        for j, col in enumerate(line):
            if col == SPLITTER and lines[i - 1][j] == BEAM:
                res += 1
    return res

# SOLUTION WITHOUT lru_cache:
#
# def move_down(lines, i, j, cache={}):
#     if i == len(lines):
#         return 1
#     if j < 0 or j == len(lines[0]):
#         return 0
#     if (i, j) in cache:
#         return cache[(i, j)]
#     if lines[i][j] == SPLITTER:
#         all_paths = move_down(lines, i + 1, j - 1) + move_down(lines, i + 1, j + 1)
#     else:
#         all_paths = move_down(lines, i + 1, j)
#     cache[(i, j)] = all_paths
#     return all_paths


lines = []


@lru_cache(maxsize=None)
def move_down_lru(i, j):
    if i == len(lines):
        return 1
    if j < 0 or j == len(lines[0]):
        return 0
    if lines[i][j] == SPLITTER:
        all_paths = move_down_lru(i + 1, j - 1) + move_down_lru(i + 1, j + 1)
    else:
        all_paths = move_down_lru(i + 1, j)
    return all_paths


def part2(inp: str) -> str | int | None:
    global lines
    lines = [[e for e in l] for l in inp.splitlines()[1:]]
    lines[0][len(lines[0]) // 2] = "|"
    return move_down_lru(1, len(lines[0]) // 2)


aoc = AoC(part_1=part1, part_2=part2)
inp = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
..............."""
expected_result = 21
aoc.assert_p1(inp, expected_result)
aoc.submit_p1()

expected_result = 40
aoc.assert_p2(inp, expected_result)
aoc.submit_p2()
