#!/usr/bin/env python3

def no_c(my_string):
    """
    Returns a copy of my_str without c or C
    Args:
        my_str - the string to filter
    """

    new_str = ""
    for i in my_string:
        if i != 'c' and i != 'C':
            new_str += i
    return (new_str)
