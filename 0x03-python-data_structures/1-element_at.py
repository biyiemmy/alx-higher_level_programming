#!/usr/bin/python3

def element_at(my_list, idx):
    """
    gets an elment from a list at index idx
    Args:
        my_list - list to search
        idx - the position to access
    Return:
        None - if idx is out of range
        Data - element at idx
    """

    if 0 < idx or idx >= len(my_list):
        return my_list[idx]
    else:
        None
