#!/usr/bin/python3
def pascal_triangle(n):
    """
    Returns a list of lists representing Pascal’s triangle of n.
    
    Args:
        n (int): The number of rows in the triangle.
        
    Returns:
        list: A list of lists representing Pascal's triangle.
    """
    if n <= 0:
        return []
    
    triangle = [[1]]  # The first row is always [1]
    
    for i in range(1, n):
        row = [1]  # Start each row with a 1
        
        # Calculate the middle elements of the row
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        
        row.append(1)  # End each row with a 1
        triangle.append(row)  # Add the row to the triangle
    
    return triangle

