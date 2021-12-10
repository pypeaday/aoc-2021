"""day 9 tests"""

from src.day9 import get_data, find_low_points, pad_data


def test_pad_data():

    expected = [
        [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
        [9, 2, 1, 9, 9, 9, 4, 3, 2, 1, 0, 9],
        [9, 3, 9, 8, 7, 8, 9, 4, 9, 2, 1, 9],
        [9, 9, 8, 5, 6, 7, 8, 9, 8, 9, 2, 9],
        [9, 8, 7, 6, 7, 8, 9, 6, 7, 8, 9, 9],
        [9, 9, 8, 9, 9, 9, 6, 5, 6, 7, 8, 9],
        [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    ]
    data = get_data()
    padded_data = pad_data(data)
    assert expected == padded_data


def test_find_low_points():

    data = get_data()
    expected = [(0, 1), (0, 9), (2, 2), (4, 6)]
    indices, values = find_low_points(data)

    for t in indices:
        assert t in expected

    for t in expected:
        assert t in indices

    assert set(values) == set([1, 0, 5, 5])
    assert values == [1, 0, 5, 5]


def test_get_data():
    data = get_data()
    expected = [
        [2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
        [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
        [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
        [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
        [9, 8, 9, 9, 9, 6, 5, 6, 7, 8],
    ]
    assert data == expected
