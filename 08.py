from adventofcode import AoC
import math


def get_euclidean_distance(a: tuple[int, int, int], b: tuple[int, int, int]) -> int:
    return math.sqrt(pow(a[0] - b[0], 2) + pow(a[1] - b[1], 2) + pow(a[2] - b[2], 2))


def part1(inp: str) -> str | int | None:
    boxes = []
    for line in inp.splitlines():
        boxes.append(tuple([int(el) for el in line.split(",")]))

    distances = {}
    for i, b1 in enumerate(boxes):
        for j in range(i + 1, len(boxes)):
            if i == j:
                continue
            distances[(i, j)] = get_euclidean_distance(b1, boxes[j])
    sorted_distances = sorted(
        distances.items(),
        key=lambda item: item[1]
    )
    circuits = []
    for c in range(CONNS_CNT):
        min_ixs = sorted_distances[c][0]
        box1 = boxes[min_ixs[0]]
        box2 = boxes[min_ixs[1]]
        b1_c_ix = -1
        b2_c_ix = -1
        # get indexes of circuits where boxes are connected (-1 if not found)
        for i, c in enumerate(circuits):
            if box1 in c:
                b1_c_ix = i
            if box2 in c:
                b2_c_ix = i
        # if they are in the same circuit already, do nothing
        if b1_c_ix == b2_c_ix and b1_c_ix != -1:
            continue
        # if both are in different circuits, combine the two circuits
        if b1_c_ix != -1 and b2_c_ix != -1:
            circuits[b1_c_ix] += circuits[b2_c_ix]
            del circuits[b2_c_ix]
        # if box1 is in a circuit, add box2 to it
        elif b1_c_ix != -1:
            circuits[b1_c_ix].append(box2)
        # if box2 is in a circuit, add box1 to it
        elif b2_c_ix != -1:
            circuits[b2_c_ix].append(box1)
        # if none are in a circuit, create a new circuit
        else:
            circuits.append([box1, box2])
    sorted_lens = sorted([len(el) for el in circuits])
    return math.prod(sorted_lens[-3:])


def part2(inp: str) -> str | int | None:
    boxes = []
    for line in inp.splitlines():
        boxes.append(tuple([int(el) for el in line.split(",")]))

    distances = {}
    for i, b1 in enumerate(boxes):
        for j in range(i + 1, len(boxes)):
            if i == j:
                continue
            distances[(i, j)] = get_euclidean_distance(b1, boxes[j])
    sorted_distances = sorted(
        distances.items(),
        key=lambda item: item[1]
    )
    # first put in all boxes
    circuits = []
    last_found = None
    for c in range(len(sorted_distances)):
        min_ixs = sorted_distances[c][0]
        box1 = boxes[min_ixs[0]]
        box2 = boxes[min_ixs[1]]
        b1_c_ix = -1
        b2_c_ix = -1
        # get indexes of circuits where boxes are connected (-1 if not found)
        for i, c in enumerate(circuits):
            if box1 in c:
                b1_c_ix = i
            if box2 in c:
                b2_c_ix = i
        # if they are in the same circuit already, do nothing
        if b1_c_ix == b2_c_ix and b1_c_ix != -1:
            continue
        # if both are in different circuits, combine the two circuits
        if b1_c_ix != -1 and b2_c_ix != -1:
            circuits[b1_c_ix] += circuits[b2_c_ix]
            del circuits[b2_c_ix]
        # if box1 is in a circuit, add box2 to it
        elif b1_c_ix != -1:
            circuits[b1_c_ix].append(box2)
        # if box2 is in a circuit, add box1 to it
        elif b2_c_ix != -1:
            circuits[b2_c_ix].append(box1)
        # if none are in a circuit, create a new circuit
        else:
            circuits.append([box1, box2])
        last_found = [box1, box2]
    if len(circuits) == 1:
        return last_found[0][0] * last_found[1][0]
    return None


aoc = AoC(part_1=part1, part_2=part2)
inp = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689"""
expected_result = 40
CONNS_CNT = 10
aoc.assert_p1(inp, expected_result)
# exit()
CONNS_CNT = 1000
aoc.submit_p1()

expected_result = 25272
aoc.assert_p2(inp, expected_result)
aoc.submit_p2()
