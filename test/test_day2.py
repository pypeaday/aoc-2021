from src.day2 import get_data, calculate_position, calculate_position_with_aim, get_aims


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


def test__calculate_position():
    data = get_data()

    assert calculate_position(data, "horizontal") == 15
    assert calculate_position(data, "depth") == 10


def test_get_aims():
    data = get_data()
    expected = [0, 5, 5, 2, 10, 10]
    aims = get_aims(data)
    assert aims == expected


def test__calculate_position_with_aim():
    data = get_data()

    assert calculate_position_with_aim(data, "horizontal") == 15
    assert calculate_position_with_aim(data, "depth") == 60
