# Day 5: Hydrothermal Venture
from collections import Counter
import numpy as np


def read_data():
    with open("data.txt", "r") as f:
        data = [line.strip().split(" -> ") for line in f.readlines()]
    return [
        [tuple(map(int, start.split(","))), tuple(map(int, end.split(",")))]
        for start, end in data
    ]


def get_list_of_all_points(data):
    return [[(x1, y1), (x2, y2)] for x1, y1, x2, y2 in data]


def is_straight(line):
    x_start, y_start = line[0]
    x_end, y_end = line[1]
    return x_start == x_end or y_start == y_end


def get_all_lines(list_of_points):
    all_lines = []
    for start, end in list_of_points:
        x_start, y_start = start
        x_end, y_end = end
        print(f"Start coordinates {start}, end coordinates {end}")
        x_length = abs(x_end - x_start) + 1
        y_length = abs(y_end - y_start) + 1
        max_length = max(x_length, y_length)
        print(f"Length of x: {x_length}, length of y: {y_length}")
        x_points = np.linspace(x_start, x_end, max_length)
        y_points = np.linspace(y_start, y_end, max_length)
        line = list(zip(x_points, y_points))

        # comment out for part 2
        if is_straight(line):
            all_lines.append(line)

    return all_lines


def get_result(all_lines):
    lines = [point for line in all_lines for point in line]
    counted_points = Counter(lines)
    counter = 0
    for key, value in counted_points.items():
        if value > 1:
            counter += 1
    print(f"The number of points where at least two lines overlap: {counter}")


if __name__ == "__main__":
    list_of_points = read_data()
    print(f"List of all coordinates: {list_of_points}")
    all_lines = get_all_lines(list_of_points)
    get_result(all_lines)
