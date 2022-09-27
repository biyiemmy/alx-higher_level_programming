#!/usr/bin/env python3

def no_c(my_string):
    """
    Returns a copy of my_string without c or C
    Args:
        my_string - the string to filter
    """
    return "".join(filter(lambda x: x not in 'cC', my_string))
