"""day 7"""
from typing import List, Tuple


def get_data(filepath: str = "./data/day7_sample.txt") -> List[int]:

    with open(filepath, "r") as f:
        data = f.readline()
    return [int(x) for x in data.split(",")]


def find_min(data) -> Tuple[int, int]:
    """find_min.

    find the value in data such that the sum of distances from all points to a given
    point is minimized

    Args:
        data:

    Returns:
        min_position
        min_fuel
    """
    min_position = -1
    min_fuel = sum([abs(data[0] - j) for j in data if data[0] != j])

    for i in data[1:]:
        fuel = sum([abs(i - j) for j in data if i != j])
        if fuel < min_fuel:
            min_fuel = fuel
            min_position = i

    return min_position, min_fuel


def partial_sum(n: int) -> int:
    """partial_sum.

    calculate sum 1 to n

    Args:
        n (int): n

    Returns:
        int:
    """

    return (n * (n + 1)) // 2


def find_harder_min(data: List[int]) -> Tuple[int, int]:
    min_position = -1
    min_fuel = sum([partial_sum(abs(0 - j)) for j in data if 0 != j])

    for i in range(max(data)):
        fuel = sum([partial_sum(abs(i - j)) for j in data if i != j])
        if fuel < min_fuel:
            min_fuel = fuel
            min_position = i

    return min_position, min_fuel


if __name__ == "__main__":
    data = get_data("./data/day7.txt")
    pos, fuel = find_min(data)
    print(f"Day 7 part 1 -- position: {pos}, fuel: {fuel}")
    pos, fuel = find_harder_min(data)
    print(f"Day 7 part 2 -- position: {pos}, fuel: {fuel}")
