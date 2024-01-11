#!/usr/bin/env python3
"""module for tpe checking"""
from typing import Tuple, Any, Union, List


def zoom_array(lst: Tuple,
               factor: int = 2) -> List:
    """Type Checking
    Keyword arguments:
    lst (tuple): a tuple input
    factor (int): a int input
    Return: a tuple
    """
    zoomed_in: Tuple[Any, ...] = tuple(
        item for item in lst
        for i in range(int(factor))
    )
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)
