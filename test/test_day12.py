"""test day 12"""
from src.day12 import is_connected_simple, get_data


def test_is_connected_simple():
    data, caves, edges, cave_list = get_data()
    assert is_connected_simple(cave_list, "start", "A") is True
    assert is_connected_simple(cave_list, "start", "end") is False
