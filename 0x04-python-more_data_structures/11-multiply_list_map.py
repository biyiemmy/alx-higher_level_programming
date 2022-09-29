#!/usr/bin/python3

def weight_average(my_list=[]):
    """
    a function that returns a list with all values multiplied by a number without using any loops.
    """
    def multiply_list_map(my_list=[], number=0):
        return list(map(lambda x: x * number, my_list))
