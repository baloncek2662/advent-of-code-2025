from adventofcode import AoC
from itertools import combinations
import shapely

CANDIDATES = []


def part1(inp: str) -> str | int | None:
    coordinates = []
    for line in inp.splitlines():
        coordinates.append(tuple([int(el) for el in line.split(",")]))
    max_area = 0
    for i, el in enumerate(coordinates):
        for j, el_2 in enumerate(coordinates, start=i + 1):
            diff = (abs(el[0] - el_2[0]) + 1, abs(el[1] - el_2[1]) + 1)
            area = diff[0] * diff[1]
            CANDIDATES.append((el, el_2, area))
            if area > max_area:
                max_area = area
    return max_area


def area_valid(el, el_2, valid_coordinates):
    from_x = min(el[1], el_2[1])
    to_x = max(el[1], el_2[1])

    from_y = min(el[0], el_2[0])
    to_y = max(el[0], el_2[0])
    # print(el, el_2)
    for i in range(from_x, to_x + 1):
        for j in range(from_y, to_y + 1):
            if (j, i) not in valid_coordinates:
                # print(j,i,"not in valid coordinates")
                return False
    return True


def part2_too_slow(inp: str) -> str | int | None:
    coordinates = []
    for line in inp.splitlines():
        coordinates.append(tuple([int(el) for el in line.split(",")]))
    max_area = 0
    valid_coordinates = set()
    for i, el in enumerate(coordinates):
        # valid_coordinates.add(el)
        for j, el_2 in enumerate(coordinates, start=i + 1):
            # if there is an # to the right or to the bottom of this coordinate,
            # mark all coordinates up to it as valid
            if el[0] == el_2[0]:
                from_x = min(el[1], el_2[1])
                to_x = max(el[1], el_2[1])
                for x in range(from_x, to_x + 1):
                    valid_coordinates.add((el[0], x))

            if el[1] == el_2[1]:
                from_y = min(el[0], el_2[0])
                to_y = max(el[0], el_2[0])
                for y in range(from_y, to_y + 1):
                    valid_coordinates.add((y, el[1]))

    # print(valid_coordinates)

    # edge_coordinates = set()
    # print(valid_coordinates)
    # for el in valid_coordinates:
    #     # el is edge coordinate if not all its surrounding elements are in valid_voordinages
    #     print(el, (el[0], el[1] - 1) in valid_coordinates , (el[0] - 1, el[1]) in valid_coordinates , (el[0], el[1] + 1) in valid_coordinates , (el[0] + 1, el[1]) in valid_coordinates)
    #     if not ((el[0], el[1] - 1) in valid_coordinates and (el[0] - 1, el[1]) in valid_coordinates and (el[0], el[1] + 1) in valid_coordinates and (el[0] + 1, el[1]) in valid_coordinates):
    #         edge_coordinates.add(el)
        # if (el[0], el[1] + 1) not in valid_coordinates and (el[0] - 1, el[1]) not in valid_coordinates:
        #     edge_coordinates.add(el)
        # if (el[0], el[1] + 1) not in valid_coordinates and (el[0] + 1, el[1]) not in valid_coordinates:
        #     edge_coordinates.add(el)
        # if (el[0], el[1] - 1) not in valid_coordinates and (el[0] + 1, el[1]) not in valid_coordinates:
        #     edge_coordinates.add(el)
    print(len(valid_coordinates))
    # print(edge_coordinates)

    # valid_coordinates_2 = set()
    # for i, el in enumerate(valid_coordinates):
    #     for j, el_2 in enumerate(valid_coordinates, start=i + 1):
    #         # if there is an # to the right or to the bottom of this coordinate,
    #         # mark all coordinates up to it as valid
    #         if el[0] == el_2[0]:
    #             from_x = min(el[1], el_2[1])
    #             to_x = max(el[1], el_2[1])
    #             for x in range(from_x, to_x + 1):
    #                 valid_coordinates_2.add((el[0], x))

    #         if el[1] == el_2[1]:
    #             from_y = min(el[0], el_2[0])
    #             to_y = max(el[0], el_2[0])
    #             for y in range(from_y, to_y + 1):
    #                 valid_coordinates_2.add((y, el[1]))
    # print(valid_coordinates_2)

    # use same solution as part 1, but check that all coordinates in the area are in valid_coordinates_2
    max_area = 0
    for i, el in enumerate(coordinates):
        for j, el_2 in enumerate(coordinates, start=i + 1):
            if not area_valid(el, el_2, valid_coordinates):
                continue
            # print("contains valid area!", el, el_2)
            diff = (abs(el[0] - el_2[0]) + 1, abs(el[1] - el_2[1]) + 1)
            area = diff[0] * diff[1]
            if area > max_area:
                max_area = area
    return max_area


def part2(inp: str) -> str | int | None:
    points = []
    for line in inp.splitlines():
        points.append(shapely.Point(int(el) for el in line.split(",")))
    polygon = shapely.Polygon(points)
    shapely.prepare(polygon)

    # find larges rectangle in polygon which has corners on polygon points
    pairs = combinations(points, 2)
    max_area = 0
    for p1, p2 in pairs:
        rectangle = shapely.box(p1.x, p1.y, p2.x, p2.y)
        if polygon.contains(rectangle):
            area = (abs(p1.x - p2.x) + 1) * (abs(p1.y - p2.y) + 1)
            if area > max_area:
                max_area = area
    return int(max_area)


aoc = AoC(part_1=part1, part_2=part2)
inp = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3"""
expected_result = 50
aoc.assert_p1(inp, expected_result)
aoc.submit_p1()

expected_result = 24
aoc.assert_p2(inp, expected_result)
aoc.submit_p2()
