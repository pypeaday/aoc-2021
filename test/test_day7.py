"""test day 7"""

from src.day7 import get_data, find_min, partial_sum, find_harder_min


def test_find_harder_min():
    data = get_data()
    expected_fuel = 168
    expected_pos = 5

    pos, fuel = find_harder_min(data)

    assert expected_fuel == fuel
    assert expected_pos == pos


def test_partial_sum():
    n = 16 - 5
    expected = 66
    my_sum = partial_sum(n)
    assert my_sum == expected
    n = 5 - 1
    expected = 10
    my_sum = partial_sum(n)
    assert my_sum == expected


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
