#!/usr/bin/env python3
"""
function sum_mixed_list which takes
 a list mxd_lst of integers and
 floats and returns their sum as a float.
"""
from typing import Union


def sum_mixed_list(mxd_lst: list[Union[int, float]]) -> float:
    """
    This function takes a list mxd_lst
     of integers and floats and
      returns their sum as a float
    :param mxd_lst:
    :return: float
    """
    return sum(mxd_lst)
