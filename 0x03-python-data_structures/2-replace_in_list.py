#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """
    replace an elment from a list at index idx with elem
    Args:
        my_list - list to search
        idx - the position to access
        element - new elem to swap with
    Return:
        my_list
    """

    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
