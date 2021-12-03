"""day 2 module"""
from typing import List, Tuple


_MAP = {
    "horizontal": {
        "forward": 1,
    },
    "depth": {"up": -1, "down": 1},
}


def get_data(filepath: str = "./data/day2_sample.txt") -> List[Tuple[str, int]]:
    """get_data.

    Args:
        filepath (str): filepath

    Returns:
        List[Tuple[str, int]]:
    """

    with open(filepath, "r") as f:
        data = f.readlines()

    return [(sub.split(" ")[0], int(sub.split(" ")[1])) for sub in data]


def calculate_position(data: List[Tuple[str, int]], dim: str = "horizontal") -> int:

    _map = _MAP[dim]
    res = sum([sub[1] * _map.get(sub[0], 0) for sub in data])

    return res
