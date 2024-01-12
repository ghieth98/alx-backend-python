#!/usr/bin/python3

"""
Annotate element_length function which takes lst as an argument to return values with appropriate types
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    :param lst:
    :return:
    """
    return [(i, len(i)) for i in lst]
