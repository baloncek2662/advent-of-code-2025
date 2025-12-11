from adventofcode import AoC
import copy


START = "you"
END = "out"


def get_out_paths(devices, device_name, curr_path, visited_paths):
    # if we've reached the end, return
    if device_name == END:
        return 1

    # check if we've already gone down this path. If yes, we are in a loop so return 0
    for p in visited_paths:
        if p == curr_path:
            return 0

    # mark the current path as visited
    visited_paths.append(copy.deepcopy(curr_path))
    out_paths_count = 0
    for output in devices[device_name]:
        curr_path.append(output)
        out_paths_count += get_out_paths(devices, output, curr_path, visited_paths)
        curr_path.remove(output)
    return out_paths_count


def part1(inp: str) -> str | int | None:
    devices = {}
    for line in inp.splitlines():
        device, outputs = line.split(":")
        devices[device] = outputs.strip().split(" ")
    return get_out_paths(devices, START, [START], [])


def part2(inp: str) -> str | int | None:
    return None


aoc = AoC(part_1=part1, part_2=part2)
inp = """aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out"""
expected_result = 5
aoc.assert_p1(inp, expected_result)
aoc.submit_p1()

expected_result = None
aoc.assert_p2(inp, expected_result)
aoc.submit_p2()
