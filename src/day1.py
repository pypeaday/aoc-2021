"""day 1 solutions"""
from typing import List


def get_data(filepath: str = "./data/day1_sample.txt") -> List[int]:
    """get_data.

    Args:
        filepath (str): filepath

    Returns:
        list: of integers of sonar sweep (see problem statement)
    """

    with open(filepath, "r") as f:
        data = f.readlines()

    return [int(x) for x in data]


def count_increases(data: List[int]) -> int:
    """count_increases.

    Args:
        data (List[int]): data

    Returns:
        int: number of times the depth increases
    """
    points = [j > i for i, j in zip(data[:-1], data[1:])]

    return sum(points)


def count_increases_by_window(data: List[int]) -> int:
    """count_increases_by_window.

    Args:
        data (List[int]): data

    Returns:
        int: number of times the depth increases over sliding windows of 3 measurements
    """
    points = [
        sum([i, j, k]) < sum([j, k, l])
        for i, j, k, l in zip(data[:-3], data[1:-2], data[2:-1], data[3:])
    ]
    return sum(points)


if __name__ == "__main__":
    data = get_data("./data/day1.txt")
    print(f"Day 1 Solution 1 = {count_increases(data)}")
    print(f"Day 2 Solution 1 = {count_increases_by_window(data)}")
