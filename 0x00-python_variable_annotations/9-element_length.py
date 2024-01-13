#!/usr/bin/env python3
"""This module defines a function element_length"""
from typing import Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Takes a list 'lst' as input and returns a new list of tuples.

    Args:
        lst (list): The input list containing elements of any data type.

    Returns:
        list: A list of tuples, where each tuple contains an item from the
        input list and its length.
    """
    return [(idx, len(idx)) for idx in lst]
