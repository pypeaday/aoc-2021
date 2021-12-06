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


def update_marks(marks, boards, drawn):
    def __mark_elements_on_board(
        drawn: int, board: List[List[int]], board_marks: List[List[int]]
    ):
        """track the marked elements on board recurisvely

        Args:
            draw_values (int): drawn value from data
            board (List[List[int]]): one board
            board_marks (List[List[int]]): marks for that one board


        """

        for i, row in enumerate(board):
            idx = find_all_idx(row, drawn)
            for _id in idx:
                board_marks[i][_id] = 1

        return board_marks

    for j, board in enumerate(boards):
        marks[j] = __mark_elements_on_board(drawn, board, marks[j])
    return marks


def play_bingo(
    draw_values: List[int], boards: List[List[List[int]]]
) -> Tuple[int, int]:

    # initialize zero-arrays like each board
    marks = [like_zeros(board) for board in boards]

    for i, drawn in enumerate(draw_values):
        # Note recurrsion side-effect by design
        marks = update_marks(marks, boards, drawn)
        print(marks)
        breakpoint()

        # Check for winner
        for j, board_marks in enumerate(marks):
            if is_winner(board_marks):
                return (drawn, j)
        print(i, drawn)

    print("No Winner")


if __name__ == "__main__":
    draw_values, boards = get_data()

    print(f"Day 4 solution 1 is {play_bingo(draw_values, boards)}")
