#!/usr/bin/env python3
"""py module for sum of list elemnts"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """adding list items

    Keyword arguments:
    input_list (list): a list of items
    Returns: the sum
    """
    sum: float = 0
    for i in input_list:
        sum += i

    return sum
