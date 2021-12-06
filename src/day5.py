"""day 5"""
from typing import List, Tuple, Optional


def get_data(
    filepath: str = "./data/day5_sample.txt",
) -> List[Tuple[Tuple[int, int], Tuple[int, int]]]:
    """get_data.

    Args:
        filepath (str): filepath

    Returns:
        List[Tuple[Tuple[int],Tuple[int]]]:
            ex. [((0, 9), (5, 9)),
                 ((9, 4), (3, 4)),
                 ((8, 0), (0, 8)),
                 ((2, 2), (2, 1)),
                 ((7, 0), (7, 4)),
                 ((6, 4), (2, 0)),
                 ((0, 9), (2, 9)),
                 ((3, 4), (1, 4)),
                 ((0, 0), (8, 8)),
                 ((5, 5), (8, 2))]
    """

    data: List = []
    with open(filepath, "r") as f:
        for line in f.readlines():
            p1, p2 = line.split(" -> ")
            x1, y1 = p1.split(",")
            x2, y2 = p2.split(",")
            data.append(((int(x1), int(y1)), (int(x2), int(y2))))
    return data


def get_points_of_1d_line(
    p1: Tuple[int, int], p2: Tuple[int, int]
) -> Tuple[List[int], List[int]]:
    """get_points_of_1d_line.

    Args:
        p1 (Tuple[int]): p1 like (0,9)
        p2 (Tuple[int]): p2 like (2,8)

    Returns:
        Tuple[List[int], List[int]]: horizontal index array and vertial index array
    """

    if p1[0] == p2[0] or p1[1] == p2[1]:
        x1 = min(p1[0], p2[0])
        x2 = max(p1[0], p2[0])

        y1 = min(p1[1], p2[1])
        y2 = max(p1[1], p2[1])
        horizontal_points = [x for x in range(x1, x2 + 1)]
        vertial_points = [y for y in range(y1, y2 + 1)]
    else:
        return [], []

    return horizontal_points, vertial_points


def get_points_of_all_1d_lines(
    data: List[Tuple[Tuple[int, int], Tuple[int, int]]]
) -> List[Tuple[List[int], List[int]]]:

    lines = [get_points_of_1d_line(points[0], points[1]) for points in data]

    return [ls for ls in lines if ls[0]]


def mark_board_with_1d_lines(
    lines: List[Tuple[List[int], List[int]]], board: List[List[int]]
) -> List[List[int]]:
    for line in lines:
        if len(line[0]) == 1:  # vertical line
            column_id = line[0][0]
            row_ids = line[1]
            for row_id in row_ids:
                board[row_id][column_id] += 1

        elif len(line[1]) == 1:  # horizontal line
            row_id = line[1][0]
            column_ids = line[0]
            row = board[row_id]
            for column_id in column_ids:
                row[column_id] += 1

    return board


def get_points_of_2d_line(
    p1: Tuple[int, int], p2: Tuple[int, int]
) -> Optional[List[Tuple[int, int]]]:
    """get_points_of_2d_line.

    Args:
        p1 (Tuple[int]): p1 like (0,9)
        p2 (Tuple[int]): p2 like (2,8)

    Returns:
        List[Tuple[int, int]]: indices of diagonal line
    """
    if p1[0] == p2[0] or p1[1] == p2[1]:
        # handled in 1d lines
        return None
    if abs(p1[0] - p2[0]) == abs(p1[1] - p2[1]):
        y1 = p1[0]
        y2 = p2[0]
        x1 = p1[1]
        x2 = p2[1]

        if x1 < x2 and y1 < y2:  # 45 down right
            diagonal_points = [
                (i, j)
                for i, j in zip(
                    [x for x in range(x1, x2 + 1)], [y for y in range(y1, y2 + 1)]
                )
            ]
        elif x1 < x2 and y1 > y2:  # 45 down left
            diagonal_points = [
                (i, j)
                for i, j in zip(
                    [x for x in range(x1, x2 + 1)], [y for y in range(y1, y2 - 1, -1)]
                )
            ]
        elif x1 > x2 and y1 > y2:  # 45 up right
            diagonal_points = [
                (i, j)
                for i, j in zip(
                    [x for x in range(x1, x2 - 1, -1)],
                    [y for y in range(y1, y2 - 1, -1)],
                )
            ]
        else:  # 45 up left
            diagonal_points = [
                (i, j)
                for i, j in zip(
                    [x for x in range(x1, x2 - 1, -1)],
                    [y for y in range(y1, y2 + 1)],
                )
            ]
        return diagonal_points
    else:
        return None


def get_points_of_all_2d_lines(
    data: List[Tuple[Tuple[int, int], Tuple[int, int]]]
) -> List[List[Tuple[int, int]]]:

    lines = [get_points_of_2d_line(points[0], points[1]) for points in data]

    return [ls for ls in lines if ls]


def mark_board_with_2d_lines(
    lines: List[List[Tuple[int, int]]], board: List[List[int]]
) -> List[List[int]]:
    for line in lines:
        for point in line:
            rid = point[0]
            cid = point[1]
            board[rid][cid] += 1

    return board


def find_max(data: List) -> int:
    maxes = []
    for points in data:
        maxes.append(max(max(points[0]), max(points[1])))
    return max(maxes) + 1


def initialize_board(data: List) -> List[List[int]]:

    width = find_max(data)
    height = width
    board = [[0 for _ in range(width)] for _ in range(height)]
    return board


def count_overlaps(board: List[List[int]]) -> int:
    counter = 0
    for row in board:
        _max = max(row) + 1
        for i in range(2, _max):
            counter += row.count(i)
    return counter


if __name__ == "__main__":

    data = get_data("./data/day5.txt")
    # data = get_data()
    lines_1d = get_points_of_all_1d_lines(data)
    board = initialize_board(data)
    board = mark_board_with_1d_lines(lines_1d, board)
    count = count_overlaps(board)

    print(f"Day 5 solution 1 is {count}")

    lines_2d = get_points_of_all_2d_lines(data)
    board2 = initialize_board(data)
    board2 = mark_board_with_1d_lines(lines_1d, board2)
    board2 = mark_board_with_2d_lines(lines_2d, board2)
    count = count_overlaps(board2)

    print(f"Day 5 solution 2 is {count}")
