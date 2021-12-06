"""day 4 module"""
from typing import List, Tuple, Any, Dict


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
    my_list = [x for x in ls]

    def __like_zeros(ls: List) -> List:
        for i, v in enumerate(ls):
            if isinstance(v, int):
                ls[i] = 0
            else:
                ls[i] = like_zeros(v)

        return ls

    return __like_zeros(my_list)


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


def take_one_turn_on_one_board(drawn: int, board: List[List[int]]) -> List[List[int]]:
    mark = like_zeros(board)
    for i, row in enumerate(board):
        idx = find_all_idx(row, drawn)
        for _id in idx:
            mark[i][_id] = 1
    return mark


def combine_mark_from_one_board(
    old_mark: List[List[int]], new_mark: List[List[int]]
) -> List[List[int]]:

    mark = like_zeros(old_mark)
    for i, old_row in enumerate(old_mark):
        mark[i] = [sum([v, new_mark[i][j]]) for j, v in enumerate(old_row)]
    return mark


def combine_marks(
    old_marks: List[List[List[int]]], new_marks: List[List[List[int]]]
) -> List[List[List[int]]]:
    return [
        combine_mark_from_one_board(old_mark, new_mark)
        for old_mark, new_mark in zip(old_marks, new_marks)
    ]


def play_bingo(
    draw_values: List[int], boards: List[List[List[int]]]
) -> Tuple[int, int, int, Dict[int, List]]:
    """play_bingo.

    Args:
        draw_values (List[int]): draw_values
        boards (List[List[List[int]]]): boards

    Returns:
        Tuple[int, int, int, Dict[int, List]]:  number of turns till winner,value from drawn values that caused the win and index of the winning board, the state dictionary of marks
    """

    # initialize zero-arrays like each board
    state_dict = {-1: [like_zeros(board) for board in boards]}

    for i, drawn in enumerate(draw_values):
        new_marks = [take_one_turn_on_one_board(drawn, board) for board in boards]
        state_dict[i] = combine_marks(state_dict[i - 1], new_marks)

        # Check for winner
        if i < 5:
            # 5x5 board requires at least 5 turns
            continue
        for j, board_marks in enumerate(state_dict[i]):
            if is_winner(board_marks):
                return (i, drawn, j, state_dict)

    raise Exception("No Winner")


def get_unmarked_numbers(marks: List[List[int]], board: List[List[int]]) -> List[int]:
    values = []

    for i, row in enumerate(marks):
        values.extend([v for j, v in enumerate(board[i]) if not row[j]])
    return values


if __name__ == "__main__":
    draw_values, boards = get_data("./data/day4.txt")

    idx, val, board_id, state_dict = play_bingo(draw_values, boards)
    winning_board = boards[board_id]
    unmarked = get_unmarked_numbers(state_dict[idx][board_id], winning_board)
    print(f"Day 4 solution 1 is {sum(unmarked) * val}")
