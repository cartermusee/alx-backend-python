#!/usr/bin/env python3
"""Complex types - functions"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """callable

    Keyword arguments:
    multiplier (float): multiplier input
    Returns: a callable func
    """
    def multiplier_funct(x: float) -> float:
        return x * multiplier
    return multiplier_funct
