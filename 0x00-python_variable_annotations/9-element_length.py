#!/usr/bin/env python3
"""module for duck type"""
from typing import List, Iterable, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """duck type an iterable object

    Keyword arguments:
    lst (iterable[sequence]): list input
    Returns: a list values with the appropriate types
    """
    return [(i, len(i)) for i in lst]
