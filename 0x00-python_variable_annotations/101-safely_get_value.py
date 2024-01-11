#!/usr/bin/env python3
from typing import List, TypeVar, Mapping, Any, Union
T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[T, None]) -> Union[Any, T]:
    """ More involved type annotations

    Keyword arguments:
    dct (mapping): mapping input
    key (any): any tpe
    default (union[T,none]): default parameter
    Return:  values, add type annotations to the function
    """
    if key in dct:
        return dct[key]
    else:
        return default
