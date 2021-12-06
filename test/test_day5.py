"""test day 5"""
from src.day5 import (
    get_data,
    initialize_board,
    get_points_of_1d_line,
    get_points_of_all_1d_lines,
)


def test_get_points_of_all_1d_lines():
    data = get_data("./data/day5_sample.txt")
    lines = get_points_of_all_1d_lines(data)
    expected = [
        ([0, 1, 2, 3, 4, 5], [9]),
        ([3, 4, 5, 6, 7, 8, 9], [4]),
        ([2], [1, 2]),
        ([7], [0, 1, 2, 3, 4]),
        ([0, 1, 2], [9]),
        ([1, 2, 3], [4]),
    ]
    assert lines == expected


def test_get_points_of_1d_line():
    p1 = (0, 0)
    p2 = (0, 4)
    horizontal, vertical = get_points_of_1d_line(p1, p2)

    expected_horizontal = [0]
    expected_vertical = [0, 1, 2, 3, 4]
    assert expected_horizontal == horizontal
    assert expected_vertical == vertical

    p1 = (9, 7)
    p2 = (7, 7)
    horizontal, vertical = get_points_of_1d_line(p1, p2)

    expected_horizontal = [7, 8, 9]
    expected_vertical = [7]
    assert expected_horizontal == horizontal
    assert expected_vertical == vertical


def test_initialize_board():
    expected = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    data = get_data("./data/day5_sample.txt")
    board = initialize_board(data)
    assert board == expected


def test_get_data():
    data = get_data("./data/day5_sample.txt")
    expected = [
        ((0, 9), (5, 9)),
        ((8, 0), (0, 8)),
        ((9, 4), (3, 4)),
        ((2, 2), (2, 1)),
        ((7, 0), (7, 4)),
        ((6, 4), (2, 0)),
        ((0, 9), (2, 9)),
        ((3, 4), (1, 4)),
        ((0, 0), (8, 8)),
        ((5, 5), (8, 2)),
    ]
    assert data == expected
