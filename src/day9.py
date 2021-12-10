"""day 9"""
from typing import List


def get_data(filepath: str = "./data/day9_sample.txt") -> List[List[int]]:
    data = []
    with open(filepath, "r") as f:
        for line in f.readlines():
            data.append([int(x) for x in line.strip()])
    return data
