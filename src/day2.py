"""day 2 module"""
from typing import List, Tuple


def get_data(filepath: str = "./data/day2_sample.txt") -> List[Tuple[str, int]]:

    with open(filepath, "r") as f:
        data = f.readlines()

    return [(l.split(" ")[0], int(l.split(" ")[1])) for l in data]
