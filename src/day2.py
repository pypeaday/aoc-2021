"""day 2 module"""
from typing import List, Tuple


_MAP = {
    "horizontal": {
        "forward": 1,
    },
    "depth": {"up": -1, "down": 1},
    "aim": {"down": 1, "up": -1},
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
    """calculate_position.

    Using MAP and dim or "horizontal" or "depth" calculate the final position along "dim" of the sub

    Args:
        data (List[Tuple[str, int]]): data
        dim (str): one of "horizontal" or "depth"

    Returns:
        int:
    """

    _map = _MAP[dim]
    res = sum([sub[1] * _map.get(sub[0], 0) for sub in data])

    return res


def get_aims(data: List[Tuple[str, int]]) -> List[int]:
    """get_aims.
    Return a list of index-specific aim values
    Args:
        data (List[Tuple[str, int]]): data

    Returns:
        List[int]:
    """
    _map = _MAP["aim"]
    aims: List = []
    for i, sub in enumerate(data):
        try:
            aims.append(_map.get(sub[0], 0) * sub[1] + aims[i - 1])
        except IndexError:
            aims.append(0)
    return aims


def calculate_position_with_aim(
    data: List[Tuple[str, int]], dim: str = "horizontal"
) -> int:
    """calculate_position_with_aim.

    Args:
        data (List[Tuple[str, int]]): data
        dim (str): one of "horizontal" or "depth"

    Returns:
        int:
    """
    aims = get_aims(data)
    _map = _MAP["horizontal"]

    if dim == "horizontal":
        return calculate_position(data, dim)
    else:
        return sum([aim * sub[1] * _map.get(sub[0], 0) for aim, sub in zip(aims, data)])


if __name__ == "__main__":
    data = get_data("./data/day2.txt")
    print(
        f"day 2 solution 1: {calculate_position(data, 'horizontal') * calculate_position(data, 'depth')}"
    )

    print(
        f"day 2 solution 2: {calculate_position_with_aim(data, 'horizontal') * calculate_position_with_aim(data, 'depth')}"
    )
