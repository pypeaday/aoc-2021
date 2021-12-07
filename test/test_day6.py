""" test day 6 """
from src.day6 import get_data, one_day_passes


def test_one_day_passes():

    data = get_data("./data/day6_sample.txt")
    old_data = [x for x in data]
    for i in range(18):
        new_data = one_day_passes(old_data)
        old_data = new_data
    assert len(new_data) == 26

    old_data = [x for x in data]
    for i in range(80):
        new_data = one_day_passes(old_data)
        old_data = new_data
    assert len(new_data) == 5934
