#!/usr/bin/python3

"""
Given the parameters and the return values, add type annotations to the function
"""
from typing import Any, Mapping, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default=Union[T, Any]) -> Union[Any, T]:
    """
    :param dct:
    :param key:
    :param default:
    :return:
    """
    if key in dct:
        return dct[key]
    else:
        return default
