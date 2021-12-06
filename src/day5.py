"""day 5"""
from typing import List, Tuple


def get_data(filepath: str = "./data/day5_sample.txt") -> List[List[Tuple[int]]]:
    """get_data.

    Args:
        filepath (str): filepath

    Returns:
        List[List[Tuple[int]]]:
            ex. [[(0, 9), (5, 9)],
                 [(9, 4), (3, 4)],
                 [(8, 0), (0, 8)],
                 [(2, 2), (2, 1)],
                 [(7, 0), (7, 4)],
                 [(6, 4), (2, 0)],
                 [(0, 9), (2, 9)],
                 [(3, 4), (1, 4)],
                 [(0, 0), (8, 8)],
                 [(5, 5), (8, 2)]]
    """

    data: List = []
    with open(filepath, "r") as f:
        for line in f.readlines():
            p1, p2 = line.split(" -> ")
            x1, y1 = p1.split(",")
            x2, y2 = p2.split(",")
            data.append([(int(x1), int(y1)), (int(x2), int(y2))])
    return data


def get_points_of_line(p1: Tuple[int], p2: Tuple[int]) -> Tuple[List[int], List[int]]:
    """get_points_of_line.

    Args:
        p1 (Tuple[int]): p1 like (0,9)
        p2 (Tuple[int]): p2 like (2,8)

    Returns:
        Tuple[List[int], List[int]]: horizontal index array and vertial index array
    """

    horizontal_points = [x for x in range(p1[0], p2[0])]
    vertial_points = [y for y in range(p1[1], p2[1])]
    return horizontal_points, vertial_points


def initialize_board(data: List):

    width = 9
    height = len(data)
    board = [[0 for _ in range(width)] for _ in range(height)]
    return board
