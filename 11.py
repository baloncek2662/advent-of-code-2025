import re
from adventofcode import AoC
import copy

from pygments.lexers.sql import lookahead


START = "you"
OUT = "out"
START_2 = "svr"
DAC = "dac"
FFT = "fft"


def get_out_paths(devices, device_name, curr_path, cache={}):
    if device_name == OUT:
        return 1
    if device_name in cache:
        return cache[device_name]
    out_paths_count = 0
    for output in devices[device_name]:
        curr_path.append(output)
        out_paths_count += get_out_paths(devices, output, curr_path, cache)
        curr_path.remove(output)
    cache[device_name] = out_paths_count
    return out_paths_count


def part1(inp: str) -> str | int | None:
    devices = {}
    for line in inp.splitlines():
        device, outputs = line.split(":")
        devices[device] = outputs.strip().split(" ")
    return get_out_paths(devices, START, [START])


# very important to have a different cache for each call - do not define it as a default argument
def get_paths_to(devices, device_name, to, curr_path, cache):
    if device_name == to:
        return 1
    if device_name in cache:
        return cache[device_name]
    out_paths_count = 0
    for output in devices[device_name]:
        curr_path.append(output)
        out_paths_count += get_paths_to(devices, output, to, curr_path, cache)
        curr_path.remove(output)
    cache[device_name] = out_paths_count
    return out_paths_count


def part2(inp: str) -> str | int | None:
    devices = {}
    for line in inp.splitlines():
        device_name, outputs = line.split(":")
        devices[device_name] = outputs.strip().split(" ")
    devices[OUT] = []
    # all paths that go from srv to dac to fft to out
    one = get_paths_to(devices, START_2, DAC, [START_2], {}) * get_paths_to(devices, DAC, FFT, [DAC], {}) * get_paths_to(devices, FFT, OUT, [FFT], {})
    # all paths that go from srv to fft to dac to out
    two = get_paths_to(devices, START_2, FFT, [START_2], {}) * get_paths_to(devices, FFT, DAC, [FFT], {}) * get_paths_to(devices, DAC, OUT, [DAC], {})
    return one + two


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

inp = """svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out"""
expected_result = 2
aoc.assert_p2(inp, expected_result)
aoc.submit_p2()
