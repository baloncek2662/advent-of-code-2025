from adventofcode import AoC


def part1(inp: str) -> str | int | None:
    regions_str = inp.split("\n\n")[-1]
    regions = []
    for region in regions_str.splitlines():
        sides_str, counts_str = region.split(":")
        sides = tuple(int(s) for s in sides_str.split("x"))
        counts = [int(c) for c in counts_str.split()]
        regions.append({"sides" : sides, "counts" : counts})
    res = 0
    for r in regions:
        r_area = r["sides"][0] * r["sides"][1]
        els_area = sum([el * 8 for el in r["counts"]])
        if r_area > els_area:
            res += 1
    return res


def part2(inp: str) -> str | int | None:
    return None


aoc = AoC(part_1=part1, part_2=part2)
inp = """0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2"""
expected_result = 2
aoc.assert_p1(inp, expected_result)
aoc.submit_p1()

expected_result = None
aoc.assert_p2(inp, expected_result)
aoc.submit_p2()
