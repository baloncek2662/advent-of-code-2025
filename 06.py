from operator import mul
from adventofcode import AoC
import math


def part1(inp: str) -> str | int | None:
    table = []
    for row in inp.splitlines():
        table.append(row.split())
    sum = 0
    for j in range(len(table[0])):
        operator = table[len(table) - 1][j]
        res = int(table[0][j])
        for i in range(1, len(table) - 1):
            if operator == "*":
                res *= int(table[i][j])
            elif operator == "+":
                res += int(table[i][j])
        sum += res

    return sum


def get_longest_row(table):
    longest_row = 0
    for i in range(len(table) - 1):
        if len(table[i]) > longest_row:
            longest_row = len(table[i])
    return longest_row


def col_is_separator(table, j):
    for i in range(len(table)):
        if j >= len(table[i]):
            return False
        if table[i][j] != " ":
            return False
    return True


def part2(inp: str) -> str | int | None:
    table = []
    for row in inp.splitlines():
        table.append(list(row))

    problems = []
    values = []
    longest_row = get_longest_row(table)
    for j in range(longest_row - 1, -1, -1):
        val = ""
        if col_is_separator(table, j):
            problems.append(values)
            values = []
            continue
        for i in range(len(table) - 1):
            if len(table[i]) - 1 < j:
                continue
            if table[i][j] != "":
                val += table[i][j]
        values.append(int(val))
    problems.append(values)
    operators = [t for t in table[len(table) - 1] if t != " "]
    operators = operators[::-1]
    assert len(operators) == len(problems), "Operators and problems are not the same length!"

    res = 0
    for i in range(len(operators)):
        if operators[i] == "*":
            res += math.prod(problems[i])
        elif operators[i] == "+":
            res += sum(problems[i])
    return res


aoc = AoC(part_1=part1, part_2=part2)
inp = """123 328  51 64
 45 64  387 23
  6 98  215 314
*   +   *   +
"""
expected_result = 4277556
aoc.assert_p1(inp, expected_result)
aoc.submit_p1()

expected_result = 3263827
aoc.assert_p2(inp, expected_result)
aoc.submit_p2()
