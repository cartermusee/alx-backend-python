#!/usr/bin/env python3
from typing import List, Iterable, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """duck type an iterable object

    Keyword arguments:
    lst (iterable): list input
    Returns: values with the appropriate types
    """
    return [(i, len(i)) for i in lst]
