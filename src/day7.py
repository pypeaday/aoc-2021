"""day 7"""
from typing import List, Tuple


def get_data(filepath: str = "./data/day7_sample.txt") -> List[int]:

    with open(filepath, "r") as f:
        data = f.readline()
    return [int(x) for x in data.split(",")]


def find_min(data) -> Tuple[int, int]:
    """find_min.

    find the value in data such that the sum of distances from all points to a given
    point is minimized

    Args:
        data:

    Returns:
        min_position
        min_fuel
    """
    min_position = -1
    min_fuel = sum([abs(data[0] - j) for j in data if data[0] != j])

    for i in data[1:]:
        fuel = sum([abs(i - j) for j in data if i != j])
        if fuel < min_fuel:
            min_fuel = fuel
            min_position = i

    return min_position, min_fuel
