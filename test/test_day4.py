from src.day4 import (
    get_data,
    find_all_idx,
    like_zeros,
    is_winner,
    play_bingo,
    update_marks,
)


def test_update_marks():
    drawn_values, boards = get_data()

    expected = [
        [
            [0, 0, 0, 1, 0],
            [0, 0, 0, 1, 0],
            [0, 1, 0, 0, 1],
            [0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0],
        ],
        [
            [0, 0, 0, 0, 0],
            [1, 0, 0, 0, 1],
            [0, 0, 1, 0, 0],
            [0, 1, 0, 0, 1],
            [0, 0, 0, 0, 0],
        ],
        [
            [0, 0, 0, 0, 1],
            [0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1],
            [0, 0, 0, 0, 1],
        ],
    ]

    test_draw = drawn_values[0]

    marks = like_zeros(expected)

    marks = update_marks(marks, boards, test_draw)

    for i, _board in enumerate(expected):
        for j, _row in enumerate(_board):
            assert marks[i][j] == _row


def test_get_data():
    expected_boards = [
        [
            [22, 13, 17, 11, 0],
            [8, 2, 23, 4, 24],
            [21, 9, 14, 16, 7],
            [6, 10, 3, 18, 5],
            [1, 12, 20, 15, 19],
        ],
        [
            [3, 15, 0, 2, 22],
            [9, 18, 13, 17, 5],
            [19, 8, 7, 25, 23],
            [20, 11, 10, 24, 4],
            [14, 21, 16, 12, 6],
        ],
        [
            [14, 21, 17, 24, 4],
            [10, 16, 15, 9, 19],
            [18, 8, 23, 26, 20],
            [22, 11, 13, 6, 5],
            [2, 0, 12, 3, 7],
        ],
    ]

    expected_drawn = [
        7,
        4,
        9,
        5,
        11,
        17,
        23,
        2,
        0,
        14,
        21,
        24,
        10,
        16,
        13,
        6,
        15,
        25,
        12,
        22,
        18,
        20,
        8,
        19,
        3,
        26,
        1,
    ]

    drawn, boards = get_data()
    assert expected_boards == boards
    assert expected_drawn == drawn


def test_find_all_idx():

    expected = [0, 1, 2, 4]
    data = [1, 1, 1, 2, 1]
    assert find_all_idx(data, 1) == expected


def test_like_zeros():
    expected = [[0, 0], [0, 0, 0]]
    data = [[1, 1], [2, 2, 2]]

    assert like_zeros(data) == expected


def test_is_winner():
    data = [[1, 1, 1], [1, 0, 0], [0, 0, 0]]
    assert is_winner(data) is True
    data = [[1, 0, 1], [1, 0, 0], [1, 0, 0]]
    assert is_winner(data) is True


def test_play_bingo():
    draw_values, boards = get_data()

    drawn = 24
    board_idx = 2

    res = play_bingo(draw_values, boards)

    # assert res[0] == drawn
    assert res[1] == board_idx
