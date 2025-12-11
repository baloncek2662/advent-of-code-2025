from adventofcode import AoC
import re
import copy
from collections import deque


def is_diagram_after_moves_ok(diag: list[bool], moves):
    # start with state where all lights are off
    state = []
    for _ in range(len(diag)):
        state.append(False)

    for m in moves:
        state[m] = not state[m]

    if state == diag:
        print("winning moves:", moves)
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
        # min_presses = press(m["diag"], m["buttons"], None, set())
        total += get_min_presses(m["diag"], m["buttons"])
    return total


def part2(inp: str) -> str | int | None:
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
        # min_presses = press(m["diag"], m["buttons"], None, set())
        total += get_min_presses(m["diag"], m["buttons"])
    return total


aoc = AoC(part_1=part1, part_2=part2)
inp = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"""
expected_result = 7
aoc.assert_p1(inp, expected_result)
aoc.submit_p1()

expected_result = None
aoc.assert_p2(inp, expected_result)
aoc.submit_p2()
