from adventofcode import AoC
import textwrap


def part1(inp: str) -> str | int | None:
    invalid_ids = []
    for r in inp.split(","):
        start = int(r.split("-")[0])
        end = int(r.split("-")[1])
        for i in range(start, end + 1):
            i_str = str(i)
            i_str_len = len(i_str)
            if i_str_len % 2 != 0:
                continue
            half_ix = int(i_str_len / 2)
            if i_str[:half_ix] == i_str[half_ix:]:
                invalid_ids.append(i)

    return sum(invalid_ids)


def get_divisors(n: int) -> list[int]:
    divs = []
    for i in range(1, int(n / 2) + 1):
        if n % i == 0:
            divs.append(i)
    return divs


def part2(inp: str) -> str | int | None:
    invalid_ids = []
    for r in inp.split(","):
        start = int(r.split("-")[0])
        end = int(r.split("-")[1])
        for i in range(start, end + 1):
            i_str = str(i)
            i_str_len = len(i_str)
            divisors = get_divisors(i_str_len)
            for div in divisors:
                equal_parts = textwrap.wrap(i_str, div)
                for ep in equal_parts:
                    if ep != equal_parts[0]:
                        break
                else:
                    invalid_ids.append(i)

    return sum(set(invalid_ids))


aoc = AoC(part_1=part1, part_2=part2)
inp = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""
expected_result = 1227775554
aoc.assert_p1(inp, expected_result)
aoc.submit_p1()

expected_result = 4174379265
aoc.assert_p2(inp, expected_result)
aoc.submit_p2()
