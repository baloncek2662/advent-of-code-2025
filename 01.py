from adventofcode import AoC


def part1(inp: str) -> str | int | None:
    pos = 50
    zeroes_count = 0
    for line in inp.splitlines():
        direction = line[:1]
        value = int(line[1:])
        remainder = value % 100
        if direction == "R":
            pos += remainder
            pos = pos % 100
        else:
            pos -= remainder
            if pos < 0:
                pos = 100 + pos
        if pos == 0:
            zeroes_count += 1
    return zeroes_count


def part2(inp: str) -> str | int | None:
    pos = 50
    zeroes_count = 0
    for line in inp.splitlines():
        direction = line[:1]
        value = int(line[1:])
        quotient, remainder = divmod(value, 100)
        zeroes_count += quotient
        start_pos = pos
        if direction == "R":
            pos += remainder
            if pos // 100 > 0 and pos % 100 != 0 and start_pos != 0:
                zeroes_count += 1
            pos = pos % 100
        else:
            pos -= remainder
            if pos < 0:
                pos = 100 + pos
                if pos != 0 and start_pos != 0:
                    zeroes_count += 1
        if pos == 0:
            zeroes_count += 1
    return zeroes_count


aoc = AoC(part_1=part1, part_2=part2)
inp = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""
expected_result = 3
aoc.assert_p1(inp, expected_result)
aoc.submit_p1()

expected_result = 6
aoc.assert_p2(inp, expected_result)
aoc.submit_p2()
