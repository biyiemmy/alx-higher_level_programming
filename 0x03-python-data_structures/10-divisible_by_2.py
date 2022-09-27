#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """
    find the values divisible by two in list
    Args:
        my_list - list to search
    Return:
        list of True or False
    """
    return list(map(lambda x: False if x % 2 else True, my_list))
