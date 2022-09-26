#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """
    replace an elment from a list at index idx with elem
    Args:
        my_list - list to search
        idx - the position to access
        element - new elem to swap with
    Return:
        modified my_list
    """

    copy_list = my_list[:]
    if idx < 0 or idx >= len(copy_list):
        return copy_list
    copy_list[idx] = element
    return copy_list
