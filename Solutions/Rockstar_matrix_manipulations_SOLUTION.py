#---------------------------------------------------------
#
# Matrix Manipulations
#
# In Mathematics, a matrix is a data type like a table
# that consists of rows and columns.
# You are asked to write functions to perform some
# mathematical operations using matrices (plural of matrix).
#
#---------------------------------------------------------
#
##### Task 1:
# Scalar Multiplication.
# Given a scalar (a number) and a matrix, multiply each
# element of the matrix by the given number and return
# that matrix
def scalar_multiplication(scalar, matrix):
    #---------------------------------------------------------
    # These are the tests your function must pass.
    #
    """
    Edge case - multiply by 0
    >>> scalar_multiplication(0, [[2, 5, 6], [3, 2, 7], [4, 2, 1], [4, 1, 8]]) # Test 1
    [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
    
    Normal case - multiply by 1 (unchanged)
    >>> scalar_multiplication(1, [[2, 5], [3, 2], [4, 2], [1, 8]]) # Test 1
    [[2, 5], [3, 2], [4, 2], [1, 8]]
    
    Normal case 
    >>> scalar_multiplication(3, [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]]) # Test 1
    [[3, 3, 3], [6, 6, 6], [9, 9, 9], [12, 12, 12]]
    
    Edge case - 0 matrix
    >>> scalar_multiplication(5, [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]) # Test 1
    [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
    
    Edge case - empty matrix
    >>> scalar_multiplication(7, []) # Test 1
    []
    
    """

    for row_index in range(len(matrix)):
        for col_index in range(len(matrix[row_index])):
            matrix[row_index][col_index] *= scalar
    return matrix

    


# Task 2
# A matrix's dimension is defined by the number
# of rows and columns it contains.  A matrix with
# m rows and n columns is denoted as an m x n matrix
# For this exercise you will be required to return a
# tuple (m, n) of the dimensions of the given matrix
#
# N.B. Some matrix operations require certain rules with the
# sizes of the corresponding matrices e.g. addition, subtration
# and some matrix multiplication
def get_matrix_dimension(matrix):
    """
    Edge Case - Empty matrix
    >>> get_matrix_dimension([]) # Test 1
    (0, 0)
    
    Normal case - 
    >>> get_matrix_dimension([[2, 5], [3, 2], [4, 2], [1, 8]]) # Test 1
    (4, 2)

    Normal case - 
    >>> get_matrix_dimension([[2, 5, 7, 9], [3, 2, 4, 2], [1, 8, 5, 6]]) # Test 1
    (3, 4)

    Normal case - one column
    >>> get_matrix_dimension([[2], [3], [2], [4], [2], [1]]) # Test 1
    (6, 1)

    Normal case - one row
    >>> get_matrix_dimension([[2, 9, 11, 3, 7, 1]]) # Test 1
    (1, 6)
    """

    num_rows = len(matrix)
    if num_rows != 0:
        num_cols = len(matrix[0])
    else:
        num_cols = 0
    return (num_rows, num_cols)

    
    
# Task 3
# Matrix A and Matrix B are said to have the same dimensions
# if they have the same number of rows and columns
# Define a predicate to determine whether two matrices have the
# same dimensions
def same_dimensions(matrix_a, matrix_b):
    """
    Edge Case - Empty matrices
    >>> same_dimensions([], []) # Test 1
    True
    
    Normal case - Same matrix
    >>> same_dimensions([[2, 5], [3, 2], [4, 2], [1, 8]], [[2, 5], [3, 2], [4, 2], [1, 8]]) # Test 1
    True

    Normal case - same columns, different rows
    >>> same_dimensions([[2, 5, 7, 9], [3, 2, 4, 2]], [[1, 8, 5, 6]]) # Test 1
    False

    Normal case - same rows, different columns
    >>> same_dimensions([[2, 3], [3, 7]], [[2], [4]]) # Test 1
    False


    """

    return get_matrix_dimension(matrix_a) == get_matrix_dimension(matrix_b)

    
    
            


# Task 2: Matrix Addition
# To add Matrix A and Matrix B, add each corresponding element
# from each matrix
# Note to add two matrices together they need to be the same
# dimensions
def matrix_addition(matrix_a, matrix_b):
     #---------------------------------------------------------
    # These are the tests your function must pass.
    #
    """
    Normal case - not same dimensions
    >>> matrix_addition([[2, 5, 6], [3, 2, 7], [4, 2, 1], [4, 1, 8]], [[3, 9, 9]]) # Test 1
    []
    
    Normal case
    >>> matrix_addition([[2, 5], [3, 2]], [[4, 2], [1, 8]]) # Test 1
    [[6, 7], [4, 10]]
    
    Normal case 
    >>> matrix_addition([], []) # Test 1
    []
    
    
    """

    # if not same dimensions return empty list
    if not same_dimensions(matrix_a, matrix_b):
        return []

    # if same dimensions
    result = []

    # loop through both matrices and add corresponding elements
    for row_index in range(len(matrix_a)):
        row = []
        for col_index in range(len(matrix_a[row_index])):
            total = matrix_a[row_index][col_index] + \
                     matrix_b[row_index][col_index]
            row.append(total)
        result.append(row)
    return result

    
#---------------------------------------------------------
# This main program executes all the tests above when this
# file is run.  Uncomment the code below if you want to
# run the tests automatically.

from doctest import testmod, REPORT_ONLY_FIRST_FAILURE
print(testmod(verbose = False,
              optionflags = REPORT_ONLY_FIRST_FAILURE))
