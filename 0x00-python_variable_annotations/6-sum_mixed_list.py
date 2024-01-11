#!/usr/bin/env python3
"""module for mixed items in list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """function do sum for all ints and floats

    Keyword arguments:
    mxd_lstt: list input with both int and floats
    Returns: the sum
    """
    sum: float = 0
    for num in mxd_lst:
        sum += num
    return sum
