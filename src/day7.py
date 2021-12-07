"""day 7"""
from typing import List


def get_data(filepath: str = "./data/day7_sample.txt") -> List[int]:

    with open(filepath, "r") as f:
        data = f.readline()
    return [int(x) for x in data.split(",")]
