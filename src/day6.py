"""day 6"""
from typing import List


def get_data(filepath: str = "./data/day6_sample.txt") -> List[int]:
    with open(filepath, "r") as f:
        data = f.readlines()
    return [int(x) for x in data[0].split(",")]


def one_day_passes(arr: List[int]) -> List[int]:

    new_arr = [x - 1 for x in arr]
    num_new = new_arr.count(-1)
    # There must be a clever way to do this with modulo
    new_arr = [x if x >= 0 else 6 for x in new_arr]
    new_arr.extend([8 for _ in range(num_new)])
    return new_arr


if __name__ == "__main__":
    data = get_data("./data/day6.txt")
    old_data = [x for x in data]
    for i in range(80):
        new_data = one_day_passes(old_data)
        old_data = new_data
    print(f"Day 6 solution 1: {len(new_data)}")
