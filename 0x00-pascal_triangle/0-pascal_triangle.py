#!/usr/bin/python3
"""
This module helps to draw a pascal triangle
"""

def pascal_triangle(triangle):
    """
    This function takes an interger as an arguement.
    and generates a Pascal triangle with a number of rows
    corresponding to the argument.

    Args:
        triangle: an int representing the number of rows on the triangle

    Returns:
        an empty list if triangle is <= 0
        a list of a list of intergers
    """
    final_list = [[1]]
    if triangle <= 0:
        empty_list = []
        return empty_list
    else:
        for row in range(triangle - 1):
            next_row = len(final_list[-1]) + 1
            new_list = []
            for j in range(next_row):
                altered_list = [0] + final_list[-1] + [0]
                new_list.append(altered_list[j] + altered_list[j + 1])
                
            final_list.append(new_list)
    
    return final_list

         


