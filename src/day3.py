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

    if bits.count("0") == bits.count("1"):
        return str(func([0, 1]))

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


def _convert_and_multiply(v: str, u: str) -> int:
    """_convert_and_multiply.

    convert binary values to integer and multiply

    Args:
        v (str): v
        u (str): u

    Returns:
        int:
    """

    return int(v, 2) * int(u, 2)


def get_power_consumption(data: List[str]) -> int:
    """get_power_consumption.

    convert binary rates to int and return product

    Args:
        data (List[str]): data

    Returns:

        int

    """
    gamma_rate = get_gamma_rate(data)
    delta_rate = get_delta_rate(data)

    return _convert_and_multiply(gamma_rate, delta_rate)


def _get_life_support_values(data: List[str], criteria: str) -> str:
    """_get_life_support_values.

    Args:
        data (List[str]): data
        criteria (str): criteria one of "o2" or "co2"

    Returns:
        str:
    """

    if criteria.lower() == "o2":
        func = max
    elif criteria.lower() == "co2":
        func = min

    values = [x for x in data]
    bit_length = len(data[0])
    for idx in range(bit_length):
        bit = _get_bit_of_interest_by_column_index(values, idx, func)
        values = [x for x in values if x[idx] == bit]

        if len(values) == 1:
            break

    return values[0]


def get_o2_generator_rating(data: List[str]) -> str:
    """get_o2_generator_rating.

    Args:
        data (List[str]): data

    Returns:
        str:
    """
    return _get_life_support_values(data, "o2")


def get_co2_generator_rating(data: List[str]) -> str:
    """get_co2_generator_rating.

    Args:
        data (List[str]): data

    Returns:
        str:
    """
    return _get_life_support_values(data, "co2")


def get_life_support_rating(data: List[str]) -> int:
    """get_life_support_rating.

    Args:
        data (List[str]): data

    Returns:
        int:
    """
    o2 = get_o2_generator_rating(data)
    co2 = get_co2_generator_rating(data)
    return _convert_and_multiply(o2, co2)


if __name__ == "__main__":
    data = get_data("./data/day3.txt")
    print(f"Day 3 solution 1 is {get_power_consumption(data)}")
    print(f"Day 3 solution 2 is {get_life_support_rating(data)}")
