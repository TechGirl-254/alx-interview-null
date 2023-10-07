#!/usr/bin/python3

def pascal_triangle(triangle):
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

         


