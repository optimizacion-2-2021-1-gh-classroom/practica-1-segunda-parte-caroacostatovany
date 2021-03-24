import numpy as np

def create_matrix(variables, constraints):
    """
    Creates a matrix with enough rows for each constraint plus the objective function
    and enough columns for all the variables.
    Args:
        - variables (int): number of variables
        - constraints (int): number of constraints
    Returns:
        - matrix (numpy array)
    """
    
    matrix = np.zeros((constraints + 1, variables + constraints + 2))
    return matrix


def pivots_col(matrix):
    """
    Checks to see if pivots are required due to negative values on on right column
    excluding the bottom value
    """
    
    m = min(matrix[:-1,-1])
    if m >= 0:
        return False
    else:
        return True


def pivots_row(matrix):
    """
    Checks to see if pivots are required due to a negative values in bottom row, 
    excluding the final value
    """
    
    l = len(matrix[:,0])
    m = min(matrix[l-1,:-1])
    if m >= 0:
        return False
    else:
        return True


def find_negative_col(matrix):
    """
    Finds location of negative values on right column
    """
    
    l = len(matrix[0,:])
    m = min(matrix[:-1,l-1])
    if m<= 0:
        n = np.where(matrix[:-1,l-1] == m)[0][0]
    else:
        n = None
    return n


def find_negative_row(matrix):
    """
    Finds location of negative values in bottom row
    :param table:
    :return:
    """
    
    l = len(matrix[:,0])
    m = min(matrix[l-1,:-1])
    if m <= 0:
        n = np.where(matrix[l-1,:-1] == m)[0][0]
    else:
        n = None
    return n