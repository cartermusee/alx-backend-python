#!/usr/bin/env python3
"""module for typevar"""
from typing import List, TypeVar, Mapping, Any, Union
T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[T, None]) -> Union[Any, T]:
    """ More involved type annotations

    Keyword arguments:
    dct (Mapping): mapping input
    key (Any): any tpe
    default (Union[T,none]): default parameter
    Returns:values, add type annotations to the function
    """
    if key in dct:
        return dct[key]
    else:
        return default
