#!/usr/bin/env python3
"""module for string and int/float to tuple"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ tuple with string and float

    Keyword arguments:
    k (str): string
    v (union[int, float]): int or float
    Returns: return a tiple with str and squre of v in float
    """

    return (k, float(v) ** 2)
