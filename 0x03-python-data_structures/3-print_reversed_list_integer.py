def print_reversed_list_integer(my_list=[]):
    """
    Prints integers in a list in reverse
    Args:
        my_list - list of integers defauult []
    """
    
    for i in reversed(my_list):
        print("{:d}".format(i))

