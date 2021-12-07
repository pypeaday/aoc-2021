"""day 6"""
from typing import List


def get_data(filepath: str = "./data/day6_sample.txt") -> List[int]:
    with open(filepath, "r") as f:
        data = f.readlines()
    return [int(x) for x in data[0].split(",")]
