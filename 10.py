from adventofcode import AoC
import re
import copy
from collections import deque
import numpy as np
import scipy.optimize
from scipy.optimize._constraints import LinearConstraint


def is_diagram_after_moves_ok(diag: list[bool], moves):
    # start with state where all lights are off
    state = []
    for _ in range(len(diag)):
        state.append(False)

    for m in moves:
        state[m] = not state[m]

    if state == diag:
        return True
    return False


def get_min_presses(diag, buttons):
    queue = deque()
    for i, b in enumerate(buttons):
        queue.append({
            "moves": b,
            "count": 1,
            "pressed_ixs": [i]
        })

    while True:
        el = queue.popleft()
        if is_diagram_after_moves_ok(diag, el["moves"]):
            return el["count"]
        for i, b in enumerate(buttons):
            if i not in el["pressed_ixs"]:
                new_moves = copy.deepcopy(el["moves"]) + b
                new_pressed_ixs = copy.deepcopy(el["pressed_ixs"]) + [i]
                queue.append({
                    "moves": new_moves,
                    "count": el["count"] + 1,
                    "pressed_ixs": new_pressed_ixs,
                })


def part1(inp: str) -> str | int | None:
    manuals = []
    for line in inp.splitlines():
        res = {}
        lights = re.search(r"\[(.*)\]", line)
        res["diag"] = [l == "#" for l in lights.group()[1:-1]]
        buttons = re.findall(r"\((.*?)\)", line)
        res["buttons"] = [[int(b) for b in button.split(",")] for button in buttons]
        manuals.append(res)
    total = 0
    for m in manuals:
        total += get_min_presses(m["diag"], m["buttons"])
    return total


def get_milp(buttons, joltages):
    c = np.ones(len(buttons), dtype=int)
    b = np.array(joltages, dtype=int)
    n_rows = len(joltages)
    n_cols = len(buttons)
    A = np.zeros((n_rows, n_cols), dtype=int)
    for b_ix, button in enumerate(buttons):
        for ix in button:
            A[ix, b_ix] = 1
    constraint = LinearConstraint(A, b, b)
    integrality = np.ones_like(c)
    res = scipy.optimize.milp(c=c, constraints=constraint, integrality=integrality)
    return int(sum(res.x))


def part2(inp: str) -> str | int | None:
    manuals = []
    for line in inp.splitlines():
        res = {}
        buttons = re.findall(r"\((.*?)\)", line)
        res["buttons"] = tuple(tuple(int(b) for b in button.split(",")) for button in buttons)
        joltages = re.search(r"\{(.*)\}", line)
        res["joltages"] = tuple(int(j) for j in joltages.group()[1:-1].split(","))
        manuals.append(res)
    total = 0
    for m in manuals:
        total += get_milp(m["buttons"], m["joltages"])
    return total


aoc = AoC(part_1=part1, part_2=part2)
inp = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"""
expected_result = 7
aoc.assert_p1(inp, expected_result)
aoc.submit_p1()

expected_result = 33
aoc.assert_p2(inp, expected_result)
aoc.submit_p2()
