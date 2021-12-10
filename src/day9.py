"""day 9"""
from typing import List, Tuple


def get_data(filepath: str = "./data/day9_sample.txt") -> List[List[int]]:
    data = []
    with open(filepath, "r") as f:
        for line in f.readlines():
            data.append([int(x) for x in line.strip()])
    return data


def pad_data(data: List[List[int]]) -> List[List[int]]:

    h_padding = [9] * len(data[0])
    # v_padding = [9] * (len(data) + 2)

    h_padded_data = [h_padding, *data, h_padding]
    new_data = [[9, *row, 9] for row in h_padded_data]
    return new_data


def find_low_points(data: List[List[int]]) -> Tuple[List[Tuple[int, int]], List[int]]:
    """find_low_points.

    iterate over each point in data and find points such that they are a local min
    of the adjacent points to the left/right and up/down

    Args:
        data (List[List[int]]): data

    Returns:
        Tuple[List[Tuple[int, int]], List[int]]:
    """
    possible_low_point_indices = [
        (i, j) for i in range(len(data)) for j in range(len(data[0]))
    ]

    padded_data = pad_data(data)

    for i, row in enumerate(data):
        for j, v in enumerate(row):
            # Python optimized for "shoot first ask for forgiveness later"
            right_value = padded_data[i + 1][j + 2]
            left_value = padded_data[i + 1][j]
            top_value = padded_data[i][j + 1]
            bottom_value = padded_data[i + 2][j + 1]
            surrounding_values = [right_value, left_value, top_value, bottom_value]

            if all([v < s for s in surrounding_values]):
                pass
            else:
                possible_low_point_indices.remove((i, j))
    return possible_low_point_indices, [
        data[t[0]][t[1]] for t in possible_low_point_indices
    ]


def calculate_risk(points: List[int]) -> int:

    return sum([x + 1 for x in points])


if __name__ == "__main__":

    data = get_data("./data/day9.txt")
    # data = get_data()
    ids, values = find_low_points(data)

    print(f"Day 9 solution 1: {calculate_risk(values)}")
