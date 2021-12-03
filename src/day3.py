"""day 3"""

from typing import List, Callable


def get_data(filepath: str = "./data/day3_sample.txt") -> List[str]:
    """get_data.

    format binary input into a list of strings

    Args:
        filepath (str): filepath

    Returns:
        List[str]:
    """

    with open(filepath, "r") as f:
        data = f.readlines()
    return [x.replace("\n", "") for x in data]


def _get_bit_of_interest_by_column_index(
    data: List[str], idx: int, func: Callable
) -> str:
    """_get_bit_of_interest_by_column_index.

    count number of occurences of each bit along a dimension of the input data
    and return the most common or least common depending on func

    Args:
        data (List[str]): data
        idx (int): idx
        func (Callable): one of min or max

    Returns:
        str: one of '0' or '1'
    """

    bits = [x[idx] for x in data]

    return str(func(set(bits), key=bits.count))


def get_gamma_rate(data: List[str]) -> str:
    """get_gamma_rate.

    Args:
        data (List[str]): data

    Returns:
        str:
    """

    bit_length = len(data[0])
    bits = [
        _get_bit_of_interest_by_column_index(data, idx, max)
        for idx in range(bit_length)
    ]
    return "".join(bits)


def get_delta_rate(data: List[str]) -> str:
    """get_delta_rate.

    Args:
        data (List[str]): data

    Returns:
        str:
    """

    bit_length = len(data[0])
    bits = [
        _get_bit_of_interest_by_column_index(data, idx, min)
        for idx in range(bit_length)
    ]
    return "".join(bits)


def get_power_consumption(gamma_rate: str, delta_rate: str):
    """get_power_consumption.

    convert binary rates to int and return product

    Args:
        gamma_rate (str): gamma_rate
        delta_rate (str): delta_rate
    """

    return int(gamma_rate, 2) * int(delta_rate, 2)


if __name__ == "__main__":
    data = get_data("./data/day3.txt")
    print(
        f"Day 3 solution 1 is {get_power_consumption(get_gamma_rate(data), get_delta_rate(data))}"
    )
