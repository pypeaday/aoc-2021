"""test day 3"""

from src.day3 import (
    get_data,
    _get_bit_of_interest_by_column_index,
    get_gamma_rate,
    get_delta_rate,
    get_power_consumption,
)

import pytest


def my_data():
    return [
        "00100",
        "11110",
        "10110",
        "10111",
        "10101",
        "01111",
        "00111",
        "11100",
        "10000",
        "11001",
        "00010",
        "01010",
    ]


def test_get_data():

    data = get_data("./data/day3_sample.txt")

    for v, u in zip(my_data(), data):
        assert v == u


@pytest.mark.parametrize(
    "test_input, idx, expected",
    [
        (my_data, 0, "1"),
        (my_data, 1, "0"),
        (my_data, 2, "1"),
        (my_data, 3, "1"),
        (my_data, 4, "0"),
    ],
)
def test__get_bit_of_interest_by_column_index(test_input, idx, expected):
    data = test_input()
    assert _get_bit_of_interest_by_column_index(data, idx, max) == expected


def test_get_gamma_rate():
    data = my_data()
    gamma_rate = "10110"

    assert get_gamma_rate(data) == gamma_rate


def test_get_delta_rate():
    data = my_data()
    delta_rate = "01001"
    assert get_delta_rate(data) == delta_rate


def test_get_power_consumption():
    gamma_rate = "10110"
    delta_rate = "01001"
    assert get_power_consumption(gamma_rate, delta_rate) == 198
