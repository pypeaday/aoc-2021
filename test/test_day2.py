from src.day2 import get_data


def test_get_data():
    expected = [
        ("forward", 5),
        ("down", 5),
        ("forward", 8),
        ("up", 3),
        ("down", 8),
        ("forward", 2),
    ]

    data = get_data()

    for e_tup, t_tup in zip(expected, data):
        assert e_tup == t_tup
