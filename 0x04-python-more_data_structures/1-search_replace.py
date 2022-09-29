#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """
    search and replace in an element in a list
    Args: 
        my_list - the list to search
        search - element to replace
        replace - substitue for search
    """
    if my_list is None:
        return None
    return [replace if x == search else x for x in my_list]
