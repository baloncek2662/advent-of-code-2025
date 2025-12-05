from adventofcode import AoC


def part1(inp: str) -> str | int | None:
    parsing_ranges = True
    ranges = set()
    ids = set()
    for line in inp.splitlines():
        if line == "":
            parsing_ranges = False
            continue
        if parsing_ranges:
            ranges.add((int(line.split("-")[0]), int(line.split("-")[1])))
        else:
            ids.add(int(line))
    result = 0
    for id in ids:
        for rang in ranges:
            if id >= rang[0] and id <= rang[1]:
                result += 1
                break

    return result


def part2(inp: str) -> str | int | None:
    ranges = []
    for line in inp.splitlines():
        if line == "":
            break
        ranges.append([int(line.split("-")[0]), int(line.split("-")[1])])
    srtd_rngs = sorted(ranges)
    i = 0
    while True:
        if i < len(srtd_rngs) - 1 and srtd_rngs[i][1] >= srtd_rngs[i + 1][0]:
            if srtd_rngs[i + 1][1] > srtd_rngs[i][1]:
                srtd_rngs[i][1] = srtd_rngs[i + 1][1]
            srtd_rngs.pop(i+1)
            continue
        res = 0
        if i == len(srtd_rngs):
            break
        i += 1
    for sr in srtd_rngs:
        res += sr[1] - sr[0] + 1

    return res


aoc = AoC(part_1=part1, part_2=part2)
inp = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""
expected_result = 3
aoc.assert_p1(inp, expected_result)
aoc.submit_p1()

expected_result = 14
aoc.assert_p2(inp, expected_result)
aoc.submit_p2()
