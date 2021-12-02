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


if __name__ == "__main__":
    data = get_data("./data/day1.txt")
    print(f"Day 1 Solution 1 = {count_increases(data)}")
