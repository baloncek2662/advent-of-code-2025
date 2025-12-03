from adventofcode import AoC


def part1(inp: str) -> str | int | None:
    sum = 0
    for bank in inp.splitlines():
        bank = [int(b) for b in bank]
        value_max = max(bank)
        index_max = bank.index(value_max)
        # special case: get second max and get final number by placing it before the first one
        if index_max == len(bank) - 1:
            bank[index_max] = -1
            value_second_max = max(bank)
            sum += int(f"{value_second_max}{value_max}")
            continue

        # get highest value after the max
        bank_after_max = bank[index_max + 1:]
        value_second_max = max(bank_after_max)
        sum += int(f"{value_max}{value_second_max}")

    return sum


def get_largest_joltage(bank, digits_left, joltage):
    if digits_left == 0:
        return int(joltage)

    # find largest index which is still digits_left from the end of the bank
    next_largest_list = bank[:len(bank) - digits_left + 1]
    next_largest_value = max(next_largest_list)
    next_largest_ix = bank.index(next_largest_value)
    return get_largest_joltage(bank[next_largest_ix + 1:], digits_left - 1, joltage + str(bank[next_largest_ix]))


def part2(inp: str) -> str | int | None:
    DIGITS_CNT = 12
    sum = 0
    for bank in inp.splitlines():
        bank = [int(b) for b in bank]
        sum += get_largest_joltage(bank, DIGITS_CNT, "")
    return sum


aoc = AoC(part_1=part1, part_2=part2)
inp = """987654321111111
811111111111119
234234234234278
818181911112111"""
expected_result = 357
aoc.assert_p1(inp, expected_result)
aoc.submit_p1()

expected_result = 3121910778619
aoc.assert_p2(inp, expected_result)
aoc.submit_p2()
