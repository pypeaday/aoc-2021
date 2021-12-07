"""test day 7"""

from src.day7 import get_data, find_min


def test_find_min():

    data = get_data()
    expected_fuel = 37
    expected_pos = 2
    pos, fuel = find_min(data)
    assert expected_fuel == fuel
    assert expected_pos == pos


def test_get_data():
    expected = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
    data = get_data("./data/day7_sample.txt")

    assert expected == data
