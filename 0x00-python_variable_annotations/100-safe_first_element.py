#!/usr/bin/env python3
"""module for ducks"""
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Duck typing - first element of a sequence
    Keyword arguments:
    lst (sequence): a sequence
    Return: a list or none
    """
    if lst:
        return lst[0]
    else:
        return None
