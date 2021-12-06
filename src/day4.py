"""day 4 module"""
from typing import List, Tuple, Any


def get_data(
    filepath: str = "./data/day4_sample.txt",
) -> Tuple[List[int], List[List[List[int]]]]:

    with open(filepath, "r") as f:
        data = f.readlines()

    draw_values = [int(x) for x in data[0].split(",")]

    raw_boards = data[1:]

    num_cols = 5
    num_rows = 6  # 5 + 1 for \n
    # digit width assumed two + /n
    digit_width = 3
    # board width assumed 15 = 5*digit width + 4 spaces + \n
    # board_width = num_cols * digit_width

    boards = []
    for i in range(len(raw_boards) // num_rows):  # number of boards
        raw_board = raw_boards[1 + i * num_rows : (i + 1) * num_rows]
        board = []
        for raw_row in raw_board:
            row = [
                int(raw_row[j * digit_width : (j + 1) * digit_width])
                for j in range(num_cols)
            ]
            board.append(row)
        boards.append(board)

    return draw_values, boards


def find_all_idx(ls: List, val: Any) -> List:
    """Find all indices of a given value in a list"""
    return [i for i, x in enumerate(ls) if x == val]


def like_zeros(ls: List) -> List:
    """Recursively copy a nested iterable and return zeros"""

    for i, v in enumerate(ls):
        if isinstance(v, int):
            ls[i] = 0
        else:
            ls[i] = like_zeros(v)

    return ls


def is_winner(board_marks: List[List[int]]) -> bool:
    """Check for a complete row or column"""

    # check for complete row
    for row in board_marks:
        if sum(row) == len(row):
            return True

    # check for complete column
    for _id in range(len(row)):
        if sum([row[_id] for row in board_marks]) == len(row):
            return True
    return False


def mark_elements_on_board(boards, drawn):
    """mark_elements_on_board.
    returns index of bingo matches for a paricular turn

    Args:
        boards:
        drawn:
    """

    marks = [like_zeros(board) for board in boards]

    for board in boards:
        for i, row in enumerate(board):
            idx = find_all_idx(row, drawn)
            for _id in idx:
                marks[i][_id] = 1

    return marks


def combine_marks(
    old_marks: List[List[List[int]]], new_marks: List[List[List[int]]]
) -> List[List[List[int]]]:
    marks = []
    for prev_b1, new_b1 in zip(old_marks, new_marks):
        marks.append(
            [
                [sum(items) for items in zip(*zipped_list)]
                for zipped_list in zip(old_marks, new_marks)
            ]
        )

    return marks


def play_bingo(
    draw_values: List[int], boards: List[List[List[int]]]
) -> Tuple[int, int]:

    # initialize zero-arrays like each board
    state_dict = {-1: [like_zeros(board) for board in boards]}

    for i, drawn in enumerate(draw_values):
        new_marks = mark_elements_on_board(boards, drawn)
        state_dict[i] = combine_marks(state_dict[i - 1], new_marks)

        print(marks)
        breakpoint()

        # Check for winner
        if i < 5:
            # 5x5 board requires at least 5 turns
            continue
        for j, board_marks in enumerate(marks):
            if is_winner(board_marks):
                return (drawn, j)
        print(i, drawn)

    print("No Winner")


if __name__ == "__main__":
    draw_values, boards = get_data()

    print(f"Day 4 solution 1 is {play_bingo(draw_values, boards)}")
