"""test day 7"""

from src.day7 import get_data


def test_get_data():
    expected = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
    data = get_data("./data/day7_sample.txt")

    assert expected == data
